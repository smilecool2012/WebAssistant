from django.contrib import admin
from .models import Contact, ContactNote, ContactPhone, ContactAddress, NoteTag

# Register your models here.
admin.site.register(Contact)
admin.site.register(ContactNote)
admin.site.register(ContactPhone)
admin.site.register(ContactAddress)
admin.site.register(NoteTag)
