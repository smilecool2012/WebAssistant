from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_book/', views.contacts, name='contact_book'),
    path('contact_book/add_contact/', views.add_contact, name='add_contact'),
]
