# 🚀 Google App Engine Deployment Guide

## 📋 **Complete Step-by-Step Deployment to Google App Engine**

This guide will walk you through deploying your Django photography portfolio to Google App Engine step by step.

## 🌐 **Step 1: Set Up Google Cloud Platform**

### **1a. Create Google Cloud Account**
1. **Visit**: [console.cloud.google.com](https://console.cloud.google.com/)
2. **Sign up** with your Google account
3. **Enable billing** (required for App Engine, but free tier available)
4. **Create a new project** or select existing one

### **1b. Enable App Engine API**
1. **Go to** "APIs & Services" → "Library"
2. **Search for** "App Engine Admin API"
3. **Click** "Enable"

### **1c. Install Google Cloud SDK**
1. **Download** from [cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install)
2. **Install** following the instructions for your OS
3. **Verify installation**:
   ```bash
   gcloud --version
   ```

## 🔐 **Step 2: Authenticate and Configure**

### **2a. Authenticate with Google Cloud**
```bash
gcloud auth login
```

### **2b. Set Your Project**
```bash
gcloud config set project YOUR_PROJECT_ID
```

### **2c. Verify Configuration**
```bash
gcloud config list
```

## 🚀 **Step 3: Deploy Your App**

### **3a. Collect Static Files**
```bash
python manage.py collectstatic --noinput
```

### **3b. Deploy to App Engine**
```bash
gcloud app deploy
```

**Or use the deployment script:**
```bash
chmod +x deploy_gae.sh
./deploy_gae.sh
```

## ⚙️ **Step 4: Configure Your App**

### **4a. Create App Engine App (First Time Only)**
```bash
gcloud app create --region=us-central
```

### **4b. Set Environment Variables**
Edit `app.yaml` and update:
- `SECRET_KEY`: Your production secret key
- `DATABASE_URL`: Your database connection string

## 🗄️ **Step 5: Database Setup**

### **5a. Run Migrations**
```bash
# Option 1: Use Cloud Shell
gcloud app browse
# Then run: python manage.py migrate

# Option 2: SSH into instance
gcloud app instances ssh INSTANCE_ID
python manage.py migrate
```

### **5b. Create Superuser**
```bash
python manage.py createsuperuser
```

## 🌐 **Step 6: Test Your Deployment**

### **6a. View Your App**
```bash
gcloud app browse
```

### **6b. Check Logs**
```bash
gcloud app logs tail -s default
```

## 📁 **Project Structure After Deployment**

```
AkkiCreation/
├── app.yaml                    # App Engine configuration
├── myproject/
│   ├── settings.py            # Base settings
│   ├── settings_gae.py        # App Engine specific settings
│   └── wsgi.py                # WSGI application
├── staticfiles/                # Collected static files
├── requirements.txt            # Python dependencies
├── deploy_gae.sh              # Deployment script
└── manage.py                   # Django management
```

## 🔧 **Configuration Files Explained**

### **app.yaml**
- **runtime**: Python 3.10
- **entrypoint**: Gunicorn WSGI server
- **env_variables**: Environment configuration
- **handlers**: URL routing and static files
- **scaling**: Automatic scaling configuration

### **settings_gae.py**
- **ALLOWED_HOSTS**: Configured for App Engine domains
- **Static files**: Optimized for App Engine
- **Security**: Production-ready security settings
- **Logging**: App Engine compatible logging

## 🚨 **Common Issues & Solutions**

### **Issue: "No module named 'django'"**
**Solution**: Ensure all requirements are in `requirements.txt`

### **Issue: Static files not loading**
**Solution**: Run `python manage.py collectstatic` before deployment

### **Issue: Database connection errors**
**Solution**: Check `DATABASE_URL` in `app.yaml`

### **Issue: 500 Internal Server Error**
**Solution**: Check App Engine logs: `gcloud app logs tail`

## 💰 **Pricing & Free Tier**

- **Free Tier**: 28 instance hours per day
- **Standard Environment**: Pay per use after free tier
- **Flexible Environment**: More expensive but more control

## 🔒 **Security Best Practices**

- **Change** default secret key in production
- **Use** environment variables for sensitive data
- **Enable** App Engine security features
- **Monitor** logs regularly

## 📱 **Post-Deployment Checklist**

- [ ] App loads without errors
- [ ] All pages accessible
- [ ] Static files load correctly
- [ ] Admin panel accessible
- [ ] Database migrations completed
- [ ] Superuser account created
- [ ] Forms work properly
- [ ] Mobile responsiveness works

## 🎯 **Your App URLs**

- **Main Site**: `https://YOUR_PROJECT_ID.uc.r.appspot.com/`
- **Portfolio**: `https://YOUR_PROJECT_ID.uc.r.appspot.com/portfolio/`
- **About**: `https://YOUR_PROJECT_ID.uc.r.appspot.com/portfolio/about/`
- **Services**: `https://YOUR_PROJECT_ID.uc.r.appspot.com/portfolio/services/`
- **Contact**: `https://YOUR_PROJECT_ID.uc.r.appspot.com/portfolio/contact/`
- **Admin**: `https://YOUR_PROJECT_ID.uc.r.appspot.com/admin/`

## 🚀 **Next Steps After Deployment**

1. **Add content** through admin panel
2. **Set up custom domain** (optional)
3. **Configure monitoring** and alerts
4. **Set up CI/CD** pipeline
5. **Scale up** if needed

## 📞 **Support & Resources**

- **Google Cloud Documentation**: [cloud.google.com/appengine/docs](https://cloud.google.com/appengine/docs)
- **Django on App Engine**: [cloud.google.com/python/django/appengine](https://cloud.google.com/python/django/appengine)
- **Community Support**: [stackoverflow.com](https://stackoverflow.com/questions/tagged/google-app-engine)

---

## 🎉 **Congratulations!**

Your Django photography portfolio is now live on Google App Engine!

**Benefits of App Engine:**
- ✅ **Automatic scaling** based on traffic
- ✅ **Built-in security** and monitoring
- ✅ **Global CDN** for fast loading
- ✅ **99.95% uptime** SLA
- ✅ **Easy deployment** and updates

---

**Happy Deploying! 🚀✨**
