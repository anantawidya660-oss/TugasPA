from app import create_app
from models import db, Profile, Skill, Experience, Project, Contact
from datetime import datetime
import os

app = create_app()

with app.app_context():
    print("=" * 60)
    print("📤 EXPORT DATA KE FORMAT SQL")
    print("=" * 60)
    print(f"📍 Database : {app.config['TIDB_DATABASE']}")
    print("=" * 60)
    
    # Buat folder backup
    if not os.path.exists('backup'):
        os.makedirs('backup')
    
    sql_file = open('backup/export_data.sql', 'w', encoding='utf-8')
    
    # Header SQL
    sql_file.write(f"-- ========================================\n")
    sql_file.write(f"-- EXPORT DATA FROM TIDB CLOUD\n")
    sql_file.write(f"-- Database: {app.config['TIDB_DATABASE']}\n")
    sql_file.write(f"-- Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    sql_file.write(f"-- ========================================\n\n")
    
    sql_file.write(f"USE {app.config['TIDB_DATABASE']};\n\n")
    
    # ========================================
    # 1. PROFILES
    # ========================================
    print("\n📌 1. Export Profiles...")
    profiles = Profile.query.all()
    sql_file.write("-- ========================================\n")
    sql_file.write("-- PROFILES\n")
    sql_file.write("-- ========================================\n\n")
    
    if profiles:
        for p in profiles:
            bio = p.bio.replace("'", "''").replace("\n", "\\n") if p.bio else ''
            sql_file.write(f"INSERT INTO profiles (id, name, title, bio, email, phone, location, profile_image, github_url, linkedin_url, instagram_url, created_at, updated_at) VALUES (\n")
            sql_file.write(f"  {p.id},\n")
            sql_file.write(f"  '{p.name}',\n")
            sql_file.write(f"  '{p.title}',\n")
            sql_file.write(f"  '{bio}',\n")
            sql_file.write(f"  '{p.email}',\n")
            sql_file.write(f"  '{p.phone}',\n")
            sql_file.write(f"  '{p.location}',\n")
            sql_file.write(f"  '{p.profile_image or ''}',\n")
            sql_file.write(f"  '{p.github_url or ''}',\n")
            sql_file.write(f"  '{p.linkedin_url or ''}',\n")
            sql_file.write(f"  '{p.instagram_url or ''}',\n")
            sql_file.write(f"  '{p.created_at}',\n")
            sql_file.write(f"  '{p.updated_at}'\n")
            sql_file.write(f");\n\n")
        print(f"   ✅ Profiles: {len(profiles)} data")
    
    # ========================================
    # 2. SKILLS
    # ========================================
    print("\n📌 2. Export Skills...")
    skills = Skill.query.all()
    sql_file.write("-- ========================================\n")
    sql_file.write("-- SKILLS\n")
    sql_file.write("-- ========================================\n\n")
    
    if skills:
        for s in skills:
            sql_file.write(f"INSERT INTO skills (id, name, category, proficiency, `order`, created_at) VALUES (\n")
            sql_file.write(f"  {s.id},\n")
            sql_file.write(f"  '{s.name}',\n")
            sql_file.write(f"  '{s.category or ''}',\n")
            sql_file.write(f"  {s.proficiency},\n")
            sql_file.write(f"  {s.order},\n")
            sql_file.write(f"  '{s.created_at}'\n")
            sql_file.write(f");\n\n")
        print(f"   ✅ Skills: {len(skills)} data")
    
    # ========================================
    # 3. EXPERIENCES
    # ========================================
    print("\n📌 3. Export Experiences...")
    experiences = Experience.query.all()
    sql_file.write("-- ========================================\n")
    sql_file.write("-- EXPERIENCES\n")
    sql_file.write("-- ========================================\n\n")
    
    if experiences:
        for e in experiences:
            desc = e.description.replace("'", "''").replace("\n", "\\n") if e.description else ''
            sql_file.write(f"INSERT INTO experiences (id, company, position, location, start_date, end_date, is_current, description, `order`, created_at) VALUES (\n")
            sql_file.write(f"  {e.id},\n")
            sql_file.write(f"  '{e.company}',\n")
            sql_file.write(f"  '{e.position}',\n")
            sql_file.write(f"  '{e.location or ''}',\n")
            sql_file.write(f"  '{e.start_date}',\n")
            sql_file.write(f"  {f"'{e.end_date}'" if e.end_date else 'NULL'},\n")
            sql_file.write(f"  {1 if e.is_current else 0},\n")
            sql_file.write(f"  '{desc}',\n")
            sql_file.write(f"  {e.order},\n")
            sql_file.write(f"  '{e.created_at}'\n")
            sql_file.write(f");\n\n")
        print(f"   ✅ Experiences: {len(experiences)} data")
    
    # ========================================
    # 4. PROJECTS
    # ========================================
    print("\n📌 4. Export Projects...")
    projects = Project.query.all()
    sql_file.write("-- ========================================\n")
    sql_file.write("-- PROJECTS\n")
    sql_file.write("-- ========================================\n\n")
    
    if projects:
        for p in projects:
            desc = p.description.replace("'", "''").replace("\n", "\\n") if p.description else ''
            sql_file.write(f"INSERT INTO projects (id, title, description, category, image_url, project_url, github_url, technologies, `order`, created_at) VALUES (\n")
            sql_file.write(f"  {p.id},\n")
            sql_file.write(f"  '{p.title}',\n")
            sql_file.write(f"  '{desc}',\n")
            sql_file.write(f"  '{p.category or ''}',\n")
            sql_file.write(f"  '{p.image_url or ''}',\n")
            sql_file.write(f"  '{p.project_url or ''}',\n")
            sql_file.write(f"  '{p.github_url or ''}',\n")
            sql_file.write(f"  '{p.technologies or ''}',\n")
            sql_file.write(f"  {p.order},\n")
            sql_file.write(f"  '{p.created_at}'\n")
            sql_file.write(f");\n\n")
        print(f"   ✅ Projects: {len(projects)} data")
    
    # ========================================
    # 5. CONTACTS (jika ada)
    # ========================================
    print("\n📌 5. Export Contacts...")
    contacts = Contact.query.all()
    sql_file.write("-- ========================================\n")
    sql_file.write("-- CONTACTS\n")
    sql_file.write("-- ========================================\n\n")
    
    if contacts:
        for c in contacts:
            msg = c.message.replace("'", "''").replace("\n", "\\n") if c.message else ''
            sql_file.write(f"INSERT INTO contacts (id, name, email, subject, message, is_read, created_at) VALUES (\n")
            sql_file.write(f"  {c.id},\n")
            sql_file.write(f"  '{c.name}',\n")
            sql_file.write(f"  '{c.email}',\n")
            sql_file.write(f"  '{c.subject or ''}',\n")
            sql_file.write(f"  '{msg}',\n")
            sql_file.write(f"  {1 if c.is_read else 0},\n")
            sql_file.write(f"  '{c.created_at}'\n")
            sql_file.write(f");\n\n")
        print(f"   ✅ Contacts: {len(contacts)} data")
    
    sql_file.close()
    
    print("\n" + "=" * 60)
    print(f"✅ EXPORT SELESAI!")
    print("=" * 60)
    print(f"📁 File: backup/export_data.sql")
    print(f"📋 Isi: {len(profiles)} profiles, {len(skills)} skills, {len(experiences)} experiences, {len(projects)} projects, {len(contacts)} contacts")
    print("=" * 60)
    print("\n📌 Cara import ke database baru:")
    print("   mysql -h host -P 4000 -u user -p database < backup/export_data.sql")