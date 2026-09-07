# 🚀 Ürün Açıklama Botu / Product Description Bot
### *Next-Gen E-Commerce Studio & Tailwind HTML Generator*

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%20%7C%203.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-1.63+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Google%20Gemini-Flash%20%2F%20Pro-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Gemini">
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.4+-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <b>🌐 Language / Dil Seçimi:</b><br>
  <a href="#-türkçe"><b>🇹🇷 Türkçe Dokümantasyon</b></a> | <a href="#-english"><b>🇬🇧 English Documentation</b></a>
</p>

---

<a name="-türkçe"></a>
## 🇹🇷 Türkçe

**Ürün Açıklama Botu**, e-ticaret siteleri ve pazaryerleri için karmaşık, dağınık ve teknik Excel ürün verilerini; SEO uyumlu, mobil duyarlı ve yüksek dönüşüm odaklı **Tailwind HTML** şablonlarına dönüştüren yapay zeka (Google Gemini API) destekli modern bir stüdyo uygulamasıdır.

Referans tasarım ilkeleri (**Design DNA**, **Taste-Skill / Anti-Slop**, **Scroll-Craft**) doğrultusunda inşa edilen arayüz; klişe, mor-neon yapay zeka şablonlarından tamamen arındırılarak profesyonel, mat arduvaz tonlarında ve ergonomik bir çalışma alanına kavuşturulmuştur.

---

### ✨ Öne Çıkan Özellikler

- 🎨 **Anti-Slop Modern Stüdyo Tasarımı:**
  - Generic yapay zeka parıltıları ve aşırı bulanık cam efektleri yerine; mat arduvaz zemin, katmanlı derinlik ve ince 1px kenarlıklar.
  - Marka Kimliği Renkleri: `#ff9610` (Sıcak Kehribar/Turuncu aksiyon rengi) ve `#009cf3` (Elektrik Gök Mavisi odak rengi).
  - 14px - 22px kavisli yumuşak (squircle) hatlar ve dokunsal yaylanma efektli butonlar.

- 📐 **Kompakt ve 50 / 50 Simetrik Mimari:**
  - Geniş ekranlarda taşmayı önleyen merkezlenmiş 1120px dengeli kabuk düzeni.
  - Sol tarafta dosya yükleme ve ayarlar, sağ tarafta anlık veri tablosu ve sütun seçimi sunan dengeli iki sütunlu mimari.
  - Ekrana eşit yayılan (`flex: 1`) 3 sekme yapısı.

- 📱💻 **İmza Deneyim: İki Cihazlı Canlı Önizleme Simülatörü:**
  - **Masaüstü Modu:** Mac tarzı renkli pencere kontrolleri ve adres çubuğu ile geniş ekran simülasyonu.
  - **Mobil E-Ticaret Modu (375px):** Özel akıllı telefon kasası, hoparlör çentiği ve kaydırılabilir ekran ile mobil alışveriş deneyimini anlık test etme imkanı.

- 🧭 **3 Adımlı Sezgisel Süreç Çubuğu (Stepper):**
  - `1. Excel Yükle & Sütun Seç` ➔ `2. AI HTML Dönüştürme` ➔ `3. Canlı Önizle & İndir` adımlarıyla anlık durum takibi.

- ⚡ **Toplu Excel İşleme & Hız Limiti Kontrolü:**
  - Yüzlerce satırlık ürün listesini tek tıklamayla dönüştürme.
  - Gemini API limit aşımlarını (Rate Limit) engellemek için istekler arası bekleme süresi (slider) ayarı.

- 🔔 **Çift Kanallı Bildirim Sistemi:**
  - Uzun süren dönüştürme işlemleri bittiğinde yerel Windows masaüstü bildirimi ve HTML5 tarayıcı bildirimi alma.

- 📥 **Tek Tıkla Excel Dışa Aktarma:**
  - Üretilen tüm yeni açıklamaları orijinal verilerle birleştirerek doğrudan `.xlsx` formatında indirme.

---

### 📁 Proje Dosya Mimarisi

```text
Urun-Aciklama-Botu-Product-Description-Bot/
├── README.md                       # Proje Ana Dokümantasyonu (TR/EN)
└── UrunAciklamaBotu_Public/
    ├── app.py                      # Streamlit Ana Uygulama & Sekme Düzeni
    ├── requirements.txt            # Python Paket Bağımlılıkları
    ├── .streamlit/
    │   └── config.toml             # Minimalist tema ve toolbar gizleme ayarları
    ├── assets/
    │   └── UAB.png                 # Stüdyo Logo ve Görselleri
    └── src/
        ├── __init__.py             # Modül başlatıcı
        ├── config.py               # Marka renkleri, sabitler ve varsayılan prompt
        ├── excel_processor.py      # Excel okuma, toplu işleme ve dışa aktarım
        ├── gemini_service.py       # Google Gemini API modeli ve istemci katmanı
        ├── ui_components.py        # Anti-slop CSS motoru, stepper, cihaz simülatörü
        └── utils.py                # Masaüstü bildirim entegrasyonu
```

---

### 🛠️ Kurulum ve Çalıştırma Rehberi

