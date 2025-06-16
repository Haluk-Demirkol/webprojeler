from django.db import models
from django.utils import timezone

class IptalBasvuru(models.Model):
    ad                = models.CharField(max_length=100)
    soyad             = models.CharField(max_length=100)
    telefon           = models.CharField(max_length=20)
    email             = models.EmailField()
    mesaj             = models.TextField(blank=True)

    rezervasyon_tarihi= models.DateTimeField(default=timezone.now, null=True, blank=True)
    ucret             = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    basvuru_tarihi    = models.DateTimeField(auto_now_add=True)
    mail_gonderildi   = models.BooleanField(default=False)   # ← e‑posta zaten gitmiş mi?

    def __str__(self):
        return f"{self.ad} {self.soyad} — {self.basvuru_tarihi.date()}"


