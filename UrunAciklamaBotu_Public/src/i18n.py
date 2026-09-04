"""
Çoklu Dil (TR / EN) Desteği ve Çeviri Sözlüğü
"""

TRANSLATIONS = {
    "TR": {
        "app_title": "Ürün Açıklama Dönüştürücü",
        "app_subtitle": "E-ticaret ürün teknik detaylarını SEO uyumlu, estetik Tailwind HTML şablonlarına çevirin.",
        "badge": "v2.0 Glass Edition",
        
        # Sidebar
        "sidebar_settings": "⚙️ Uygulama Ayarları",
        "api_key_label": "Google Gemini API Anahtarı:",
        "api_key_help": "Google AI Studio'dan aldığınız API anahtarını buraya girin.",
        "api_success": "✅ API Bağlantısı Başarılı",
        "api_no_models": "❌ Bu API anahtarıyla uyumlu model bulunamadı.",
        "api_enter_key": "💡 Lütfen devam etmek için API anahtarınızı girin.",
        "model_label": "Kullanılacak AI Modeli:",
        "advanced_prompt_title": "🛠️ Gelişmiş Prompt Şablonu",
        "prompt_label": "Tailwind HTML Prompt Şablonu:",
        "delay_label": "İstekler Arası Bekleme (Saniye):",
        "delay_help": "Gemini API limit aşımını (Rate Limit) engellemek için bekleme süresi.",
        
        # Tabs
        "tab_upload": "📂 1. Dosya Yükleme & İşlem",
        "tab_preview": "👁️ 2. Canlı HTML Önizleme",
        "tab_download": "📊 3. Sonuçlar & İndirme",
        
        # Tab 1
        "upload_card_title": "1. Excel Dosyanızı Yükleyin",
        "upload_card_desc": "Dönüştürmek istediğiniz ürün teknik açıklamalarını içeren Excel (.xlsx, .xls) dosyasını yükleyin.",
        "file_uploader_label": "Excel Dosyası Seçin",
        "has_header_label": "Dosyada Başlık Satırı Var",
        "has_header_help": "Eğer dosyanızın ilk satırı başlık değil doğrudan ürün açıklaması ise bu işareti kaldırın.",
        "header_row_label": "Başlık Satır İndeksi (0 = 1. Satır):",
        "file_loaded_success": "📁 Dosya başarıyla yüklendi! Toplam {total} satır tespit edildi.",
        "target_col_label": "Dönüştürülecek Açıklama Sütunu:",
        "long_header_tip": "💡 **İpucu:** Seçtiğiniz sütun adı uzun bir açıklama metnine benziyor. Eğer Excel dosyanızın en üst satırı başlık değil doğrudan 1. ürün açıklamasıysa, sağ üstteki **'Dosyada Başlık Satırı Var'** kutucuğundaki işareti kaldırın.",
        "start_button": "🚀 HTML Dönüştürmeyi Başlat",
        "preview_header": "Veri Önizlemesi (İlk 3 Satır):",
        "err_no_api": "⚠️ Lütfen sol menüden geçerli bir API Anahtarı girin ve model seçin.",
        "err_empty_df": "⚠️ Yüklenen dosyada dönüştürülecek satır bulunamadı!",
        "processing_title": "⏳ İşlem Yürütülüyor...",
        "spinner_text": "Yapay Zeka ürün açıklamalarını Tailwind HTML kodlarına dönüştürüyor...",
        "process_status": "İşleniyor ({current}/{total}):",
        "notify_msg": "🎉 {total} üründen {success} adedi başarıyla HTML'e dönüştürüldü!",
        "success_msg": "🎉 Tüm açıklamalar başarıyla dönüştürüldü! Bilgisayarınıza bildirim gönderildi. Lütfen yukarıdaki **'2. Canlı HTML Önizleme'** veya **'3. Sonuçlar & İndirme'** sekmesine geçin.",
        "upload_info": "📌 Başlamak için yukarıdaki alandan bir Excel dosyası yükleyin.",
        
        # Tab 2
        "preview_title": "👁️ Canlı HTML Render & Kod Önizleme",
        "preview_sub": "İşlenmiş satırlardan birini seçerek üretilen Tailwind HTML'in gerçek web çıktısını inceleyin.",
        "select_row": "İncelemek istediğiniz satırı seçin:",
        "row_prefix": "Satır",
        "raw_code_title": "📝 Ham HTML Kodu",
        "live_render_title": "🎨 Gerçek E-Ticaret Canlı Render",
        "preview_info": "📌 Önizleme yapabilmek için 1. Sekmeden bir Excel dosyası yükleyip dönüştürme işlemini başlatın.",
        
        # Tab 3
        "download_title": "📊 İşlem İstatistikleri ve Dışa Aktarma",
        "metric_total": "Toplam Satır",
        "metric_processed": "İşlenen",
        "metric_success": "Başarılı",
        "metric_error": "Hata",
        "summary_table_title": "📋 Dönüştürülmüş Veri Özeti",
        "download_btn": "📥 Dönüştürülmüş Excel Dosyasını İndir (.xlsx)",
        "download_info": "📌 Henüz indirilecek dönüştürülmüş veri bulunmamaktadır."
    },
    "EN": {
        "app_title": "Product Description Converter",
        "app_subtitle": "Transform complex e-commerce product technical specs into SEO-friendly, modern Tailwind HTML snippets.",
        "badge": "v2.0 Glass Edition",
        
        # Sidebar
        "sidebar_settings": "⚙️ App Settings",
        "api_key_label": "Google Gemini API Key:",
        "api_key_help": "Enter your Google AI Studio API key here.",
        "api_success": "✅ API Connection Successful",
        "api_no_models": "❌ No compatible models found with this API key.",
        "api_enter_key": "💡 Please enter your API key to continue.",
        "model_label": "Select AI Model:",
        "advanced_prompt_title": "🛠️ Advanced Prompt Template",
        "prompt_label": "Tailwind HTML Prompt Template:",
        "delay_label": "Delay Between Requests (Seconds):",
        "delay_help": "Optional pause between API calls to prevent Rate Limit errors.",
        
        # Tabs
        "tab_upload": "📂 1. Upload File & Process",
        "tab_preview": "👁️ 2. Live HTML Preview",
        "tab_download": "📊 3. Results & Download",
        
        # Tab 1
        "upload_card_title": "1. Upload Your Excel File",
        "upload_card_desc": "Upload the Excel (.xlsx, .xls) file containing raw product technical descriptions.",
        "file_uploader_label": "Choose Excel File",
        "has_header_label": "File Has Header Row",
        "has_header_help": "Uncheck this if the first row of your Excel file is a product description rather than a column name.",
        "header_row_label": "Header Row Index (0 = Row 1):",
        "file_loaded_success": "📁 File uploaded successfully! Detected {total} rows.",
        "target_col_label": "Select Column to Convert:",
        "long_header_tip": "💡 **Tip:** The selected column name looks like a long text. If your first row is a product description instead of a header name, uncheck **'File Has Header Row'** at the top right.",
        "start_button": "🚀 Start HTML Conversion",
        "preview_header": "Data Preview (First 3 Rows):",
        "err_no_api": "⚠️ Please enter a valid API key and select a model in the left menu.",
        "err_empty_df": "⚠️ No rows found to convert in the uploaded file!",
        "processing_title": "⏳ Processing Items...",
        "spinner_text": "AI is converting product descriptions into Tailwind HTML code...",
        "process_status": "Processing ({current}/{total}):",
        "notify_msg": "🎉 {success} of {total} products successfully converted to HTML!",
        "success_msg": "🎉 All descriptions successfully converted! Desktop notification sent. Please switch to **'2. Live HTML Preview'** or **'3. Results & Download'** tab above.",
        "upload_info": "📌 Upload an Excel file above to get started.",
        
        # Tab 2
        "preview_title": "👁️ Live HTML Render & Code Preview",
        "preview_sub": "Select any processed row to see how the generated Tailwind HTML visually renders in real-time.",
        "select_row": "Select a row to inspect:",
        "row_prefix": "Row",
        "raw_code_title": "📝 Raw HTML Code",
        "live_render_title": "🎨 Real E-Commerce Live Render",
        "preview_info": "📌 Please upload an Excel file and start conversion in Tab 1 to see preview.",
        
        # Tab 3
        "download_title": "📊 Execution Metrics & Export",
        "metric_total": "Total Rows",
        "metric_processed": "Processed",
        "metric_success": "Successful",
        "metric_error": "Errors",
        "summary_table_title": "📋 Converted Data Summary",
        "download_btn": "📥 Download Converted Excel File (.xlsx)",
        "download_info": "📌 No converted data available to download yet."
    }
}

def get_text(key: str, lang: str = "TR", **kwargs) -> str:
    """Belirtilen anahtara göre seçili dildeki metni döndürür."""
    text_dict = TRANSLATIONS.get(lang, TRANSLATIONS["TR"])
    text = text_dict.get(key, TRANSLATIONS["TR"].get(key, key))
    if kwargs:
        return text.format(**kwargs)
    return text
