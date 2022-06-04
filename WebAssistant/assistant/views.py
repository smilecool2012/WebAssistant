from django.shortcuts import render
from .models import Contact, ContactNote, ContactPhone, ContactAddress, NoteTag
from .forms import AddContact, AddTag
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
        name = request.POST['find_contact']
        contact = Contact.objects.filter(name__contains=name)
        context.update({'contact': contact})
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
    # вид лінки тут такий : contact_book/<contact_id>/see_notes
    # тут треба буде парсити теги для кожної нотатки у темплейті ,
    # бо воно передає всі теги які є у базі
    contact_notes = ContactNote.objects.filter(contact_id=contact_id)
    note_tags = NoteTag.object.all()
    context = {
        'notes': contact_notes,
        'tags': note_tags,
    }
    return render(request, template_name='pages/see_notes.html', context=context)


def delete_note(request, contact_id, note_id):
    # вид лінки тут такий : contact_book/<contact_id>/see_notes/delete_note/<note_id>
    ContactNote.objects.filter(id=note_id).delete()
    return redirect('see_contact_notes', contact_id=contact_id)


def add_tag(request, contact_id, note_id):
    # вид лінки тут такий : contact_book/<contact_id>/see_notes/add_tag/<note_id>
    form = AddTag()
    if request.method == "POST":
        form = AddTag(request.POST)
        if form.is_valid():
            new_tag_value = request.POST['tag']
            new_tag = NoteTag(tag=new_tag_value, note_id=note_id)
            new_tag.save()
            return redirect('see_contact_notes', contact_id=contact_id)
    return render(request, 'pages/add_tag.html', {'form': form})

