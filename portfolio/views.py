from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Photo, Category, Contact, Testimonial
from .forms import ContactForm
# from .models import PortfolioSection, Photo
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


# ----------------- Public Views -----------------

def home(request):
    featured_photos = Photo.objects.filter(featured=True)[:6]
    categories = Category.objects.all()
    testimonials = Testimonial.objects.filter(featured=True)[:3]

    context = {
        'featured_photos': featured_photos,
        'categories': categories,
        'testimonials': testimonials,
    }
    return render(request, 'portfolio/home.html', context)


def portfolio(request):
    category_id = request.GET.get('category')
    if category_id:
        photos = Photo.objects.filter(category_id=category_id)
        selected_category = get_object_or_404(Category, id=category_id)
    else:
        photos = Photo.objects.all()
        selected_category = None

    categories = Category.objects.all()

    paginator = Paginator(photos, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'portfolio/portfolio.html', context)


def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    related_photos = Photo.objects.filter(category=photo.category).exclude(id=photo.id)[:4]

    context = {
        'photo': photo,
        'related_photos': related_photos,
    }
    return render(request, 'portfolio/photo_detail.html', context)


def about(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'portfolio/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('portfolio:contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)


def services(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'portfolio/services.html', context)


# ----------------- Admin Views -----------------

def is_admin_user(user):
    return user.is_staff and user.is_active


def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('portfolio:admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user and is_admin_user(user):
            login(request, user)
            return redirect('portfolio:admin_dashboard')
        else:
            messages.error(request, 'Invalid credentials or not an admin user')

    return render(request, 'portfolio/admin_login.html')


@login_required
@user_passes_test(is_admin_user)
def admin_dashboard(request):
    # Example: show some stats in dashboard
    total_photos = Photo.objects.count()
    total_categories = Category.objects.count()
    total_contacts = Contact.objects.count()

    context = {
        'total_photos': total_photos,
        'total_categories': total_categories,
        'total_contacts': total_contacts,
    }
    return render(request, 'portfolio/admin_dashboard.html', context)


@login_required
def admin_logout(request):
    logout(request)
    return redirect('portfolio:admin_login')


# def upload_photo(request):
#     if request.method == 'POST':
#         section_name = request.POST['section']
#         photo_file = request.FILES['photo']
#         section = PortfolioSection.objects.get(name=section_name)
#         Photo.objects.create(section=section, image=photo_file)
#         return redirect('admin_dashboard')
