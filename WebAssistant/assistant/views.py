from datetime import datetime

from django.shortcuts import render
from .models import Contact, ContactNote, ContactPhone, ContactAddress, NoteTag
from .forms import AddContact, AddTag, AddNote
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return render(request, template_name='pages/index.html', context={'title': 'Web assistant'})


def contacts(request):
    phones = ContactPhone.objects.all()
    addresses = ContactAddress.objects.all()
    context = {'phones': phones,
               'addresses': addresses, }
    if request.method == 'POST':
        valid_contacts = []
        if 'find_contact' in request.POST:
            name = request.POST['find_contact']
            valid_contacts = Contact.objects.filter(name__contains=name)
            context.update({'contact': valid_contacts})
            return render(request, template_name='pages/contact_book.html', context=context)
        elif 'find_birthday' in request.POST:
            date_interval = request.POST['find_birthday']
            for this_cnt in Contact.objects.all():
                current_date = datetime.now().date()
                this_year_birthday = datetime(
                    year=current_date.year,
                    month=this_cnt.birthday.month,
                    day=this_cnt.birthday.day,
                ).date()
                if current_date > this_year_birthday:
                    this_year_birthday = datetime(
                        year=current_date.year + 1,
                        month=this_cnt.birthday.month,
                        day=this_cnt.birthday.day,
                    ).date()
                if str((this_year_birthday - current_date).days) == date_interval:
                    valid_contacts.append(this_cnt)
        context.update({'contact': valid_contacts})
        return render(request, template_name='pages/contact_book.html', context=context)
    else:
        contact = Contact.objects.all()
        context.update({'contact': contact})
    return render(request, template_name='pages/contact_book.html', context=context)


def add_contact(request):
    form = AddContact()
    if request.method == 'POST':
        form = AddContact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            birthday = form.cleaned_data['birthday']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            phones = form.cleaned_data['phone']
            contact = Contact(name=name, birthday=birthday, email=email)
            contact.save()
            list_of_phones = phones.split(',')
            for phone in list_of_phones:
                add_phone = ContactPhone(contact_id=contact, phone=phone.strip())
                add_phone.save()
            list_of_addresses = address.split(',')
            for address in list_of_addresses:
                add_address = ContactAddress(contact_id=contact, address=address.strip())
                add_address.save()
            return redirect('contact_book')
    return render(request, 'pages/add_contact.html', {'form': form})


def delete_contact(request, contact_id):
    Contact.objects.filter(id=contact_id).delete()
    return redirect('contact_book')


def update_contact(request, contact_id):
    ...


def see_contact_notes(request, contact_id):
    contact_notes = ContactNote.objects.filter(contact_id=contact_id)
    note_tags = NoteTag.objects.all()
    context = {
        'notes': contact_notes,
        'tags': note_tags,
        'id_contact': contact_id,
    }
    return render(request, template_name='pages/see_notes.html', context=context)


def delete_note(request, contact_id, note_id):
    ContactNote.objects.filter(id=note_id).delete()
    return redirect('see_contact_notes', contact_id=contact_id)


def add_tag(request, contact_id, note_id):
    context = {'form': AddTag(),
               'id_contact': contact_id,
               'id_note': note_id,
               }
    if request.method == "POST":
        context['form'] = AddTag(request.POST)
        if context['form'].is_valid():
            new_tag_value = context['form'].cleaned_data['tag']
            new_tag = NoteTag(tag=new_tag_value, note_id=ContactNote.objects.filter(id=note_id)[0])
            new_tag.save()
            return redirect('see_contact_notes', contact_id=contact_id)
    return render(request, 'pages/add_tag.html', context)


def add_note(request, contact_id):
    context = {'form': AddNote(),
               'id_contact': contact_id
               }
    if request.method == 'POST':
        context['form'] = AddNote(request.POST)
        if context['form'].is_valid():
            note = context['form'].cleaned_data['note']
            tags = context['form'].cleaned_data['tag']
            note_to_db = ContactNote(note=note, contact_id=Contact.objects.filter(id=contact_id)[0])
            note_to_db.save()
            list_of_tags = tags.split(',')
            for tag in list_of_tags:
                tag_to_db = NoteTag(tag=tag.strip(), note_id=note_to_db)
                tag_to_db.save()
            return redirect('see_contact_notes', contact_id=contact_id)
    return render(request, 'pages/add_note.html', context)


def update_note(request, contact_id, note_id):
    ...


def detail_contact(request, contact_id):
    contact_notes = ContactNote.objects.filter(contact_id=contact_id)
    note_tags = NoteTag.objects.all()
    phones = ContactPhone.objects.filter(contact_id_id=contact_id)
    addresses = ContactAddress.objects.filter(contact_id_id=contact_id)
    contact = Contact.objects.get(pk=contact_id)
    context = {'form': AddNote,
               'id_contact': contact_id,
               'phones': phones,
               'addresses': addresses,
               'contact': contact,
               'notes': contact_notes,
               'tags': note_tags,
               }
    return render(request, 'pages/detail_contact.html', context)