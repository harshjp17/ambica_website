"""
Run this ONCE after first migration to create the admin user.
Usage: python setup_admin.py
"""
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ambica_engineering.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

USERNAME = 'ambica2026'
PASSWORD = 'harsh@ambica17!'
EMAIL    = 'admin@ambicaengineering.in'

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(username=USERNAME, email=EMAIL, password=PASSWORD)
    print(f"✅ Superuser '{USERNAME}' created successfully!")
    print(f"   Login at: http://127.0.0.1:8000/admin/")
    print(f"   Username : {USERNAME}")
    print(f"   Password : {PASSWORD}")
else:
    print(f"ℹ️  User '{USERNAME}' already exists. Skipping.")
