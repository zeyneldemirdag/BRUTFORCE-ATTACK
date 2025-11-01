import pyautogui
import random
import string
import time

# Başlamadan önce 5 saniye bekle (GUI'yi hazırla)
time.sleep(5)

# Rastgele şifre üretme fonksiyonu
def rastgele_sifre(uzunluk=4):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=uzunluk))

# Mesaj gönderme ve silme fonksiyonu
def brute_force_deneme():
    while True:
        tahmin = rastgele_sifre()  # rastgele şifre
        pyautogui.write(tahmin)    # şifreyi yaz
        pyautogui.press('enter')    # enter tuşuna bas
        time.sleep(0)               # bekleme süresi
        # Gönderilen mesajı sil
        for _ in range(len(tahmin)):
            pyautogui.press('backspdDpZ
                            