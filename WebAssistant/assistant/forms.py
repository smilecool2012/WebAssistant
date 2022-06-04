from django import forms
from .models import NoteTag


class AddContact(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'contact_name'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'date_form'}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'email_form'}))
    address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'address_form'}))
    phone = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'phone_form'}))


class AddTag(forms.Form):
    tag = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'tag_form'}))


class AddNote(forms.Form):
    note = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'note_name'}))
    tag = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'tags'}))
    