from django import forms
from .models import Contact


class AddContact(forms.Form):
    name = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'contact_name'}))
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'date_form'}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class': 'email_form'}))
    address = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'address_form'}))
    phone = forms.CharField(max_length=250, widget=forms.TextInput(attrs={'class': 'phone_form'}))

    def clean(self):

        super(AddContact, self).clean()

        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        address = [addr.strip() for addr in self.cleaned_data['address'].split(',')]
        phones = [phn.strip() for phn in self.cleaned_data['phone'].split(',')]

        all_emails = [cnt.email for cnt in Contact.objects.all()]

        if len(name) > 40:
            self._errors['name'] = self.error_class(['Name length is maximum 40 characters'])
        if len(email) > 50:
            self._errors['email'] = self.error_class(['Email length is maximum 50 characters'])
        if email in all_emails:
            self._errors['email'] = self.error_class(['Contact with this email is already in the book'])
        for this_phone in phones:
            if len(this_phone) > 13:
                self._errors['phone'] = self.error_class(['Phone length is maximum 13 characters'])
                break
            if not this_phone[1:].isdigit() or not this_phone.startswith('+'):
                self._errors['phone'] = self.error_class(['Phone must start with + and contain only digits'])
        for this_addr in address:
            if len(this_addr) > 20:
                self._errors['address'] = self.error_class(['Address length is maximum 20 characters'])
                break

        return self.cleaned_data


class AddTag(forms.Form):
    tag = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'tag_form'}))

    def clean(self):

        super(AddTag, self).clean()

        tags = [tg.strip() for tg in self.cleaned_data['tag'].split(',')]

        for this_tag in tags:
            if len(this_tag) > 20:
                self._errors['tag'] = self.error_class(['Tag length is maximum 20 characters'])
                break

        return self.cleaned_data


class AddNote(forms.Form):
    note = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'note_name'}))
    tag = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'tags'}))

    def clean(self):

        super(AddNote, self).clean()

        note_to_add = self.cleaned_data['note']
        tags = [tg.strip() for tg in self.cleaned_data['tag'].split(',')]

        if len(note_to_add) > 50 :
            self._errors['note'] = self.error_class(['Note length is maximum 50 characters'])
        for this_tag in tags:
            if len(this_tag) > 20:
                self._errors['tag'] = self.error_class(['Tag length is maximum 20 characters'])
                break

        return self.cleaned_data
