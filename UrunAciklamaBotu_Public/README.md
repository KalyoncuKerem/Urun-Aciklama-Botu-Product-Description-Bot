# 🚀 Ürün Açıklama Botu / Product Description Bot (Open-Source Edition)

<p align="center">
  <b>🌐 Language / Dil:</b><br>
  <a href="#-türkçe"><b>🇹🇷 Türkçe</b></a> | <a href="#-english"><b>🇬🇧 English</b></a>
</p>

---

<a name="-türkçe"></a>
## 🇹🇷 Türkçe

Bu proje, e-ticaret siteleri için karmaşık ve ham ürün teknik özelliklerini SEO uyumlu, estetik **Tailwind HTML** kodlarına dönüştüren yapay zeka (Google Gemini API) destekli bir **Streamlit** web uygulamasıdır.

### 🌟 Öne Çıkan Özellikler

- 🎨 **Glassmorphism Dark SaaS UI**: Modern dark mode, cam efekti ve estetik SaaS arayüz tasarımı.
- ⚡ **Toplu Excel Dönüştürme**: Excel dosyanızı yükleyerek tüm ürün açıklamalarını tek seferde HTML formatına dönüştürün.
- 👁️ **Canlı HTML Visual Preview**: Üretilen Tailwind HTML kodunun Tailwind CDN entegrasyonu ile e-ticaret görünümünde anlık olarak canlı izlenmesi ve test edilmesi.
- 🤖 **Dinamik Gemini Model Seçimi**: API anahtarınız ile kullanılabilir Gemini modellerini (Flash, Pro vb.) otomatik listeleme ve seçim olanağı.
- ⚙️ **Esnek Rate-Limit & Bekleme Ayarı**: API istekleri arasında bekleme süresi (slider) ayarlayarak Rate Limit aşımlarını engelleme.
- 🔔 **Masaüstü & Tarayıcı Bildirimleri**: İşlem tamamlandığında anında bilgisayar (Windows) ve tarayıcı bildirimi alma.
- 📌 **Gelişmiş Excel Esnekliği**: Başlık satırı olan veya olmayan Excel dosyalarını otomatik okuma, canlı ilerleme çubuğu ve kolay dışa aktarım (.xlsx).

---

### 🔒 Gizlilik ve Özel Prompt Yapılandırması

Bu açık kaynaklı repo özel/ticari prompt içeriklerini barındırmaz. Kendi e-ticaret şablonunuza özel prompt tanımlamak için:

1. Uygulamayı çalıştırdıktan sonra sol menüdeki **"🛠️ Gelişmiş Prompt Şablonu"** alanından prompt'unuzu anlık olarak düzenleyebilirsiniz.
2. Veya varsayılan şablonu kalıcı olarak değiştirmek için `src/config.py` dosyasındaki `DEFAULT_SYSTEM_PROMPT` değişkenini güncelleyebilirsiniz.

> ⚠️ **Önemli Not:** Kendi özel prompt şablonunuzu yazarken ham metnin geleceği yere mutlaka `{original_text}` etiketini eklemeyi unutmayın!

---

### 📁 Proje Dosya Yapısı

```text
UrunAciklamaBotu_Public/
├── .env.example                # Çevre değişkeni şablonu
├── .gitignore                  # Git yoksayma kuralları
├── README.md                   # Türkçe & İngilizce Proje Dokümantasyonu
├── requirements.txt            # Python bağımlılıkları
├── app.py                      # Ana Streamlit uygulama dosyası
├── .streamlit/
│   └── config.toml             # Koyu tema ve sunucu yapılandırması
├── assets/                     # Görsel ve logo varlıkları
│   └── UAB.png
└── src/                        # Modüler Python paketi
    ├── __init__.py
    ├── config.py               # Uygulama sabitleri ve varsayılan prompt şablonu
    ├── excel_processor.py      # Excel okuma, dönüştürme ve dışa aktarım
    ├── gemini_service.py       # Google Gemini API entegrasyonu
    ├── ui_components.py        # Glassmorphic CSS ve canlı HTML render iframe
    └── utils.py                # Masaüstü bildirim araçları
```

---

### 🛠️ Kurulum ve Çalıştırma

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
   
   # Linux / macOS için:
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

