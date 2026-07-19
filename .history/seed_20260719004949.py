from app import create_app
from models import db, Profile, Skill, Experience, Project
from datetime import datetime

app = create_app()

with app.app_context():
    # 1. Buat Profil
    profile = Profile.query.first() or Profile()
    profile.name = "Yusuf Meiyosaefi"
    profile.title = "Graphic Designer & Creative Professional"
    profile.bio = "Saya adalah seorang graphic designer dengan passion dalam menciptakan visual storytelling yang bermakna. Menggabungkan estetika organik dengan pendekatan modern untuk menghadirkan solusi desain yang autentik dan berkesan."
    profile.email = "yusuf@example.com"
    profile.phone = "+62 812 3456 7890"
    profile.location = "Jakarta, Indonesia"
    profile.github_url = "https://github.com/yusufmeiyosaefi"
    profile.linkedin_url = "https://linkedin.com/in/yusufmeiyosaefi"
    profile.instagram_url = "https://instagram.com/yusufmeiyosaefi"
    db.session.add(profile)
    
    # 2. Buat Skills (REVISED)
    skills_data = [
        # Pemodelan dan Analisis Sistem
        {"name": "Perancangan Class Diagram & UML", "category": "Pemodelan dan Analisis Sistem", "proficiency": 90, "order": 1},
        {"name": "Dokumentasi Arsitektur Web & Aplikasi", "category": "Pemodelan dan Analisis Sistem", "proficiency": 85, "order": 2},
        {"name": "StarUML", "category": "Pemodelan dan Analisis Sistem", "proficiency": 88, "order": 3},
        {"name": "Visual Paradigm", "category": "Pemodelan dan Analisis Sistem", "proficiency": 82, "order": 4},
        {"name": "Draw.io", "category": "Pemodelan dan Analisis Sistem", "proficiency": 80, "order": 5},
        # Produksi Multimedia & Kreatif
        {"name": "Desain Grafis & Visual Content", "category": "Produksi Multimedia & Kreatif", "proficiency": 92, "order": 6},
        {"name": "Adobe (Photoshop/Illustrator)", "category": "Produksi Multimedia & Kreatif", "proficiency": 90, "order": 7},
        {"name": "Canva", "category": "Produksi Multimedia & Kreatif", "proficiency": 88, "order": 8},
        {"name": "Penyuntingan Video (CapCut)", "category": "Produksi Multimedia & Kreatif", "proficiency": 80, "order": 9},
        {"name": "Manajemen Live Streaming (OBS Studio)", "category": "Produksi Multimedia & Kreatif", "proficiency": 75, "order": 10},
        # Manajemen Infrastruktur Komunitas
        {"name": "Implementasi & Pengelolaan Teknologi", "category": "Manajemen Infrastruktur Komunitas", "proficiency": 85, "order": 11},
        {"name": "WordPress", "category": "Manajemen Infrastruktur Komunitas", "proficiency": 78, "order": 12},
    ]
    for data in skills_data:
        if not Skill.query.filter_by(name=data["name"]).first():
            db.session.add(Skill(**data))
    
    # 3. Buat Experiences (REVISED)
    exp_data = [
        {
            "company": "Teknologi Desa & Infrastruktur Digital",
            "position": "Pengelola Infrastruktur Teknologi & Desain Visual",
            "location": "[Lokasi Anda]",
            "start_date": datetime(2023, 1, 1),
            "end_date": None,
            "is_current": True,
            "description": """Mengelola infrastruktur teknologi di tingkat desa serta memproduksi desain visual inovatif melalui berbagai perangkat kreatif. Mengintegrasikan solusi teknologi untuk mendukung transformasi digital di komunitas pedesaan.

Tools yang digunakan:
• Adobe (Photoshop/Illustrator)
• Canva
• OBS Studio
• CapCut
• WordPress""",
            "order": 1
        },
        {
            "company": "[Nama Perusahaan/Proyek]",
            "position": "Arsitek Sistem & Analis",
            "location": "[Lokasi Anda]",
            "start_date": datetime(2023, 6, 1),
            "end_date": None,
            "is_current": False,
            "description": """Merancang arsitektur sistem menggunakan Class Diagram untuk pengembangan aplikasi dan platform berbasis web. Memastikan struktur data yang optimal dan scalable melalui pemodelan sistem yang terstruktur.

Tools yang digunakan:
• StarUML
• Draw.io
• Visual Paradigm""",
            "order": 2
        }
    ]
    for data in exp_data:
        if not Experience.query.filter_by(company=data["company"]).first():
            db.session.add(Experience(**data))
    
    # 4. Buat Projects (REVISED)
    proj_data = [
        {
            "title": "Sistem Informasi & Dokumentasi Berbasis Web",
            "description": "Membangun dan mengelola platform publikasi berbasis web terintegrasi serta menyusun pemodelan sistem menggunakan Class Diagram untuk memastikan struktur arsitektur data yang optimal.",
            "category": "Web Development & System Analysis",
            "image_url": "",
            "project_url": "https://yusufmeiyosaefi682024105.wordpress.com/",
            "github_url": "",
            "technologies": "UML, Class Diagram, Web Development, System Design",
            "order": 1
        },
        {
            "title": "Portfolio Desain Visual & Multimedia Kreatif",
            "description": "Merancang dan memproduksi berbagai aset komunikasi visual inovatif untuk kebutuhan publikasi digital dan branding guna meningkatkan keterlibatan audiens secara efektif.",
            "category": "Multimedia & Branding Visual",
            "image_url": "",
            "project_url": "https://canva.link/1nagmqtqrhsb564",
            "github_url": "",
            "technologies": "Adobe Photoshop, Adobe Illustrator, Canva",
            "order": 2
        }
    ]
    for data in proj_data:
        if not Project.query.filter_by(title=data["title"]).first():
            db.session.add(Project(**data))
    
    db.session.commit()
    print("✅ Semua data berhasil diisi!")