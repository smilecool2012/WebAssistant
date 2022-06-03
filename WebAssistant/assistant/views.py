from django.shortcuts import render
from .models import Contact, ContactNote, ContactPhone, ContactAddress
from .forms import AddContact
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, template_name='pages/index.html', context={'title': 'Web assistant'})


def contacts(request):
    contact = Contact.objects.all()
    phones = ContactPhone.objects.all()
    addresses = ContactAddress.objects.all()
    context = {
        'contact': contact,
        'phones': phones,
        'addresses': addresses,
    }
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
        form = AddContact
        return redirect('contact_book')
    else:
        form = AddContact
    return render(request, 'pages/add_contact.html', {'form': form})
