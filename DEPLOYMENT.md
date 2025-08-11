# 🚀 Django Photography Portfolio - Deployment Guide

This guide will help you deploy your Django photography portfolio to free hosting platforms.

## 📋 Prerequisites

- Your Django project is working locally
- Git repository is set up and pushed to GitHub
- Python 3.8+ knowledge

## 🌐 Free Hosting Options

### 1. **Render (Recommended - Best Free Tier)**
- **Free Tier**: 750 hours/month
- **Pros**: Easy setup, automatic deployments, good documentation
- **Cons**: Sleeps after 15 minutes of inactivity

### 2. **Railway**
- **Free Tier**: $5 credit monthly
- **Pros**: Easy deployment, supports Django, automatic HTTPS
- **Cons**: Limited free tier

### 3. **PythonAnywhere**
- **Free Tier**: Limited but good for Django
- **Pros**: Python-focused, easy Django deployment
- **Cons**: Limited bandwidth and storage

## 🚀 Deploy to Render (Step-by-Step)

### Step 1: Sign Up
1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Verify your email

### Step 2: Create New Web Service
1. Click "New +" button
2. Select "Web Service"
3. Connect your GitHub repository: `Vishal-Ubale2121/Akki`

### Step 3: Configure Service
- **Name**: `django-photography-portfolio` (or any name you prefer)
- **Environment**: `Python 3`
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn myproject.wsgi:application`

### Step 4: Set Environment Variables
Add these environment variables:

```
DEBUG=False
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
ALLOWED_HOSTS=your-app-name.onrender.com
```

### Step 5: Deploy
1. Click "Create Web Service"
2. Wait for build to complete (5-10 minutes)
3. Your app will be available at: `https://your-app-name.onrender.com`

## 🔧 Alternative: Deploy to Railway

### Step 1: Sign Up
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Create new project

### Step 2: Deploy
1. Select "Deploy from GitHub repo"
2. Choose your repository
3. Railway will auto-detect Django and deploy

## 🔧 Alternative: Deploy to PythonAnywhere

### Step 1: Sign Up
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create free account
3. Verify email

### Step 2: Upload Code
1. Go to "Files" tab
2. Upload your project or clone from GitHub
3. Install requirements: `pip install -r requirements.txt`

### Step 3: Configure Web App
1. Go to "Web" tab
2. Add new web app
3. Choose "Manual configuration"
4. Set Python version to 3.8+
5. Configure WSGI file

## 🛠️ Local Testing Before Deployment

Test your production settings locally:

```bash
# Set environment variables
set DEBUG=False
set SECRET_KEY=test-secret-key
set ALLOWED_HOSTS=localhost,127.0.0.1

# Collect static files
python manage.py collectstatic

# Test production server
python manage.py runserver
```

## 🔒 Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY`
- [ ] `ALLOWED_HOSTS` configured
- [ ] HTTPS enabled
- [ ] Static files collected
- [ ] Database migrations applied

## 📱 Post-Deployment

1. **Create Superuser**: Access admin panel
2. **Add Content**: Upload photos, testimonials
3. **Test All Pages**: Ensure everything works
4. **Monitor Logs**: Check for errors
5. **Set Up Custom Domain** (optional)

## 🚨 Common Issues & Solutions

### Issue: Static files not loading
**Solution**: Ensure `STATIC_ROOT` is set and files are collected

### Issue: Database connection error
**Solution**: Check `DATABASE_URL` environment variable

### Issue: 500 Internal Server Error
**Solution**: Check logs and ensure all environment variables are set

### Issue: Media files not working
**Solution**: Configure media file serving or use cloud storage

## 📞 Support

- **Render**: [docs.render.com](https://docs.render.com)
- **Railway**: [docs.railway.app](https://docs.railway.app)
- **PythonAnywhere**: [help.pythonanywhere.com](https://help.pythonanywhere.com)

## 🎯 Next Steps

After successful deployment:
1. Set up monitoring
2. Configure backups
3. Set up CI/CD pipeline
4. Add custom domain
5. Implement CDN for media files

---

**Happy Deploying! 🚀**
