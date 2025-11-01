import pyautogui
import time

# Başlamadan önce 10 saniye bekler (hazırlanman için)
time.sleep(10)

# Mesaj gönderme fonksiyonu
def mesaj(metin):
    pyautogui.write(metin)   # verilen metni yaz
    pyautogui.press('enter')   # enter tuşuna bas

# Sonsuz döngü ile sürekli mesaj gönder
while True:
    mesaj("RAHATSIZ ETME!!")  # "merhaba" yaz
    time.sleep(0)

