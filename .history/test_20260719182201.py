# test_connection.py
from app import create_app
from models import db

app = create_app()

with app.app_context():
    try:
        # Cek koneksi
        result = db.session.execute('SELECT 1')
        print("✅ Koneksi ke TiDB berhasil!")
        print(f"📁 Database: {app.config['TIDB_DATABASE']}")
        print(f"📍 Host: {app.config['TIDB_HOST']}")
    except Exception as e:
        print(f"❌ Gagal koneksi: {e}")