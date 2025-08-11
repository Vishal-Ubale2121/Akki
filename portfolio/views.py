from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Photo, Category, Contact, Testimonial
from .forms import ContactForm

# Create your views here.

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
    
    # Pagination
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
