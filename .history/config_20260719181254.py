import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    
    # ========================================
    # PAKAI SQLITE - LOCAL DATABASE
    # ========================================
    # Tidak perlu koneksi ke TiDB, cukup pakai file lokal
    SQLALCHEMY_DATABASE_URI = 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 280,
        'pool_size': 5,
        'max_overflow': 10,
        'echo': False
    }
    
    # ========================================
    # Atau jika ingin tetap pakai TiDB (opsional)
    # Uncomment di bawah jika ingin pakai TiDB
    # ========================================
    TIDB_HOST = os.getenv('TIDB_HOST')
    TIDB_PORT = os.getenv('TIDB_PORT', '4000')
    TIDB_USER = os.getenv('TIDB_USER')
    TIDB_PASSWORD = os.getenv('TIDB_PASSWORD')
    TIDB_DATABASE = os.getenv('TIDB_DATABASE')
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{TIDB_USER}:{TIDB_PASSWORD}@{TIDB_HOST}:{TIDB_PORT}/{TIDB_DATABASE}"
        f"?ssl=true&ssl_verify_cert=false&ssl_verify_identity=false"
    )
    
    # Cloudinary Configuration (opsional untuk local)
    CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME', '')
    CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY', '')
    CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET', '')
    
    # Resend Configuration (opsional untuk local)
    RESEND_API_KEY = os.getenv('RESEND_API_KEY', '')
    RESEND_FROM_EMAIL = os.getenv('RESEND_FROM_EMAIL', '')
    
    # Admin Credentials
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')