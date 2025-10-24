from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control p-4',
                'placeholder': 'Your Name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control p-4',
                'placeholder': 'Your Email',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Message',
                'required': True
            })
        }
