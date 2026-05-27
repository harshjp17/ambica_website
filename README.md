# Shree Ambica Engineering — Website Setup Guide

## Quick Start (3 steps)

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Setup database & admin
```bash
python manage.py migrate
python setup_admin.py
```

### Step 3 — Run the website
```bash
python manage.py runserver
```
Visit: **http://127.0.0.1:8000**

---

## Admin Panel

URL      : http://127.0.0.1:8000/admin/
Username : **ambica2026**
Password : **harsh@ambica17!**

The admin panel lets you:
- View and manage all customer enquiries from the Contact form
- Mark enquiries as read/unread
- Filter by product type or date
- Search by name, company, email, or phone

---

## Pages

| Page     | URL          |
|----------|--------------|
| Home     | /            |
| Services | /services/   |
| About    | /about/      |
| Contact  | /contact/    |
| Admin    | /admin/      |

---

## Customisation

### Update contact details
Edit `templates/base.html` — search for `XXXXX XXXXX` and replace with your phone number and email.

### Update address
Edit `templates/base.html` — find the footer section and update the address.

### Change logo
Replace `static/images/logo.png` with your new logo file.

### Edit any page content
All page content is in `templates/main/` folder:
- `home.html` — Home page
- `services.html` — Products & Services page
- `about.html` — About Us page
- `contact.html` — Contact page

### Collect static files (for production)
```bash
python manage.py collectstatic
```

### Production settings
Before going live, update `ambica_engineering/settings.py`:
- Set `DEBUG = False`
- Set `ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']`
- Change `SECRET_KEY` to a secure random value

---

## Project Structure

```
ambica_site/
├── manage.py              # Django management
├── setup_admin.py         # One-time admin user setup
├── requirements.txt       # Python packages
├── ambica_engineering/    # Project config
│   ├── settings.py
│   └── urls.py
├── main/                  # Main app
│   ├── models.py          # Enquiry model
│   ├── views.py           # Page views
│   ├── forms.py           # Contact form
│   ├── admin.py           # Admin config
│   └── urls.py            # URL routes
├── templates/             # HTML templates
│   ├── base.html          # Base layout (nav + footer)
│   └── main/
│       ├── home.html
│       ├── services.html
│       ├── about.html
│       └── contact.html
└── static/
    ├── css/style.css      # All styles
    ├── js/main.js         # Animations & interactivity
    └── images/logo.png    # Your logo
```
