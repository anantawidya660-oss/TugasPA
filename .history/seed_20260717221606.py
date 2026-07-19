from app import create_app
from models import db, Profile, Skill, Experience, Project
from datetime import datetime

app = create_app()

with app.app_context():
    # 1. Buat atau Update Profil
    profile = Profile.query.first()
    if not profile:
        profile = Profile()
    
    profile.name = "Yusuf Meiyosaefi"
    profile.title = "Graphic Designer & Creative Professional"
    profile.bio = """Saya adalah seorang graphic designer dengan passion dalam menciptakan visual storytelling yang bermakna. 
    Menggabungkan estetika organik dengan pendekatan modern untuk menghadirkan solusi desain yang autentik dan berkesan."""
    profile.email = "yusuf@example.com"
    profile.phone = "+62 812 3456 7890"
    profile.location = "Jakarta, Indonesia"
    profile.github_url = "https://github.com/yusufmeiyosaefi"
    profile.linkedin_url = "https://linkedin.com/in/yusufmeiyosaefi"
    profile.instagram_url = "https://instagram.com/yusufmeiyosaefi"
    
    db.session.add(profile)
    db.session.commit()
    print("✓ Profil berhasil dibuat!")
    
    # 2. Buat Skills
    skills_data = [
        {"name": "Adobe Photoshop", "category": "Design Tools", "proficiency": 95, "order": 1},
        {"name": "Adobe Illustrator", "category": "Design Tools", "proficiency": 90, "order": 2},
        {"name": "Figma", "category": "Design Tools", "proficiency": 85, "order": 3},
        {"name": "UI/UX Design", "category": "Design Skills", "proficiency": 88, "order": 4},
        {"name": "Brand Identity", "category": "Design Skills", "proficiency": 92, "order": 5},
        {"name": "Typography", "category": "Design Skills", "proficiency": 85, "order": 6},
        {"name": "Python", "category": "Programming", "proficiency": 70, "order": 7},
        {"name": "HTML & CSS", "category": "Programming", "proficiency": 75, "order": 8},
        {"name": "Flask", "category": "Programming", "proficiency": 65, "order": 9},
    ]
    
    for skill_data in skills_data:
        skill = Skill.query.filter_by(name=skill_data["name"]).first()
        if not skill:
            skill = Skill(**skill_data)
            db.session.add(skill)
    
    db.session.commit()
    print("✓ Skills berhasil dibuat!")
    
    # 3. Buat Experiences
    experiences_data = [
        {
            "company": "Creative Studio Design",
            "position": "Lead Graphic Designer",
            "location": "Jakarta, Indonesia",
            "start_date": datetime(2021, 6, 1),
            "end_date": None,
            "is_current": True,
            "description": "Memimpin tim desain untuk menciptakan brand identity dan visual assets untuk berbagai klien. Bertanggung jawab atas konsep kreatif dari awal hingga eksekusi final.",
            "order": 1
        },
        {
            "company": "Digital Agency Pro",
            "position": "UI/UX Designer",
            "location": "Bandung, Indonesia",
            "start_date": datetime(2019, 3, 1),
            "end_date": datetime(2021, 5, 31),
            "is_current": False,
            "description": "Mendesain antarmuka pengguna untuk aplikasi mobile dan web. Melakukan user research, wireframing, prototyping, dan user testing untuk memastikan pengalaman pengguna yang optimal.",
            "order": 2
        },
        {
            "company": "Freelance Designer",
            "position": "Graphic Designer",
            "location": "Remote",
            "start_date": datetime(2017, 1, 1),
            "end_date": datetime(2019, 2, 28),
            "is_current": False,
            "description": "Mengerjakan berbagai proyek desain grafis untuk klien dari berbagai industri, termasuk logo design, social media graphics, dan print materials.",
            "order": 3
        }
    ]
    
    for exp_data in experiences_data:
        exp = Experience.query.filter_by(company=exp_data["company"], position=exp_data["position"]).first()
        if not exp:
            exp = Experience(**exp_data)
            db.session.add(exp)
    
    db.session.commit()
    print("✓ Experiences berhasil dibuat!")
    
    # 4. Buat Projects
    projects_data = [
        {
            "title": "Brand Identity - EcoLife",
            "description": "Membangun identitas brand yang kuat untuk perusahaan ramah lingkungan. Meliputi logo design, color palette, typography system, dan brand guidelines.",
            "category": "Brand Identity",
            "image_url": "https://via.placeholder.com/600x400/d4820a/ffffff?text=EcoLife+Brand",
            "project_url": "https://example.com/ecolife",
            "github_url": "",
            "technologies": "Adobe Illustrator, Adobe Photoshop",
            "order": 1
        },
        {
            "title": "Mobile App - FitTrack",
            "description": "Desain UI/UX untuk aplikasi fitness tracking. Fokus pada pengalaman pengguna yang intuitif dengan visual yang memotivasi.",
            "category": "UI/UX Design",
            "image_url": "https://via.placeholder.com/600x400/d4820a/ffffff?text=FitTrack+App",
            "project_url": "https://example.com/fittrack",
            "github_url": "https://github.com/yusuf/fittrack",
            "technologies": "Figma, Adobe XD",
            "order": 2
        },
        {
            "title": "Portfolio Website - Personal",
            "description": "Website portofolio pribadi yang menampilkan karya desain dengan pendekatan visual yang warm dan organik.",
            "category": "Web Design",
            "image_url": "https://via.placeholder.com/600x400/d4820a/ffffff?text=Portfolio+Website",
            "project_url": "https://yusuf.design",
            "github_url": "https://github.com/yusuf/portfolio",
            "technologies": "Flask, HTML, CSS, JavaScript",
            "order": 3
        },
        {
            "title": "Social Media Campaign - GreenEarth",
            "description": "Kampanye media sosial untuk organisasi lingkungan. Membuat visual yang engaging dan edukatif untuk meningkatkan kesadaran publik.",
            "category": "Social Media Design",
            "image_url": "https://via.placeholder.com/600x400/d4820a/ffffff?text=GreenEarth+Campaign",
            "project_url": "https://example.com/greenearth",
            "github_url": "",
            "technologies": "Adobe Photoshop, Adobe Illustrator, After Effects",
            "order": 4
        }
    ]
    
    for proj_data in projects_data:
        project = Project.query.filter_by(title=proj_data["title"]).first()
        if not project:
            project = Project(**proj_data)
            db.session.add(project)
    
    db.session.commit()
    print("✓ Projects berhasil dibuat!")
    
    print("\n🎉 Semua data berhasil dibuat!")
    print("Sekarang buka http://localhost:5000 untuk melihat website!")