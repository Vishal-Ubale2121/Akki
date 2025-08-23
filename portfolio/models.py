from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/photos/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='photos')
    date_taken = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    camera_settings = models.CharField(max_length=200, blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    photo = models.ImageField(upload_to='portfolio/testimonials/', blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.company}"

"""
class PortfolioSection(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    section = models.ForeignKey(PortfolioSection, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to="portfolio_photos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.section.name} - {self.image.name}"
        """
