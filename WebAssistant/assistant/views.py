from django.shortcuts import render
from .models import Contact, ContactNote, ContactPhone, ContactAddress
from .forms import AddContact
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
    if request.method == 'POST':
        name = request.POST['name']
        birthday = request.POST['birthday']
        email = request.POST['email']
        address = request.POST['address']
        phones = request.POST['phone']
        contact = Contact(name=name, birthday=birthday, email=email)
        contact.save()
        list_of_phones = phones.split(',')
        for phone in list_of_phones:
            add_phone = ContactPhone(contact_id_id=contact.id, phone=phone.strip())
            add_phone.save()
        list_of_addresses = address.split(',')
        for address in list_of_addresses:
            add_address = ContactAddress(contact_id_id=contact.id, address=address.strip())
            add_address.save()
        return redirect('contact_book')
    else:
        form = AddContact
    return render(request, 'pages/add_contact.html', {'form': form})


def delete_contact(request, contact_id):
    Contact.objects.filter(id=contact_id).delete()
    return redirect('contact_book')


def update_contact(request, contact_id):
    ...
