from django import forms
from django.forms import ModelForm
from . import models

class VenueForm(ModelForm):
    class Meta:
        model = models.Venue
        fields = '__all__' # could also write it ('name', 'address', 'phone', 'web', 'email')

        labels = {
            'name': '',
            'address': '',
            'phone': '',
            'web': '',
            'email': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Luogo'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Indirizzo'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefono'}),
            'web': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Web'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = models.Event
        fields = ('name', 'image', 'date', 'venue', 'manager', 'description')

        labels = {
            'name': '',
            'image': '',
            'date': '',
            'venue': '', 
            'manager': '',
            'description': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data'}),
            'venue': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrizione'}),
        }