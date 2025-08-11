#!/bin/bash

echo "🚀 Deploying Django Photography Portfolio to Google App Engine..."

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: Please run this script from your Django project root directory"
    exit 1
fi

echo "📁 Current directory: $(pwd)"

# Check if app.yaml exists
if [ ! -f "app.yaml" ]; then
    echo "❌ Error: app.yaml file not found. Please create it first."
    exit 1
fi

# Create staticfiles directory if it doesn't exist
echo "📁 Creating staticfiles directory..."
mkdir -p staticfiles

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ Error: Google Cloud SDK (gcloud) is not installed."
    echo "Please install it from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check if user is authenticated
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q .; then
    echo "🔐 Please authenticate with Google Cloud first:"
    echo "gcloud auth login"
    exit 1
fi

# Check if project is set
PROJECT_ID=$(gcloud config get-value project 2>/dev/null)
if [ -z "$PROJECT_ID" ]; then
    echo "❌ Error: No Google Cloud project is set."
    echo "Please set your project: gcloud config set project YOUR_PROJECT_ID"
    exit 1
fi

echo "✅ Using Google Cloud project: $PROJECT_ID"

# Deploy to App Engine
echo "🚀 Deploying to Google App Engine..."
gcloud app deploy --quiet

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Deployment successful!"
    echo ""
    echo "🔧 Next steps:"
    echo "1. Visit your app: https://$PROJECT_ID.uc.r.appspot.com/"
    echo "2. Run database migrations:"
    echo "   gcloud app instances ssh INSTANCE_ID"
    echo "   python manage.py migrate"
    echo "3. Create superuser:"
    echo "   python manage.py createsuperuser"
    echo ""
    echo "🌐 Your photography portfolio is now live on Google App Engine!"
    echo "URL: https://$PROJECT_ID.uc.r.appspot.com/"
else
    echo "❌ Deployment failed. Please check the error messages above."
    exit 1
fi
