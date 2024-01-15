from django.urls import path
from . import views

urlpatterns = [
    path('', views.categorias, name="Categorias"),
    path('', views.testimonials, name="testimonial"),
]