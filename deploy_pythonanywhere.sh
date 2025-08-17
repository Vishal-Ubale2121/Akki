z#!/bin/bash

echo "🚀 Deploying Django Photography Portfolio to PythonAnywhere..."

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: Please run this script from your Django project root directory"
    exit 1
fi

echo "📁 Current directory: $(pwd)"

# Create static directory if it doesn't exist
echo "📁 Creating staticfiles directory..."
mkdir -p static

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Create superuser if it doesn't exist
echo "👤 Checking for superuser..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(is_superuser=True).exists():
    print('Creating superuser...')
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: username=admin, password=admin123')
else:
    print('Superuser already exists')
"

echo "✅ Deployment completed successfully!"
echo ""
echo "🔧 Next steps:"
echo "1. Go to PythonAnywhere Web tab"
echo "2. Reload your web app"
echo "3. Visit your website: https://YOUR_USERNAME.pythonanywhere.com"
echo "4. Login to admin: /admin (username: admin, password: admin123)"
echo ""
echo "🎉 Your photography portfolio is now live!"
