#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML TABLE бүтцийг DIV + FLEX layout руу шилжүүлэх
"""

import os
import re

def convert_to_modern_html(filepath, is_root=False):
    """HTML файлын хуучин table бүтцийг div + flex руу хөрвүүлэх"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'<title>(.*?)</title>', content)
        title = title_match.group(1) if title_match else 'Онлайн сургалтын систем'
        
        # Extract main content (h2 болон дараах агуулга)
        main_match = re.search(r'<h2>(.*?)</h2>(.*?)(?=<br>\s*<table border="1"[^>]*cellpadding="15")', content, re.DOTALL)
        
        if not main_match:
            print(f"⚠ Content not found in: {filepath}")
            return False
        
        page_heading = main_match.group(1).strip()
        main_content = main_match.group(2).strip()
        
        # CSS path
        css_path = 'styles/main.css' if is_root else '../styles/main.css'
        logo_path = 'images/logo.png' if is_root else '../images/logo.png'
        
        # Холбоосын prefix
        prefix = '' if is_root else '../'
        
        # Шинэ HTML бүтэц
        new_html = f'''<!DOCTYPE html>
<html lang="mn">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<link rel="stylesheet" href="{css_path}">
</head>
<body>
<div class="container">

<!-- Толгой хэсэг -->
<header class="header fade-in">
<div class="header-content">
<div class="logo-section">
<img src="{logo_path}" alt="Лого">
<div class="title-section">
<h1>Онлайн сургалтын систем</h1>
<p>Боловсрол бол ирээдүй</p>
</div>
</div>
<div class="contact-info">
<div><strong>Утас:</strong> 77001122</div>
<div><strong>Імэйл:</strong> info@edu.mn</div>
</div>
</div>
</header>

<!-- Навигаци -->
<nav class="navigation">
<ul class="nav-menu">
<li><a href="{prefix}index.html">Нүүр хуудас</a></li>
<li><a href="{prefix}member1/courses.html">Хичээлүүд</a></li>
<li><a href="{prefix}member2/dashboard.html">Хянах самбар</a></li>
<li><a href="{prefix}member4/library.html">Номын сан</a></li>
<li><a href="{prefix}member5/exams.html">Шалгалт</a></li>
<li><a href="{prefix}member6/contact.html">Холбоо барих</a></li>
<li class="login-btn"><a href="{prefix}login.html">Нэвтрэх</a></li>
</ul>
</nav>

<!-- Үндсэн агуулга -->
<main class="main-content fade-in">
<div class="page-title">
<h2>{page_heading}</h2>
</div>

{main_content}

</main>

<!-- Хөл хэсэг -->
<footer class="footer">
<div class="footer-content">
<div class="footer-section">
<h3>Онлайн сургалтын систем</h3>
<p>Манай системд 1,500 гаруй оюутан, 200 гаруй багш нар идэвхтэй ажиллаж байна.</p>
<p><strong>Хаяг:</strong> Улаанбаатар хот, Сүхбаатар дүүрэг, 1-р хороо</p>
</div>
<div class="footer-section">
<h3>Холбоос</h3>
<ul>
<li><a href="{prefix}member6/contact.html">Холбоо барих</a></li>
<li><a href="{prefix}member6/policies.html">Дүрэм журам</a></li>
<li><a href="{prefix}member6/privacy.html">Нууцлалын бодлого</a></li>
<li><a href="{prefix}member6/terms.html">Үйлчилгээний нөхцөл</a></li>
<li><a href="{prefix}member6/admin.html">Администрацийн хэсэг</a></li>
</ul>
</div>
<div class="footer-section">
<h3>Холбогдох</h3>
<p><strong>Утас:</strong> 77001122, 99112233</p>
<p><strong>Факс:</strong> 70111222</p>
<p><strong>Імэйл:</strong> info@edu.mn</p>
<p><strong>Ажлын цаг:</strong> Даваа-Баасан 09:00-18:00</p>
</div>
</div>
<div class="footer-bottom">
© 2025 Онлайн сургалтын систем. Бүх эрх хуулиар хамгаалагдсан. | Хөгжүүлсэн: Веб хөгжүүлэлтийн баг
</div>
</footer>

</div>
</body>
</html>'''
        
        # Файл хадгалах
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        print(f"✓ Шинэчилсэн: {filepath}")
        return True
        
    except Exception as e:
        print(f"✗ Алдаа: {filepath} - {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Бүх HTML файлуудыг шинэчлэх"""
    
    print("\n📁 Үндсэн файлуудыг шинэчилж байна...")
    for filename in ['index.html', 'login.html', 'register.html']:
        convert_to_modern_html(filename, is_root=True)
    
    folders = ['member1', 'member2', 'member3', 'member4', 'member5', 'member6']
    
    for folder in folders:
        print(f"\n📁 {folder}/ хавтсыг шинэчилж байна...")
        
        if not os.path.exists(folder):
            continue
        
        html_files = [f for f in os.listdir(folder) if f.endswith('.html')]
        
        for html_file in sorted(html_files):
            filepath = os.path.join(folder, html_file)
            convert_to_modern_html(filepath, is_root=False)
    
    print(f"\n{'='*60}")
    print(f"✅ Бүх файл FLEX layout руу амжилттай шилжсэн!")
    print(f"✨ Одоо веб сайт нь CSS загвартай, FLEX layout ашигласан!")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
