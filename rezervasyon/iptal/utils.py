from datetime import time

def hesapla_iade_durumu(basvuru_dt, rezervasyon_dt):
    if not rezervasyon_dt or not basvuru_dt:
        return "Gerekli bilgiler eksik."

    fark_gun = (rezervasyon_dt.date() - basvuru_dt.date()).days

    if fark_gun > 5:
        return "Tam iade yapılacaktır."
    elif fark_gun > 0:
        return "%20 kesinti ile iade yapılacaktır."
    elif fark_gun == 0:
        saat_kriteri = time(11, 0)
        if basvuru_dt.time() <= saat_kriteri:
            return "%20 kesinti ile iade yapılacaktır."
        else:
            return "Saat 11:00 sonrası başvuru yapıldığı için iade yapılamaz."
    else:
        return "Rezervasyon tarihi geçmiş, iade yapılamaz."
