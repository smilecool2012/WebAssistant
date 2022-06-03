from django.shortcuts import render
from .models import Contact, ContactNote, ContactPhone, ContactAddress
from .forms import AddContact


# Create your views here.
def index(request):
    return render(request, template_name='pages/index.html', context={'title': 'Web assistant'})


# def contacts(request):
#     contact = Contact.objects.all()
#     context = {
#         'contact': contact
#     }
#     print(contact['name'])
#     return render(request, template_name='pages/contact_book.html', context=context)

# def contacts(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         birthday = request.POST['birthday']
#         email = request.POST['email']
#         address = request.POST['address']
#         phones = request.POST['phone']
#         contact = Contact(name=name, birthday=birthday, email=email)
#         contact.save()
#         list_of_phones = phones.split(',')
#         for phone in list_of_phones:
#             add_phone = ContactPhone(contact_id_id=contact.id, phone=phone.strip())
#             add_phone.save()
#         list_of_addresses = address.split(',')
#         for address in list_of_addresses:
#             add_address = ContactAddress(contact_id_id=contact.id, address=address.strip())
#             add_address.save()
#         form = AddContact
#     else:
#         form = AddContact
#     return render(request, 'pages/contact_book.html', {'form': form})
