from django.shortcuts import render
from .models import Category,Testimonial

# Create your views here.
def categorias(request):
    categorias= Category.objects.all()
    return render(request, 'testimonials/testimonial.html',{'categorias':categorias})

def testimonials(request):
    testimonials= Testimonial.objects.all()
    return render(request, 'testimonials/testimonial.html',{'testimonials':testimonials})


