# PhotoArt - Photographer Portfolio Django App

A professional photographer portfolio web application built with Django, inspired by the Presento theme. Features a modern, responsive design with comprehensive photography services showcase.

## Setup

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Open your browser and go to `http://127.0.0.1:8000/portfolio/`

## Admin Setup

1. Access the admin interface at `http://127.0.0.1:8000/admin/`
2. Login with username: `admin` (password was set during setup)
3. Create categories for your photos (e.g., Portrait, Wedding, Commercial)
4. Add photos with categories, descriptions, and locations
5. Create testimonials from satisfied clients
6. Manage contact form submissions

## Project Structure

- `myproject/` - Main project configuration
- `main/` - Basic Django app with simple views
- `portfolio/` - Main photographer portfolio application
- `manage.py` - Django management script
- `requirements.txt` - Python dependencies
- `media/` - Uploaded photos and testimonials

## Available URLs

### Main App
- `/` - Simple home page
- `/about/` - Simple about page

### Portfolio App
- `/portfolio/` - Portfolio home page with featured photos
- `/portfolio/portfolio/` - Full portfolio with category filtering
- `/portfolio/photo/<id>/` - Individual photo detail page
- `/portfolio/about/` - About page with photographer information
- `/portfolio/contact/` - Contact form and information
- `/portfolio/services/` - Photography services and pricing

### Admin
- `/admin/` - Django admin interface (username: admin, password: set during setup)

## Features

### Portfolio App
- **Modern, responsive design** inspired by Presento theme
- **Photo management system** with categories and metadata
- **Contact form** for client inquiries
- **Testimonials system** with ratings
- **Portfolio gallery** with filtering and pagination
- **Professional services showcase** with pricing
- **Admin interface** for content management
- **Image upload and management** with Pillow
- **SEO-friendly URLs** and breadcrumb navigation

### Technical Features
- Django 5.2.5 with modern Python practices
- Bootstrap 5 for responsive design
- Font Awesome icons
- SQLite database (easily upgradeable to PostgreSQL/MySQL)
- Media file handling for photos
- Form validation and error handling
- Pagination for large photo collections
