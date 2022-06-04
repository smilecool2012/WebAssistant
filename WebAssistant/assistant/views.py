import datetime

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
        if 'find_contact' in request.POST:
            name = request.POST['find_contact']
            contact = Contact.objects.filter(name__contains=name)
            context.update({'contact': contact})
            return render(request, template_name='pages/contact_book.html', context=context)
        elif 'find_birthday' in request.POST:
            list_of_contacts = []
            valid_contacts = []
            delta_days = 0
            contact = Contact.objects.all()
            date_interval = request.POST['find_birthday']
            for item in contact:
                list_of_contacts.append(item)
            while delta_days != date_interval:
                for item in list_of_contacts:
                    valid_days = datetime.datetime.now() + datetime.timedelta(days=delta_days)
                    for value in item.values():
                        if not isinstance(value, str):
                            if value.month == valid_days.month and value.day == valid_days.day:
                                valid_contacts.append(item)
                delta_days += 1
            for item in valid_contacts:
                date = item.get("birthday")
                valid_year = date.replace(year=datetime.datetime.now().year)
                item.update({"birthday": valid_year.strftime("%d %B")})
            return redirect('contact_book')
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
            new_tag = NoteTag(tag=new_tag_value, note_id=note_id)
            new_tag.save()
            return redirect('see_contact_notes', contact_id=contact_id)
    return render(request, 'pages/add_tag.html', context)


def add_note(request, contact_id):
    context = {'form': AddNote,
               'id_contact': contact_id
               }
    if request.method == 'POST':
        note = request.POST['note']
        tags = request.POST['tag']
        note_to_db = ContactNote(note=note, contact_id_id=contact_id)
        note_to_db.save()
        list_of_tags = tags.split(',')
        for tag in list_of_tags:
            tag_to_db = NoteTag(tag=tag.strip(), note_id_id=note_to_db.id)
            tag_to_db.save()
        return redirect('see_contact_notes', contact_id=contact_id)
    return render(request, 'pages/add_note.html', context)


def update_note(request, contact_id, note_id):
    ...
