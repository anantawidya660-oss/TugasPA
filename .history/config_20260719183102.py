import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    
    # ========================================
    # TIDB CLOUD CONFIGURATION - HARDCODE SEMENTARA
    # ========================================
    TIDB_HOST = "gateway01.ap-southeast-1.prod.aws.tidbcloud.com"
    TIDB_PORT = "4000"
    TIDB_USER = "33m2RzHZnna78w8.root"
    TIDB_PASSWORD = "x8dPqoGNNkYPr4a4"
    TIDB_DATABASE = "tugas_db"
    
    # Connection string dengan SSL untuk TiDB Cloud
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{TIDB_USER}:{TIDB_PASSWORD}@{TIDB_HOST}:{TIDB_PORT}/{TIDB_DATABASE}"
        f"?ssl=true&ssl_verify_cert=false&ssl_verify_identity=false"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 280,
        'pool_size': 5,
        'max_overflow': 10,
        'echo': False
    }
    
    # ========================================
    # CLOUDINARY CONFIGURATION
    # ========================================
    CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME', 'bnxz3eaq')
    CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY', '149761181569115')
    CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET', 'MaBn8Ddz3MW0hnbabpGhJCacuJE')
    
    # ========================================
    # RESEND CONFIGURATION
    # ========================================
    RESEND_API_KEY = os.getenv('RESEND_API_KEY', 're_CgQ8HNsB_JxsyB7cRzzay1SRJ95gzdWYV')
    RESEND_FROM_EMAIL = os.getenv('RESEND_FROM_EMAIL', 'onboarding@resend.dev')
    
    # ========================================
    # ADMIN CREDENTIALS
    # ========================================
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin123')