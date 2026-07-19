from app import create_app
from models import db
from sqlalchemy import inspect

app = create_app()

with app.app_context():
    print("=" * 60)
    print("📝 MEMBUAT TABEL DI TIDB CLOUD")
    print("=" * 60)
    print(f"📍 Database : {app.config['TIDB_DATABASE']}")
    print(f"📍 Host     : {app.config['TIDB_HOST']}")
    print("=" * 60)
    
    # Buat semua tabel
    print("\n📌 Membuat tabel...")
    db.create_all()
    print("✅ Tabel berhasil dibuat!")
    
    # Cek tabel yang ada
    inspector = inspect(db.engine)
    tables = inspector.get_table_names()
    print(f"\n📋 Tabel yang ada di {app.config['TIDB_DATABASE']}:")
    for table in tables:
        print(f"   - {table}")
    
    print("\n" + "=" * 60)
    print("🎉 TABEL BERHASIL DIBUAT!")
    print("=" * 60)
    print("\n📌 Sekarang jalankan: python seed.py")