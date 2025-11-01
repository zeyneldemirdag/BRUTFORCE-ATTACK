import pyautogui
import time

time.sleep(5)

def ultra_hizli_brute_force():
    print("⚡ ULTRA HIZLI Brute Force başlatıldı...")
    
    # PyAutoGUI güvenlik önlemini kaldır (DİKKAT!)
    pyautogui.FAILSAFE = False
    
    for i in range(10000):  # 0000 ile 9999 arası
        tahmin = f"{i:04d}"  # En hızlı 4 haneli yapma yöntemi
        
        # Ekrana yazdırmayı minimize et (çok yavaşlatır)
        if i % 1000 == 0:  # Sadece her 1000'de bir göster
            print(f"🚀 {i}/10000 deneme yapıldı
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  lölşlöşölşölş")
        
        # ÇOK HIZLI yazma (interval=0)
        pyautogui.write(tahmin, interval=0)
        pyautogui.press('enter')
        
        # Neredeyse hiç bekleme
        time.sleep(0.001)
        
        # Backspace yerine direkt yeni yazma (daha hızlı)
        # Temizleme yapmadan direkt üstüne yazıyoruz
        
    print("✅ 10000 deneme tamamlandı!")

ultra_hizli_brute_force()