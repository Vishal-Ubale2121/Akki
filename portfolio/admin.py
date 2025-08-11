from django.contrib import admin
from .models import Category, Photo, Contact, Testimonial

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date_taken', 'location', 'featured', 'created_at']
    list_filter = ['category', 'featured', 'date_taken', 'created_at']
    search_fields = ['title', 'description', 'location']
    list_editable = ['featured']
    date_hierarchy = 'created_at'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'position', 'rating', 'featured', 'created_at']
    list_filter = ['rating', 'featured', 'created_at']
    search_fields = ['name', 'company', 'content']
    list_editable = ['featured', 'rating']
