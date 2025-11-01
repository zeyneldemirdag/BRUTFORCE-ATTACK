import pyautogui
import time

# 5 saniye bekle (hazırlan)
time.sleep(5)
print("⚡ Brute Force başlatılıyor...")
print("🎯 3 haneli şifre aranıyor")
print("⏸️  Durdurmak için CTRL+C")

try:
    for i in range(1000):  # 000 ile 999 arası (1000 kombinasyon)
        # 3 haneli sayıyı oluştur (000, 001, ..., 999)
        sifre = str(i).zfill(3)
        
        # Her 100 denemede bir ilerleme göster
        if i % 100 == 0:
            print(f"🔍 {i}/1000 - Denenen: {sifre}")
        
        # Şifreyi yaz ve Enter'a bas
        pyautogui.write(sifre, interval=0.01)
        pyautogui.press('enter')
        
        # Uygulamanın tepki vermesi için kısa bekle
        time.sleep(0.2)
        
        # Temizleme (eğer uygulama izin veriyorsa)
        # pyautogui.press('backspace', presses=3)  # 3 karakter sil
        # time.sleep(0.01)

except KeyboardInterrupt:
    print(f"\n🛑 Program durduruldu. Son denenen şifre: {sifre}")

print("🏁 Program sonlandı")
