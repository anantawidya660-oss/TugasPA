from app import create_app
from models import db, Profile, Skill, Experience, Project
from datetime import datetime

app = create_app()

with app.app_context():
    print("=" * 60)
    print("📝 MENGISI DATA KE TIDB CLOUD")
    print("=" * 60)
    print(f"📍 Database : {app.config['TIDB_DATABASE']}")
    print(f"📍 Host     : {app.config['TIDB_HOST']}")
    print(f"📍 User     : {app.config['TIDB_USER']}")
    print("=" * 60)
    
    # ========================================
    # 1. PROFIL
    # ========================================
    print("\n📌 1. Membuat Profil...")
    profile = Profile.query.first()
    if not profile:
        profile = Profile()
    
    profile.name = "Ananta Widya Dwi Pranata"
    profile.title = "UI/UX Designer & Visual Designer"
    profile.bio = """Perkenalkan, nama saya Ananta Widya Dwi Pranata. Saya bukan tipe orang yang ambisius secara berlebihan, namun saya meyakini bahwa setiap pekerjaan layak dilakukan dengan sebaik-baiknya. Bagi saya, kualitas adalah bentuk tanggung jawab dan penghargaan terhadap apa yang saya kerjakan, sekecil apa pun itu.

Saya memiliki ketertarikan besar di dunia desain—baik itu desain antarmuka, branding, maupun visual komunikasi. Saya menikmati proses eksplorasi ide-ide kreatif dan selalu terbuka terhadap hal-hal baru yang dapat memperkaya sudut pandang saya. Saya percaya bahwa desain yang baik tidak hanya terlihat indah, tetapi juga mampu menyampaikan pesan dan menciptakan pengalaman yang bermakna bagi penggunanya.

Di luar itu, saya adalah pribadi yang bertanggung jawab, mudah beradaptasi, dan senang bekerja dalam tim. Saya menikmati kolaborasi karena di sanalah ide-ide segar lahir dan berkembang. Saya juga gemar belajar secara mandiri—baik melalui kursus online, eksperimen pribadi, maupun membaca tren desain terkini—agar tetap relevan dan terus berkembang.

Saya datang bukan untuk menjadi yang terbaik, tetapi untuk memberikan yang terbaik dari apa yang saya miliki. Dengan pendekatan yang rendah hati namun penuh dedikasi, saya siap berkontribusi dan berkembang bersama dalam setiap proyek yang saya jalani."""
    profile.email = "ananta@email.com"
    profile.phone = "+62 812 3456 7890"
    profile.location = "Indonesia"
    profile.github_url = "https://github.com/ananta"
    profile.linkedin_url = "https://linkedin.com/in/ananta"
    profile.instagram_url = "https://instagram.com/ananta"
    
    db.session.add(profile)
    db.session.commit()
    print("   ✅ Profil berhasil dibuat!")

    # ========================================
    # 2. SKILLS
    # ========================================
    print("\n📌 2. Membuat Skills...")
    # Hapus skills lama
    Skill.query.delete()
    
    skills_data = [
        # UI/UX Design
        {"name": "UI/UX Design", "category": "UI/UX Design", "proficiency": 90, "order": 1},
        {"name": "Wireframing & Prototyping", "category": "UI/UX Design", "proficiency": 88, "order": 2},
        {"name": "Usability Testing", "category": "UI/UX Design", "proficiency": 85, "order": 3},
        {"name": "Figma", "category": "UI/UX Design", "proficiency": 92, "order": 4},
        # Visual Design
        {"name": "Brand Identity", "category": "Visual Design", "proficiency": 90, "order": 5},
        {"name": "Adobe Illustrator", "category": "Visual Design", "proficiency": 88, "order": 6},
        {"name": "Adobe Photoshop", "category": "Visual Design", "proficiency": 87, "order": 7},
        {"name": "Desain Kemasan", "category": "Visual Design", "proficiency": 85, "order": 8},
        {"name": "Typography", "category": "Visual Design", "proficiency": 86, "order": 9},
        # Web & Development
        {"name": "HTML & CSS", "category": "Web & Development", "proficiency": 80, "order": 10},
        {"name": "JavaScript", "category": "Web & Development", "proficiency": 75, "order": 11},
        {"name": "Responsive Design", "category": "Web & Development", "proficiency": 85, "order": 12},
        # Tools
        {"name": "Canva", "category": "Tools", "proficiency": 85, "order": 13},
        {"name": "StarUML", "category": "Tools", "proficiency": 80, "order": 14},
    ]
    
    for data in skills_data:
        skill = Skill(**data)
        db.session.add(skill)
    
    db.session.commit()
    print(f"   ✅ {len(skills_data)} Skills berhasil disimpan!")

    # ========================================
    # 3. EXPERIENCES
    # ========================================
    print("\n📌 3. Membuat Experiences...")
    Experience.query.delete()
    
    exp_data = [
        {
            "company": "Pixel Creative Agency",
            "position": "Senior UI/UX Designer",
            "location": "Bandung, Indonesia",
            "start_date": datetime(2019, 3, 1),
            "end_date": datetime(2021, 5, 31),
            "is_current": False,
            "description": """Mendesain antarmuka website dan aplikasi mobile untuk berbagai startup. Berkolaborasi dengan tim developer dan product manager, membuat wireframe, prototype interaktif, serta melakukan usability testing untuk meningkatkan pengalaman pengguna.""",
            "order": 1
        },
        {
            "company": "Lumina Creative House",
            "position": "Visual Designer",
            "location": "Yogyakarta, Indonesia",
            "start_date": datetime(2017, 1, 1),
            "end_date": datetime(2019, 2, 28),
            "is_current": False,
            "description": """Mengembangkan materi branding, desain kemasan produk, konten media sosial, dan materi promosi digital untuk UMKM serta perusahaan lokal dengan pendekatan desain yang modern dan konsisten.""",
            "order": 2
        }
    ]
    
    for data in exp_data:
        exp = Experience(**data)
        db.session.add(exp)
    
    db.session.commit()
    print(f"   ✅ {len(exp_data)} Experiences berhasil disimpan!")

    # ========================================
    # 4. PROJECTS
    # ========================================
    print("\n📌 4. Membuat Projects...")
    Project.query.delete()
    
    proj_data = [
        {
            "title": "Coffee Shop Branding - Kopi Nusantara",
            "description": """Merancang identitas visual lengkap untuk coffee shop lokal, mulai dari logo, kemasan produk, menu, merchandise, hingga desain media sosial agar memiliki citra brand yang kuat dan mudah dikenali.""",
            "category": "Brand Identity",
            "image_url": "",
            "project_url": "https://example.com/kopinusantara",
            "github_url": "",
            "technologies": "Adobe Illustrator, Adobe Photoshop",
            "order": 1
        },
        {
            "title": "E-Commerce Fashion Landing Page",
            "description": """Mendesain landing page modern untuk brand fashion dengan fokus pada peningkatan konversi, tampilan responsif, navigasi yang sederhana, serta pengalaman pengguna yang optimal di perangkat mobile dan desktop.""",
            "category": "Web Design",
            "image_url": "",
            "project_url": "https://example.com/fashion-store",
            "github_url": "https://github.com/ananta/fashion-landing-page",
            "technologies": "Figma, HTML, CSS, JavaScript",
            "order": 2
        }
    ]
    
    for data in proj_data:
        project = Project(**data)
        db.session.add(project)
    
    db.session.commit()
    print(f"   ✅ {len(proj_data)} Projects berhasil disimpan!")

    # ========================================
    # SELESAI
    # ========================================
    print("\n" + "=" * 60)
    print("🎉 SEMUA DATA BERHASIL DIISI KE TIDB CLOUD!")
    print("=" * 60)
    print(f"📁 Database : {app.config['TIDB_DATABASE']}")
    print(f"📍 Host     : {app.config['TIDB_HOST']}")
    print("=" * 60)
    print("\n📌 Buka http://localhost:5000 untuk melihat portfolio")
    print("📌 Login Admin: http://localhost:5000/login")
    print("   Username: admin")
    print("   Password: admin123")
    print("=" * 60)