from django.db import models


# Create your models here.

# class User(models.Model):
#     username = models.CharField(100, unique=True, nullable=False)
#     email = models.EmailField(100, unique=True, nullable=False)
#     created_at = models.DateField(null=False, auto_now_add=True)
#     hash = models.CharField(255, nullable=False)
#     storage_size = models.IntegerField(default=0)
#     storage_limit = models.IntegerField(default=1e+7)
#     token_cookie = models.CharField(254, nullable=True, default=None)
#
#     def __str__(self):
#         return f"User({self.id}, {self.username}, {self.email})"
#
#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'
#         ordering = ['-created_at']


class Contact(models.Model):
    name = models.CharField(max_length=40, null=False)
    birthday = models.DateField(null=False)
    email = models.EmailField(max_length=50, unique=True, null=False)
    created_at = models.DateField(null=False, auto_now_add=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-created_at']


class ContactPhone(models.Model):
    phone = models.CharField(max_length=13)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    updated_at = models.DateField(null=False, auto_now=True)
    
    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'
        ordering = ['-updated_at']


class ContactAddress(models.Model):
    address = models.CharField(max_length=20)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    updated_at = models.DateField(null=False, auto_now=True)
    
    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'
        ordering = ['-updated_at']


class ContactNote(models.Model):
    note = models.CharField(max_length=50)
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    updated_at = models.DateField(null=False, auto_now=True)
    
    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-updated_at']


class NoteTag(models.Model):
    tag = models.CharField(max_length=20)
    note_id = models.ForeignKey(ContactNote, on_delete=models.CASCADE)
    updated_at = models.DateField(null=False, auto_now=True)
    
    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['-updated_at']
    