---

### 💡 Kullanım Adımları

1. Sol yan menüden **Google Gemini API Anahtarınızı** girin.
2. Açılan listeden kullanmak istediğiniz **Gemini Modelini** seçin.
3. **1. Dosya Yükleme & İşlem** sekmesinden Excel dosyanızı (.xlsx, .xls) yükleyin ve dönüştürülecek sütunu seçin.
4. **🚀 HTML Dönüştürmeyi Başlat** butonuna tıklayın.
5. İşlem bittiğinde bildirim alacaksınız; **2. Canlı HTML Önizleme** sekmesinden tasarımı canlı render olarak inceleyebilir, **3. Sonuçlar & İndirme** sekmesinden Excel dosyanızı indirebilirsiniz.

---
---

<a name="-english"></a>
## 🇬🇧 English

This project is an AI-powered (Google Gemini API) **Streamlit** web application designed to transform raw, complex product specifications into SEO-friendly, beautifully formatted **Tailwind HTML** components for e-commerce platforms.

### 🌟 Key Features

- 🎨 **Glassmorphism Dark SaaS UI**: Modern dark theme with sleek glassmorphic components and an aesthetic interface design.
- ⚡ **Bulk Excel Processing**: Upload an Excel file containing product descriptions and convert them all to HTML at once.
- 👁️ **Live HTML Visual Preview**: Real-time rendering of generated Tailwind HTML code inside an interactive iframe with Tailwind CDN support.
- 🤖 **Dynamic Gemini Model Selection**: Automatic discovery and selection of supported Gemini models (Flash, Pro, etc.) based on your API key.
- ⚙️ **Flexible Rate-Limit Control**: Configurable delay slider between API requests to avoid API rate limits.
- 🔔 **Desktop & Browser Notifications**: Instant notifications sent to your desktop (Windows) and browser upon batch completion.
- 📌 **Smart Excel Handler**: Supports Excel files with or without headers, provides live progress bars, and enables easy export to Excel (.xlsx).

---

### 🔒 Privacy & Custom Prompt Configuration

This open-source repository does not include proprietary or commercial prompt templates. To set up your custom prompt:

1. Edit your prompt on-the-fly via the sidebar section **"🛠️ Gelişmiş Prompt Şablonu" (Advanced Prompt Template)** after launching the application.
2. Or permanently update the `DEFAULT_SYSTEM_PROMPT` variable in `src/config.py`.

> ⚠️ **Important Note:** When writing your custom prompt template, ensure you include the `{original_text}` placeholder where the raw product text will be injected!

---

### 📁 Project Structure

```text
UrunAciklamaBotu_Public/
├── .env.example                # Environment variable template
├── .gitignore                  # Git ignore rules
├── README.md                   # Turkish & English Project Documentation
├── requirements.txt            # Python dependencies
├── app.py                      # Main Streamlit application file
├── .streamlit/
│   └── config.toml             # Dark theme and server configuration
├── assets/                     # Image and logo assets
│   └── UAB.png
└── src/                        # Modular Python package
    ├── __init__.py
    ├── config.py               # App constants and default prompt template
    ├── excel_processor.py      # Excel parsing, processing, and export
    ├── gemini_service.py       # Google Gemini API integration
    ├── ui_components.py        # Glassmorphic CSS and live HTML preview iframe
    └── utils.py                # Desktop notification tools
```

---

### 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/username/UrunAciklamaBotu.git
   cd UrunAciklamaBotu
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   
   # On Windows:
   .\.venv\Scripts\activate
   
   # On Linux / macOS:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   streamlit run app.py
   ```

---

### 💡 How to Use

1. Enter your **Google Gemini API Key** in the sidebar.
2. Select your preferred **Gemini Model** from the dropdown list.
3. Under **1. Dosya Yükleme & İşlem (File Upload & Process)** tab, upload your Excel file (.xlsx, .xls) and select the column to transform.
4. Click **🚀 HTML Dönüştürmeyi Başlat (Start HTML Conversion)**.
5. You will receive a desktop notification upon completion. Inspect the live rendered output in **2. Canlı HTML Önizleme (Live Preview)** tab, or download the output file in **3. Sonuçlar & İndirme (Results & Download)** tab.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
