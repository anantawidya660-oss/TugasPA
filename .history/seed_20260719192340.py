from app import create_app
from models import db, Profile, Skill, Experience, Project
from datetime import datetime

app = create_app()

with app.app_context():
    print("=" * 60)
    print("🔄 UPDATE DATA: ANANTA → YUSUF (REMOVE OLD DATA)")
    print("=" * 60)
    print(f"📍 Database : {app.config['TIDB_DATABASE']}")
    print("=" * 60)
    
    # ========================================
    # REMOVE ALL OLD DATA (kecuali Profile di-update)
    # ========================================
    print("\n🗑️  Menghapus data lama...")
    
    # Hapus semua data terkait
    Project.query.delete()
    Experience.query.delete()
    Skill.query.delete()
    print("   ✅ Projects, Experiences, Skills dihapus!")
    
    # ========================================
    # 1. UPDATE PROFIL
    # ========================================
    print("\n📌 1. Update Profil...")
    profile = Profile.query.first()
    if profile:
        profile.name = "Yusuf Meiyosaefi"
        profile.title = "Graphic Designer & Creative Professional"
        profile.bio = """Saya adalah seorang graphic designer dengan passion dalam menciptakan visual storytelling yang bermakna. Menggabungkan estetika organik dengan pendekatan modern untuk menghadirkan solusi desain yang autentik dan berkesan."""
        profile.email = "682024105@student.uksw.edu"
        profile.phone = "62 853-4971-3710"
        profile.location = "Indonesia"
        profile.github_url = "https://github.com/yusufmeiyosaefi"
        profile.linkedin_url = "https://linkedin.com/in/yusufmeiyosaefi"
        profile.instagram_url = "https://instagram.com/yusufmeiyosaefi"
        db.session.commit()
        print("   ✅ Profil berhasil diupdate!")
    else:
        print("   ❌ Profil tidak ditemukan, membuat baru...")
        profile = Profile(
            name="Yusuf Meiyosaefi",
            title="Graphic Designer & Creative Professional",
            bio="Saya adalah seorang graphic designer dengan passion dalam menciptakan visual storytelling yang bermakna. Menggabungkan estetika organik dengan pendekatan modern untuk menghadirkan solusi desain yang autentik dan berkesan.",
            email="682024105@student.uksw.edu",
            phone="62 853-4971-3710",
            location="Indonesia",
            github_url="https://github.com/yusufmeiyosaefi",
            linkedin_url="https://linkedin.com/in/yusufmeiyosaefi",
            instagram_url="https://instagram.com/yusufmeiyosaefi"
        )
        db.session.add(profile)
        db.session.commit()
        print("   ✅ Profil baru berhasil dibuat!")
    
    # ========================================
    # 2. BUAT SKILLS BARU
    # ========================================
    print("\n📌 2. Membuat Skills baru...")
    
    skills_data = [
        # Design Tools
        {"name": "Adobe Photoshop", "category": "Design Tools", "proficiency": 95, "order": 1},
        {"name": "Adobe Illustrator", "category": "Design Tools", "proficiency": 90, "order": 2},
        {"name": "Figma", "category": "Design Tools", "proficiency": 85, "order": 3},
        
        # Pemodelan dan Analisis Sistem
        {"name": "Perancangan Class Diagram & UML", "category": "Pemodelan dan Analisis Sistem", "proficiency": 90, "order": 4},
        {"name": "Dokumentasi Arsitektur Web & Aplikasi", "category": "Pemodelan dan Analisis Sistem", "proficiency": 85, "order": 5},
        {"name": "StarUML", "category": "Pemodelan dan Analisis Sistem", "proficiency": 88, "order": 6},
        {"name": "Visual Paradigm", "category": "Pemodelan dan Analisis Sistem", "proficiency": 82, "order": 7},
        {"name": "Draw.io", "category": "Pemodelan dan Analisis Sistem", "proficiency": 80, "order": 8},
        
        # Design Skills
        {"name": "UI/UX Design", "category": "Design Skills", "proficiency": 88, "order": 9},
        {"name": "Brand Identity", "category": "Design Skills", "proficiency": 92, "order": 10},
        {"name": "Typography", "category": "Design Skills", "proficiency": 85, "order": 11},
        
        # Produksi Multimedia & Kreatif
        {"name": "Desain Grafis & Visual Content", "category": "Produksi Multimedia & Kreatif", "proficiency": 92, "order": 12},
        {"name": "Adobe (Photoshop/Illustrator)", "category": "Produksi Multimedia & Kreatif", "proficiency": 90, "order": 13},
        {"name": "Canva", "category": "Produksi Multimedia & Kreatif", "proficiency": 88, "order": 14},
        {"name": "Penyuntingan Video (CapCut)", "category": "Produksi Multimedia & Kreatif", "proficiency": 80, "order": 15},
        {"name": "Manajemen Live Streaming (OBS Studio)", "category": "Produksi Multimedia & Kreatif", "proficiency": 75, "order": 16},
        
        # Programming
        {"name": "Python", "category": "Programming", "proficiency": 70, "order": 17},
        {"name": "HTML & CSS", "category": "Programming", "proficiency": 75, "order": 18},
        {"name": "Flask", "category": "Programming", "proficiency": 65, "order": 19},
        
        # Manajemen Infrastruktur Komunitas
        {"name": "Implementasi & Pengelolaan Teknologi", "category": "Manajemen Infrastruktur Komunitas", "proficiency": 85, "order": 20},
        {"name": "WordPress", "category": "Manajemen Infrastruktur Komunitas", "proficiency": 78, "order": 21},
    ]
    
    for data in skills_data:
        skill = Skill(**data)
        db.session.add(skill)
    db.session.commit()
    print(f"   ✅ {len(skills_data)} Skills berhasil dibuat!")
    
    # ========================================
    # 3. BUAT EXPERIENCES BARU
    # ========================================
    print("\n📌 3. Membuat Experiences baru...")
    
    exp_data = [
        {
            "company": "Teknologi Desa & Infrastruktur Digital",
            "position": "Pengelola Infrastruktur Teknologi & Desain Visual",
            "location": "Indonesia",
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
            "company": "Digital Agency Pro",
            "position": "UI/UX Designer & System Analyst",
            "location": "Indonesia",
            "start_date": datetime(2021, 6, 1),
            "end_date": datetime(2022, 12, 31),
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
        exp = Experience(**data)
        db.session.add(exp)
    db.session.commit()
    print(f"   ✅ {len(exp_data)} Experiences berhasil dibuat!")
    
    # ========================================
    # 4. BUAT PROJECTS BARU
    # ========================================
    print("\n📌 4. Membuat Projects baru...")
    
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
        project = Project(**data)
        db.session.add(project)
    db.session.commit()
    print(f"   ✅ {len(proj_data)} Projects berhasil dibuat!")
    
    # ========================================
    # 5. VERIFIKASI
    # ========================================
    print("\n📊 Verifikasi Data:")
    print(f"   👤 Profil: {Profile.query.count()} data")
    print(f"   🛠️ Skills: {Skill.query.count()} data")
    print(f"   💼 Experiences: {Experience.query.count()} data")
    print(f"   📁 Projects: {Project.query.count()} data")
    
    # Tampilkan profil terbaru
    profile = Profile.query.first()
    if profile:
        print(f"\n📋 Profil Terbaru:")
        print(f"   Nama  : {profile.name}")
        print(f"   Title : {profile.title}")
        print(f"   Email : {profile.email}")
        print(f"   Phone : {profile.phone}")
    
    print("\n" + "=" * 60)
    print("🎉 DATA BERHASIL DIUPDATE KE YUSUF MEIYOSAEFI!")
    print("=" * 60)
    print(f"📁 Database : {app.config['TIDB_DATABASE']}")
    print("=" * 60)
    print("\n📌 Buka http://localhost:5000 untuk melihat portfolio")
    print("📌 Login Admin: http://localhost:5000/login")
    print("   Username: admin")
    print("   Password: admin123")
    print("=" * 60)