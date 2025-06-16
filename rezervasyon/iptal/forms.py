# iptal/forms.py
from django import forms
from .models import IptalBasvuru

class IptalBasvuruForm(forms.ModelForm):
    class Meta:
        model = IptalBasvuru
        fields = ['ad', 'soyad', 'telefon', 'email', 'mesaj']
        # veya exclude:
        # exclude = ['rezervasyon_tarihi', 'ucret', 'basvuru_tarihi']
        widgets = {
            'ad': forms.TextInput(attrs={'class': 'form-control'}),
            'soyad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mesaj': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