#### 1. Gereksinimler
- Python 3.10 veya üzeri (Python 3.12 önerilir)
- Aktif bir [Google AI Studio](https://aistudio.google.com/) Gemini API Anahtarı

#### 2. Depoyu Klonlayın
```bash
git clone https://github.com/KalyoncuKerem/Urun-Aciklama-Botu-Product-Description-Bot.git
cd Urun-Aciklama-Botu-Product-Description-Bot/UrunAciklamaBotu_Public
```

#### 3. Sanal Ortam Oluşturun (Önerilen)
```bash
# Sanal ortamı kur
python -m venv .venv

# Windows üzerinde aktif et:
.venv\Scripts\activate

# Linux / macOS üzerinde aktif et:
source .venv/bin/activate
```

#### 4. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

#### 5. Uygulamayı Başlatın
```bash
streamlit run app.py
```
Uygulama otomatik olarak tarayıcınızda açılacaktır: **`http://localhost:8501`**

---

### 📖 Adım Adım Kullanım

1. **API Anahtarı Girişi:** Sol menüden Gemini API anahtarınızı girin. Modeller otomatik listelenecektir (Örn: `gemini-1.5-flash` veya `gemini-2.0-flash`).
2. **Dosya Yükleme (Tab 1):** Sol alandan `.xlsx` dosyanızı yükleyin. Sağ panelde verinizi kontrol edip dönüştürülecek açıklama sütununu seçin.
3. **Dönüştürmeyi Başlat:** `🚀 HTML Dönüştürmeyi Başlat` butonuna basın. İlerleme çubuğu anlık olarak her ürünü işleyecektir.
4. **Canlı Önizleme (Tab 2):** Üretilen Tailwind HTML kodlarını satır bazlı seçerek hem ham kod hem de **Masaüstü / Mobil** simülatöründe inceleyin.
5. **Dışa Aktarma (Tab 3):** İstatistik kartlarını kontrol edin ve `📥 Dönüştürülmüş Excel Dosyasını İndir` butonuna tıklayarak dosyanızı alın.

---

### 💡 Özel Prompt Mühendisliği Rehberi

Uygulamanın varsayılan promptu genel e-ticaret siteleri için optimize edilmiştir. Özel şablonlar tanımlamak için sol menüdeki **🛠️ Gelişmiş Prompt Şablonu** alanını veya `src/config.py` dosyasını kullanabilirsiniz.

> ⚠️ **Kritik Kural:** Kendi özel şablonunuzu yazarken ham metnin yapay zekaya aktarılacağı yere mutlaka **`{original_text}`** etiketini ekleyin!

---
---

<a name="-english"></a>
## 🇬🇧 English

**Product Description Bot** is a high-taste, AI-powered **Streamlit** studio application designed for e-commerce stores, marketplaces, and catalog managers. It automatically transforms raw, unformatted, technical product specs from Excel into clean, SEO-optimized, and responsive **Tailwind HTML** product descriptions using the Google Gemini API.

Built on principles from **Design DNA**, **Taste-Skill (Anti-Slop)**, and **Scroll-Craft**, this tool eliminates generic, neon-glowing "AI slop" in favor of a focused, matte obsidian studio experience.

---

### ✨ Key Features

- 🎨 **Anti-Slop Bespoke Studio Design:**
  - Clean obsidian slate background (`#0B0F17`), structured surface layering, and crisp 1px borders.
  - Identity Colors: `#ff9610` (Warm Tangerine/Amber) and `#009cf3` (Electric Sky Blue).
  - Tactile squircle buttons with spring press feedback and 14-22px soft corner radii.

- 📐 **Compact & Symmetrical 50 / 50 Layout:**
  - Centered 1120px max-width shell prevents content from over-stretching on ultra-wide screens.
  - Symmetrical 2-column input & preview architecture on Tab 1.
  - Equal-width (`flex: 1`) clean tab navigation.

- 📱💻 **Dual Device Live Simulator:**
  - **Desktop Mode:** Clean browser window chrome with macOS-style window controls.
  - **Mobile Mode (375px):** Realistic smartphone chassis with speaker notch and scrollable viewport for testing mobile shopper readability.

- 🧭 **3-Step Dynamic Stepper:**
  - Real-time step progress tracker: `1. Upload & Select` ➔ `2. AI Conversion` ➔ `3. Preview & Download`.

- ⚡ **Batch Excel Processing & Rate Limit Safeguard:**
  - Convert hundreds of product descriptions in one run.
  - Configurable request delay slider to prevent Gemini API quota / rate limit errors.

- 🔔 **Dual Desktop & Browser Notifications:**
  - Sound & visual notifications on Windows desktop and HTML5 browser API upon completion.

- 📥 **One-Click Excel Export:**
  - Download transformed results combined with original catalog data directly as `.xlsx`.

---

### 🛠️ Quick Installation

```bash
# 1. Clone repository
git clone https://github.com/KalyoncuKerem/Urun-Aciklama-Botu-Product-Description-Bot.git
cd Urun-Aciklama-Botu-Product-Description-Bot/UrunAciklamaBotu_Public

# 2. Setup virtual environment
python -m venv .venv
# Activate: Windows: .venv\Scripts\activate | Mac/Linux: source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run application
streamlit run app.py
```

Access the live interface at: **`http://localhost:8501`**

---

### 📄 License

Distributed under the **MIT License**. Feel free to use, modify, and integrate into your e-commerce workflows.
