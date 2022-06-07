from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact_book/', views.contacts, name='contact_book'),
    path('contact_book/add_contact/', views.add_contact, name='add_contact'),
    path('note_book/add_note', views.add_note, name='add_note'),
    path('contact_book/del_contact/<contact_id>', views.delete_contact, name='delete_contact'),
    path('note_book/', views.notes, name='note_book'),
    path('note_book/del_note/<note_id>', views.delete_note, name='delete_note'),
    path('contact_book/note_book/add_tag/<note_id>', views.add_tag, name='add_tag'),
    path('contact_book/detail/<contact_id>', views.detail_contact, name='detail_contact'),
    path('note_book/detail_note/<note_id>', views.detail_note, name='detail_note'),
    path('contact_book/change_name/<contact_id>', views.change_name, name='change_name'),
    path('contact_book/change_birthday/<contact_id>', views.change_birthday, name='change_birthday'),
    path('contact_book/add_phone/<contact_id>', views.add_phone, name='add_phone'),
    path('contact_book/detail/<contact_id>/delete_phone/<phone_value>', views.delete_phone, name='delete_phone'),
    path('contact_book/change_email/<contact_id>/', views.change_email, name='change_email'),
    path('contact_book/change_address/<contact_id>/', views.change_address, name='change_address'),
    path('note_book/change_note/<note_id>', views.change_note_name, name='change_note_name'),
    path('note_book/change_note_description/<note_id>', views.change_note_description, name='change_note_description'),
    path('note_book/change_note_status/<note_id>', views.change_note_status, name='change_note_status'),
    path('note_book/note_detail/<note_id>/delete_tag/<tag_id>', views.delete_note_tags, name='delete_note_tags'),
]
