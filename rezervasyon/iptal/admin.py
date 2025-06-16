# iptal/admin.py
from django.contrib import admin
from .models import IptalBasvuru

@admin.register(IptalBasvuru)
class IptalBasvuruAdmin(admin.ModelAdmin):
    list_display = (
        'ad', 'soyad', 'email', 'telefon',
        'rezervasyon_tarihi', 'ucret', 'basvuru_tarihi'
    )
    list_filter = ('rezervasyon_tarihi',)
    search_fields = ('ad', 'soyad', 'email')
    # detay sayfasında hangi alanlar sıralı gelsin:
    fields = (
        ('ad', 'soyad'),
        ('telefon', 'email'),
        'mesaj',
        ('rezervasyon_tarihi', 'ucret'),
        'basvuru_tarihi', 'mail_gonderildi'
    )
    readonly_fields = ('basvuru_tarihi',)


# Register your models here.
