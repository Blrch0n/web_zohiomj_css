#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTML файлуудад CSS холбох ба HTML бүтцийг FLEX layout руу шилжүүлэх
"""

import os
import re

def add_css_and_update_structure(filepath, is_root=False):
    """HTML файлд CSS холбох ба бүтцийг шинэчлэх"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # CSS холбоос нэмэх
        css_path = 'styles/main.css' if is_root else '../styles/main.css'
        
        # HEAD хэсэгт CSS холбоос нэмэх
        if '<link rel="stylesheet"' not in content:
            css_link = f'<link rel="stylesheet" href="{css_path}">'
            content = content.replace('</head>', f'  {css_link}\n</head>')
        
        # BODY бүтцийг шинэчлэх - Container классаар ороох
        if '<body>' in content and 'class="container"' not in content:
            content = content.replace('<body>', '<body>\n<div class="container">')
            # Container-ийг хаах
            content = content.replace('</body>', '</div>\n</body>')
        
        # Хуудасны толгой хэсгийг шинэчлэх
        # Толгой хэсэгт класс нэмэх
        content = re.sub(
            r'<!-- Толгой хэсэг -->\s*<table[^>]*>',
            '<!-- Толгой хэсэг -->\n<header class="header fade-in">',
            content
        )
        
        # Хөл хэсэгт класс нэмэх
        content = re.sub(
            r'<!-- Хөл хэсэг -->\s*<table[^>]*>',
            '<!-- Хөл хэсэг -->\n<footer class="footer">',
            content
        )
        
        # Үндсэн агуулгад main class нэмэх
        # <br> дараах эхний <h2> олоод main section нээх
        if '<main class="main-content">' not in content:
            content = re.sub(
                r'(<br>\s*<h2>)',
                r'<main class="main-content fade-in">\n\1',
                content,
                count=1
            )
            
            # Main section-ийг footer өмнө хаах
            content = re.sub(
                r'(<br>\s*<!-- Хөл хэсэг -->)',
                r'</main>\n\n\1',
                content
            )
        
        # Файл хадгалах
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ CSS нэмсэн: {filepath}")
        return True
        
    except Exception as e:
        print(f"✗ Алдаа: {filepath} - {e}")
        return False

def main():
    """Бүх HTML файлуудад CSS нэмэх"""
    
    # Үндсэн файлууд
    print("\n📁 Үндсэн файлуудад CSS нэмж байна...")
    for filename in ['index.html', 'login.html', 'register.html']:
        add_css_and_update_structure(filename, is_root=True)
    
    # Гишүүдийн файлууд
    folders = ['member1', 'member2', 'member3', 'member4', 'member5', 'member6']
    
    for folder in folders:
        print(f"\n📁 {folder}/ хавтаст CSS нэмж байна...")
        
        if not os.path.exists(folder):
            continue
        
        html_files = [f for f in os.listdir(folder) if f.endswith('.html')]
        
        for html_file in sorted(html_files):
            filepath = os.path.join(folder, html_file)
            add_css_and_update_structure(filepath, is_root=False)
    
    print(f"\n{'='*60}")
    print(f"✅ Бүх файлд CSS амжилттай холбогдлоо!")
    print(f"CSS файл: styles/main.css")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
