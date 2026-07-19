import os  # ← Pastikan ini ada
from flask import Flask, render_template, redirect, url_for, request, session
from config import Config
from models import db
from routes import main_routes, admin_routes, api_routes
import cloudinary
import cloudinary.uploader

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize Database
    db.init_app(app)
    
    # Configure Cloudinary
    if app.config['CLOUDINARY_CLOUD_NAME']:
        cloudinary.config(
            cloud_name=app.config['CLOUDINARY_CLOUD_NAME'],
            api_key=app.config['CLOUDINARY_API_KEY'],
            api_secret=app.config['CLOUDINARY_API_SECRET']
        )
    
    # Register Blueprints
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(admin_routes.bp, url_prefix='/admin')
    app.register_blueprint(api_routes.bp, url_prefix='/api')
    
    # Login route
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']:
                session['logged_in'] = True
                return redirect(url_for('admin.dashboard'))
            else:
                return render_template('login.html', error='Username atau password salah!')
        
        return render_template('login.html')
    
    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        return redirect(url_for('main.index'))
    
    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app = create_app()
    app.run(debug=False, host='0.0.0.0', port=port)