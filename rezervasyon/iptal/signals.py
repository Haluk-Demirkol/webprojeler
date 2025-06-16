# iptal/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import IptalBasvuru
from .utils import hesapla_iade_durumu

@receiver(post_save, sender=IptalBasvuru)
def gonder_iptal_bilgi_maili(sender, instance, created, **kwargs):
    # Yeni oluşturulmadıysa ve admin panelden rezervasyon_tarihi + ucret girildiyse
    if not created and instance.rezervasyon_tarihi and instance.ucret and not instance.mail_gonderildi:
        # iade durumu hesapla
        iade_durumu = hesapla_iade_durumu(
            instance.basvuru_tarihi,
            instance.rezervasyon_tarihi
        )

        # e-posta içeriği
        konu = "Rezervasyon İptal Durumunuz"
        mesaj = (
            f"Merhaba {instance.ad} {instance.soyad},\n\n"
            f"Rezervasyon Tarihi: {instance.rezervasyon_tarihi.strftime('%d.%m.%Y %H:%M')}\n"
            f"Ücret: {instance.ucret} ₺\n\n"
            f"İptal Talebinizin Sonucu:\n{iade_durumu}\n\n"
            "Saygılarımızla,\nRezervasyon Ekibi"
        )

        # e-posta gönder
        send_mail(
            konu,
            mesaj,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently=False,
        )

        # e-posta gönderildi bilgisi işaretle
        instance.mail_gonderildi = True
        instance.save(update_fields=["mail_gonderildi"])
