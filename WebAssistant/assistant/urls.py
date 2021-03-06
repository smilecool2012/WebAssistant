from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_book/', views.contacts, name='contact_book'),
    path('contact_book/add_contact/', views.add_contact, name='add_contact'),
    path('contact_book/<contact_id>/see_notes/add_note', views.add_note, name='add_note'),
    path('contact_book/del_contact/<contact_id>', views.delete_contact, name='delete_contact'),
    path('contact_book/update_contact/<contact_id>', views.update_contact, name='update_contact'),
    path('contact_book/<contact_id>/see_notes', views.see_contact_notes, name='see_contact_notes'),
    path('contact_book/<contact_id>/see_notes/delete_note/<note_id>', views.delete_note, name='delete_note'),
    path('contact_book/<contact_id>/see_notes/add_tag/<note_id>', views.add_tag, name='add_tag'),
]
