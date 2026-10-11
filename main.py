import streamlit as st
import time

# Sahifa sozlamalari
st.set_page_config(page_title="CryptoQulf AI", page_icon="🔏", layout="centered")

def matnni_shifrlash(matn, kalit):
    shifrlangan_matn = ""
    for harf in matn:
        shifrlangan_matn += chr(ord(harf) + kalit)
    return shifrlangan_matn

def shifrni_ochish(shifrlangan_matn, kalit):
    asliy_matn = ""
    for harf in shifrlangan_matn:
        asliy_matn += chr(ord(harf) - kalit)
    return asliy_matn

# Sayt interfeysi
st.title("🔏 CryptoQulf AI v2.0")
st.subheader("Ixtirochilikka qadam tanlovi uchun maxsus veb-platforma")
st.write("Muhim hujjatlar va xatlarni xakerlardan himoya qilish tizimi.")

# Menyular (Veb sahifadagi vkladkalar)
tab1, tab2 = st.tabs(["🔒 Matnni Shifrlash", "🔓 Shifrni Ochish"])

with tab1:
    st.header("Matnni xavfsiz qulflash")
    asliy_matn = st.text_area("Himoya qilmoqchi bo'lgan maxfiy matningizni kiriting:", key="shifr_text")
    kalit = st.number_input("Maxfiy kalit raqami (Parol):", min_value=1, max_value=100, value=7, key="shifr_key")
    
    if st.button("🔒 Shifrlashni Boshlash"):
        if asliy_matn:
            with st.spinner("Sun'iy intellekt matnni shifrlamoqda..."):
                time.sleep(1)
                natija = matnni_shifrlash(asliy_matn, kalit)
                st.success("Fayl muvaffaqiyatli shifrandi!")
                st.code(natija, language="text")
                st.warning("Ushbu kodni nusxalab oling. Uni faqat sizning parolingiz bilan ochish mumkin!")
        else:
            st.error("Iltimos, matn kiriting!")

with tab2:
    st.header("Shifrlangan xatni qayta ochish")
    shifrlangan_matn = st.text_area("Shifrlangan kodni (g'alati belgilarni) bu yerga joylang:", key="deshifr_text")
    tekshiruv_kaliti = st.number_input("Maxfiy kalit raqami (Parol):", min_value=1, max_value=100, value=7, key="deshifr_key")
    
    if st.button("🔓 Shifrni Ochish"):
        if shifrlangan_matn:
            with st.spinner("Shifr tekshirilmoqda..."):
                time.sleep(1)
                ochilgan_matn = shifrni_ochish(shifrlangan_matn, tekshiruv_kaliti)
                st.success("Shifr muvaffaqiyatli ochildi! Asliy matn:")
                st.info(ochilgan_matn)
        else:
            st.error("Iltimos, shifrlangan kodni kiriting!")

