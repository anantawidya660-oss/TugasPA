from app import create_app
from models import db
from sqlalchemy import text

app = create_app()

with app.app_context():
    print("=" * 50)
    print("📋 CEK KONEKSI TIDB")
    print("=" * 50)
    print(f"📁 Database : {app.config['TIDB_DATABASE']}")
    print(f"📍 Host     : {app.config['TIDB_HOST']}")
    print(f"👤 User     : {app.config['TIDB_USER']}")
    print("=" * 50)
    
    try:
        # Cek koneksi
        result = db.session.execute(text('SELECT 1'))
        print("✅ Koneksi ke TiDB berhasil!")
        
        # Cek database aktif
        result = db.session.execute(text('SELECT DATABASE()'))
        current_db = result.scalar()
        print(f"📌 Database aktif: {current_db}")
        
        print("=" * 50)
    except Exception as e:
        print(f"❌ Gagal koneksi: {e}")