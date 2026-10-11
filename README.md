import time

def matnni_shifrlash(matn, kalit):
    shifrlangan_matn = ""
    for harf in matn:
        # Har bir harfning matematik kodini maxfiy kalitga qarab suramiz
        shifrlangan_matn += chr(ord(harf) + kalit)
    return shifrlangan_matn

def shifrni_ochish(shifrlangan_matn, kalit):
    asliy_matn = ""
    for harf in shifrlangan_matn:
        asliy_matn += chr(ord(harf) - kalit)
    return asliy_matn

def dastur():
    print("=" * 60)
    print("          CRYPTOLULF AI v1.5 [MUKAMMAL]          ")
    print("   Ma'lumotlarni Shifrlash va Deshifrlash Tizimi   ")
    print("=" * 60)
    
    # Onlayn brauzerda xato bermasligi uchun foydalanuvchidan 
    # kerakli ma'lumotlarni ketma-ketlikda so'raymiz
    print("\n[ QADAM-1 ] Shifrlash uchun maxfiy kalit so'z (Raqam kiriting, masalan: 5):")
    try:
        kalit = int(input("Kalit raqam >>> "))
    except ValueError:
        print("Xatolik! Faqat raqam kiritishingiz kerak edi. Kalit avtomatik 7 deb olindi.")
        kalit = 7

    print("\n[ QADAM-2 ] Himoya qilmoqchi bo'lgan maxfiy matningizni kiriting:")
    asliy_matn = input("Matn >>> ")

    print("\n[AI] Ma'lumot shifrlanmoqda...")
    time.sleep(1)

    # 1. Shifrlash jarayoni
    shifrlangan_natija = matnni_shifrlash(asliy_matn, kalit)
    
    print("\n" + "=" * 60)
    print("🔏 SHIFRLANGAN MATN (Buni xakerlar o'qiy olmaydi):")
    print(f"👉 {shifrlangan_natija}")
    print("=" * 60)
    
    time.sleep(1.5)
    print("\n[ QADAM-3 ] Endi ushbu shifrni ochish (deshifrlash) uchun parolni qayta kiriting:")
    tekshiruv_kaliti = int(input("Parol raqam >>> "))

    print("\n[AI] Shifr tekshirilmoqda va ochilmoqda...")
    time.sleep(1)

    # 2. Deshifrlash jarayoni (Tekshirish)
    if tekshiruv_kaliti == kalit:
        ochilgan_matn = shifrni_ochish(shifrlangan_natija, tekshiruv_kaliti)
        print("\n" + "=" * 60)
        print("🔓 SHIFR MUVAFAQQIYATLI OCHILDI (Asliy holati):")
        print(f"👉 '{ochilgan_matn}'")
        print("=" * 60)
    else:
        print("\n" + "❌" * 20)
        print("XATOLIK: Maxfiy parol noto'g'ri! Shifr ochilmadi.")
        print("❌" * 20)

if __name__ == "__main__":
    dastur()
