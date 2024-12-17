from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('contact-us/', views.add_contact_us, name='contact_us'),
]
