# iptal/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .forms import IptalBasvuruForm
from .models import IptalBasvuru
from .utils import hesapla_iade_durumu

# iptal/views.py

def iptal_basvuru_formu(request):
    if request.method == 'POST':
        form = IptalBasvuruForm(request.POST)
        if form.is_valid():
            basvuru = form.save()
            return redirect('iptal:tesekkur', basvuru_id=basvuru.id)  # YÖNLENDİRME
    else:
        form = IptalBasvuruForm()
    return render(request, 'iptal/form.html', {'form': form})



def tesekkur(request, basvuru_id):
    basvuru = get_object_or_404(IptalBasvuru, id=basvuru_id)

    # Admin bilgileri girilmemişse bu şablona yönlendirilir
    if not basvuru.rezervasyon_tarihi or basvuru.ucret is None:
        return render(request, 'iptal/tesekkur_wait.html', {'basvuru': basvuru})

    # Aksi halde teşekkür sayfası + iade durumu
    iade_durumu = hesapla_iade_durumu(basvuru.basvuru_tarihi, basvuru.rezervasyon_tarihi)
    return render(request, 'iptal/tesekkur_simple.html', {
        'basvuru': basvuru,
        'iade_durumu': iade_durumu,
    })