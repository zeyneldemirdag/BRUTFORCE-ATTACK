# Basit giriş sistemi

# Doğru şifre
real_password = "123"

# Kullanıcıdan şifre iste
entered_password = input("Şifrenizi girin: ")

if entered_password == real_password:
    print("✅ Giriş başarılı!")
else:
    print("❌ Şifre yanlış!")