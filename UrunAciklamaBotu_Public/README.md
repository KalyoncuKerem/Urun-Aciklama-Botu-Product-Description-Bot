# 🚀 Ürün Açıklama Botu (Open-Source Edition v2.0)

Bu proje, e-ticaret siteleri için karmaşık ve ham ürün teknik özelliklerini SEO uyumlu, estetik **Tailwind HTML** kodlarına dönüştüren yapay zeka (Google Gemini API) destekli Streamlit uygulamasıdır.

---

## 🌟 Öne Çıkan Özellikler

- 🎨 **Glassmorphism Dark SaaS UI**: Modern koyu tema, saydam kartlar ve estetik responsive arayüz.
- 🌐 **Çoklu Dil Desteği (TR / EN)**: Ekranın sağ üst köşesindeki dil seçici ile **Türkçe** ve **İngilizce** arayüzler arasında anlık geçiş imkanı.
- 👁️ **Canlı HTML Visual Preview**: Üretilen Tailwind HTML kodunun Tailwind CDN entegrasyonu ile e-ticaret görünümünde anlık render edilmesi.
- 🔔 **Masaüstü & Tarayıcı Bildirimleri**: Dönüştürme tamamlandığında Windows masaüstü bildirimi.
- 📌 **Esnek Excel Okuma**: Başlık satırı olan veya olmayan Excel dosyalarını sorunsuz işleme ve akıllı sütun tespiti.

---

## 🔒 Gizlilik ve Özel Prompt Yapılandırması

Bu açık kaynaklı repo özel prompt içeriklerini barındırmaz. Kendi e-ticaret tasarımınıza özel prompt şablonunuzu tanımlamak için:

1. Uygulamayı çalıştırdıktan sonra sol menüdeki **"🛠️ Gelişmiş Prompt Şablonu"** (veya **"🛠️ Advanced Prompt Template"**) alanından prompt'unuzu anlık düzenleyebilirsiniz.
2. Veya varsayılan şablonu kalıcı olarak değiştirmek için `src/config.py` dosyasındaki `DEFAULT_SYSTEM_PROMPT` değişkenini güncelleyebilirsiniz.

> ⚠️ **Önemli Not:** Kendi özel prompt şablonunuzu yazarken ham metnin geleceği yere `{original_text}` etiketini eklemeyi unutmayın!

---

## 📁 Proje Dosya Yapısı

```
UrunAciklamaBotu_Public/
├── .gitignore                  # Git tarafından yoksayılacak hassas/geçici dosyalar
├── .env.example                # Çevre değişkeni örneği
├── README.md                   # Proje dokümantasyonu
├── requirements.txt            # Python bağımlılıkları
├── app.py                      # Ana Streamlit uygulama dosyası
├── .streamlit/
│   └── config.toml             # Koyu tema ve sunucu konfigürasyonu
├── assets/                     # Görsel ve logo varlıkları
│   └── UAB2.jpg
└── src/                        # Modüler Python paket mimarisi
    ├── __init__.py
    ├── config.py               # Uygulama sabitleri ve Genel Prompt Şablon Rehberi
    ├── i18n.py                 # Türkçe ve İngilizce dil çeviri sözlüğü
    ├── utils.py                # Regex ve masaüstü bildirim araçları
    ├── gemini_service.py       # Google Gemini API entegrasyonu
    ├── ui_components.py        # Glassmorphic CSS ve canlı HTML render iframe
    └── excel_processor.py      # Excel okuma, dönüştürme ve dışa aktarım
```

---

## 🛠️ Kurulum ve Çalıştırma

1. **Repoyu klonlayın:**
   ```bash
   git clone https://github.com/kullanici-adi/UrunAciklamaBotu.git
   cd UrunAciklamaBotu
   ```

2. **Sanal ortam oluşturun ve aktif edin:**
   ```bash
   python -m venv .venv
   # Windows için:
   .\.venv\Scripts\activate
   # Linux/macOS için:
   source .venv/bin/activate
   ```

3. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Uygulamayı çalıştırın:**
   ```bash
   streamlit run app.py
   ```
