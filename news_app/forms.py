from django import forms
from .models import Contact, News


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body', 'slug', 'image', 'category', 'status']

