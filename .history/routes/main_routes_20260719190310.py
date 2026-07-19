from flask import Blueprint, render_template, request, jsonify
from models import db, Profile, Skill, Experience, Project, Contact
from config import Config
import cloudinary.uploader
import requests
import json

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    profile = Profile.query.first()
    skills = Skill.query.order_by(Skill.order).all()
    experiences = Experience.query.order_by(Experience.order).all()
    projects = Project.query.order_by(Project.order).all()
    
    # Group skills by category
    skill_categories = {}
    for skill in skills:
        if skill.category not in skill_categories:
            skill_categories[skill.category] = []
        skill_categories[skill.category].append(skill)
    
    if not profile:
        profile = Profile()
    
    return render_template('index.html', 
                         profile=profile, 
                         skill_categories=skill_categories,
                         experiences=experiences,
                         projects=projects)

@bp.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.form
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        # Validasi input
        if not name or not email or not message:
            return jsonify({'success': False, 'message': 'Semua field wajib diisi!'}), 400
        
        # Save to database
        contact = Contact(name=name, email=email, subject=subject, message=message)
        db.session.add(contact)
        db.session.commit()
        
        # Send email via Resend
        email_result = send_email_via_resend(name, email, subject, message)
        
        if email_result.get('success'):
            return jsonify({'success': True, 'message': 'Pesan berhasil dikirim!'})
        else:
            # Email gagal, tapi data sudah tersimpan
            return jsonify({'success': True, 'message': 'Pesan tersimpan, tetapi email gagal terkirim.'})
            
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

def send_email_via_resend(name, email, subject, message):
    """Kirim email menggunakan Resend API"""
    api_key = Config.RESEND_API_KEY
    from_email = Config.RESEND_FROM_EMAIL
    to_email = Config.RESEND_TO_EMAIL
    
    if not api_key or api_key == 'your-resend-api-key':
        return {'success': False, 'message': 'RESEND_API_KEY belum dikonfigurasi'}
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Inter', sans-serif; background: #f7f3ec; padding: 40px; }}
            .container {{ max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 16px; padding: 40px; box-shadow: 0 20px 60px rgba(0,0,0,0.06); }}
            .header {{ border-bottom: 3px solid #d4820a; padding-bottom: 20px; margin-bottom: 24px; }}
            .header h2 {{ color: #000a24; font-family: 'Sora', sans-serif; margin: 0; }}
            .header span {{ color: #d4820a; }}
            .field {{ margin-bottom: 16px; }}
            .field label {{ font-weight: 600; color: #000a24; display: block; margin-bottom: 4px; font-size: 13px; }}
            .field p {{ color: #4b5563; margin: 0; padding: 8px 12px; background: #f9fafb; border-radius: 8px; }}
            .message-box {{ background: #f9fafb; border-radius: 8px; padding: 16px; margin-top: 8px; border-left: 4px solid #d4820a; }}
            .message-box p {{ color: #4b5563; margin: 0; white-space: pre-wrap; }}
            .footer {{ margin-top: 24px; padding-top: 16px; border-top: 1px solid #e5e7eb; text-align: center; color: #9ca3af; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h2>✦ <span>Ananta</span> Portfolio</h2>
            </div>
            <h3 style="color: #000a24; margin-bottom: 20px;">📩 Pesan Baru dari Kontak</h3>
            
            <div class="field">
                <label>Nama</label>
                <p><strong>{name}</strong></p>
            </div>
            
            <div class="field">
                <label>Email</label>
                <p><a href="mailto:{email}" style="color: #d4820a; text-decoration: none;">{email}</a></p>
            </div>
            
            <div class="field">
                <label>Subjek</label>
                <p>{subject if subject else '-'}</p>
            </div>
            
            <div class="field">
                <label>Pesan</label>
                <div class="message-box">
                    <p>{message}</p>
                </div>
            </div>
            
            <div class="footer">
                <p>Dikirim dari portfolio Ananta Widya Dwi Pranata</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    try:
        response = requests.post(
            'https://api.resend.com/emails',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'from': from_email,
                'to': [to_email],
                'subject': f'Portfolio Contact: {subject if subject else "Pesan Baru"}',
                'html': html_content,
                'reply_to': email
            },
            timeout=30
        )
        
        if response.status_code == 200:
            return {'success': True}
        else:
            return {'success': False, 'message': response.text}
            
    except requests.exceptions.RequestException as e:
        return {'success': False, 'message': str(e)}