from django.contrib import admin
from .models import Category,Testimonial

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Category,CategoryAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
admin.site.register(Testimonial,TestimonialAdmin)

