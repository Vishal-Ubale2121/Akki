# 🚀 PythonAnywhere Deployment Guide

## 📋 **Complete Step-by-Step Deployment to PythonAnywhere**

This guide will walk you through deploying your Django photography portfolio to PythonAnywhere step by step.

## 🌐 **Step 1: Sign Up for PythonAnywhere**

1. **Visit**: [pythonanywhere.com](https://pythonanywhere.com)
2. **Click**: "Create a Beginner account" (Free tier)
3. **Choose**: A username (e.g., `vishalubale`, `akki-photography`)
4. **Enter**: Your email and create a password
5. **Verify**: Your email address

## 🔧 **Step 2: Access Your Dashboard**

1. **Log in** to your PythonAnywhere account
2. **Navigate** to the **"Files"** tab
3. **Click** on the **"Bash"** console (or open a new one)

## 📥 **Step 3: Clone Your GitHub Repository**

In the Bash console, run these commands:

```bash
# Clone your repository
git clone https://github.com/Vishal-Ubale2121/Akki.git

# Navigate to your project
cd Akki

# Check the contents
ls -la
```

## 📦 **Step 4: Install Dependencies**

```bash
# Create a virtual environment
python3.10 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Verify Django is installed
python -c "import django; print(django.get_version())"
```

## 🌐 **Step 5: Configure Your Web App**

1. **Go to** the **"Web"** tab
2. **Click** **"Add a new web app"**
3. **Choose** **"Manual configuration"** (not Django)
4. **Select** **Python 3.10** (or the version you have)
5. **Click** **"Next"**

## ⚙️ **Step 6: Configure WSGI File**

1. **In the "Web" tab**, click on the **WSGI configuration file** link
2. **Replace** the entire content with this:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/Akki'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings_pythonanywhere'
os.environ['DEBUG'] = 'False'
os.environ['SECRET_KEY'] = 'your-super-secret-key-here-make-it-long-and-random'
os.environ['ALLOWED_HOSTS'] = 'YOUR_USERNAME.pythonanywhere.com'

# Import Django and set up the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**⚠️ IMPORTANT**: Replace `YOUR_USERNAME` with your actual PythonAnywhere username in both places!

## 📁 **Step 7: Configure Static Files**

1. **In the "Web" tab**, scroll down to **"Static files"**
2. **Add these entries**:
   - **URL**: `/static/`
   - **Directory**: `/home/YOUR_USERNAME/Akki/staticfiles`

## 🗄️ **Step 8: Set Up Your Database**

In the Bash console:

```bash
# Navigate to your project
cd ~/Akki

# Activate virtual environment
source venv/bin/activate

# Run migrations
python manage.py migrate

# Create a superuser (follow the prompts)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

## 🚀 **Step 9: Deploy and Test**

1. **Go back** to the **"Web"** tab
2. **Click** **"Reload"** button
3. **Wait** for the reload to complete
4. **Click** on your website URL to test

## 🔑 **Step 10: Access Your Admin Panel**

1. **Visit**: `https://YOUR_USERNAME.pythonanywhere.com/admin/`
2. **Login** with your superuser credentials
3. **Start adding** content to your portfolio!

## 🎯 **Your Website URLs**

- **Main Site**: `https://YOUR_USERNAME.pythonanywhere.com/`
- **Portfolio**: `https://YOUR_USERNAME.pythonanywhere.com/portfolio/`
- **About**: `https://YOUR_USERNAME.pythonanywhere.com/portfolio/about/`
- **Services**: `https://YOUR_USERNAME.pythonanywhere.com/portfolio/services/`
- **Contact**: `https://YOUR_USERNAME.pythonanywhere.com/portfolio/contact/`
- **Admin**: `https://YOUR_USERNAME.pythonanywhere.com/admin/`

## 🚨 **Common Issues & Solutions**

### **Issue: 500 Internal Server Error**
**Solution**: Check the error logs in the "Web" tab and ensure all paths are correct

### **Issue: Static files not loading**
**Solution**: Verify static files are collected and the static files configuration is correct

### **Issue: Module not found errors**
**Solution**: Ensure your virtual environment is activated and all requirements are installed

### **Issue: Database errors**
**Solution**: Run migrations and ensure the database file has proper permissions

## 🔒 **Security Notes**

- **Change** the default superuser password after first login
- **Keep** your SECRET_KEY secure
- **Monitor** your error logs regularly
- **Backup** your database periodically

## 📱 **Post-Deployment Checklist**

- [ ] Website loads without errors
- [ ] All pages are accessible
- [ ] Static files (CSS, JS, images) load correctly
- [ ] Admin panel is accessible
- [ ] Forms work properly
- [ ] Mobile responsiveness works
- [ ] Database migrations completed
- [ ] Superuser account created

## 🎉 **Congratulations!**

Your Django photography portfolio is now live on the internet! 

**Next steps:**
1. **Add content** through the admin panel
2. **Test all features** thoroughly
3. **Share your portfolio** with the world
4. **Consider upgrading** to a paid plan for more features

---

**Need help?** Check the PythonAnywhere help documentation or community forums!

**Happy Deploying! 🚀✨**
