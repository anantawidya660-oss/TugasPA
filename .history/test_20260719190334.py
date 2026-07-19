from app import create_app
from config import Config
import requests

app = create_app()

def test_resend():
    print("=" * 60)
    print("📧 TEST RESEND EMAIL")
    print("=" * 60)
    print(f"API Key    : {Config.RESEND_API_KEY[:10]}...")
    print(f"From Email : {Config.RESEND_FROM_EMAIL}")
    print(f"To Email   : {Config.RESEND_TO_EMAIL}")
    print("=" * 60)
    
    if not Config.RESEND_API_KEY or Config.RESEND_API_KEY == 'your-resend-api-key':
        print("❌ RESEND_API_KEY belum dikonfigurasi!")
        return
    
    try:
        response = requests.post(
            'https://api.resend.com/emails',
            headers={
                'Authorization': f'Bearer {Config.RESEND_API_KEY}',
                'Content-Type': 'application/json'
            },
            json={
                'from': Config.RESEND_FROM_EMAIL,
                'to': [Config.RESEND_TO_EMAIL],
                'subject': 'Test Email from Ananta Portfolio',
                'html': '<h1>✅ Test Email Berhasil!</h1><p>Ini adalah email test dari portfolio Ananta.</p>',
            },
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ Email test berhasil dikirim!")
            print(f"📨 Cek inbox: {Config.RESEND_TO_EMAIL}")
        else:
            print(f"❌ Gagal kirim email: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    with app.app_context():
        test_resend()