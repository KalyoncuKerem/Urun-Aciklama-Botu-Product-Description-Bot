import streamlit as st
import pandas as pd
import os
from src.config import (
    APP_TITLE,
    BRAND_PRIMARY_COLOR,
    DEFAULT_SYSTEM_PROMPT,
    LOGO_PATH
)
from src.ui_components import (
    inject_custom_css,
    render_hero_header,
    render_metric_cards,
    render_tailwind_live_preview,
    trigger_browser_notification
)
from src.gemini_service import GeminiService
from src.excel_processor import ExcelProcessor
from src.utils import send_desktop_notification

# 1. Sayfa Yapılandırması
st.set_page_config(
    page_title=f"{APP_TITLE} | Open-Source",
    page_icon=LOGO_PATH if os.path.exists(LOGO_PATH) else "🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Özel Glassmorphic CSS Entegrasyonu (Sidebar açma butonu görünürlüğü dahil)
inject_custom_css()

# 3. Session State Yönetimi
if "df_processed" not in st.session_state:
    st.session_state["df_processed"] = None
if "stats" not in st.session_state:
    st.session_state["stats"] = None
if "api_key" not in st.session_state:
    st.session_state["api_key"] = ""

# 4. Hero Header Render
render_hero_header()

# 5. Yan Menü (Sidebar) Ayarları
with st.sidebar:
    st.image(LOGO_PATH if os.path.exists(LOGO_PATH) else "", width=140)
    st.markdown("### ⚙️ Uygulama Ayarları")
    
    api_key_input = st.text_input(
        "Google Gemini API Anahtarı:",
        type="password",
        value=st.session_state["api_key"],
        help="Google AI Studio'dan aldığınız API anahtarını buraya girin.",
        autocomplete="off"
    )
    
    if api_key_input:
        st.session_state["api_key"] = api_key_input.strip()
    
    selected_model = None
    gemini_service = None
    
    if st.session_state["api_key"]:
        try:
            gemini_service = GeminiService(st.session_state["api_key"])
            available_models = gemini_service.get_available_models()
            
            if available_models:
                st.success("✅ API Bağlantısı Başarılı")
                
                default_idx = 0
                for idx, m in enumerate(available_models):
                    if "flash" in m.lower():
                        default_idx = idx
                        break
                        
                selected_model = st.selectbox(
                    "Kullanılacak AI Modeli:",
                    available_models,
                    index=default_idx
                )
            else:
                st.error("❌ Bu API anahtarıyla uyumlu model bulunamadı.")
        except Exception as e:
            st.error(f"❌ Bağlantı hatası: {e}")
    else:
        st.info("💡 Lütfen devam etmek için API anahtarınızı girin.")
        
    st.markdown("---")
    
    # Gelişmiş Ayarlar (Prompt ve Hız Ayarı)
    with st.expander("🛠️ Gelişmiş Prompt Şablonu", expanded=False):
        custom_prompt = st.text_area(
            "Tailwind HTML Prompt Şablonu:",
            value=DEFAULT_SYSTEM_PROMPT,
            height=280,
            help="{original_text} değişkenini değiştirmeyiniz."
        )
        
    delay_seconds = st.slider(
        "İstekler Arası Bekleme (Saniye):",
        min_value=0.5,
        max_value=3.0,
        value=1.2,
        step=0.1,
        help="Gemini API limit aşımını (Rate Limit) engellemek için bekleme süresi."
    )

# 6. Ana Sekme Mimarisi (Tabs)
tab_upload, tab_preview, tab_download = st.tabs([
    "📂 1. Dosya Yükleme & İşlem",
    "👁️ 2. Canlı HTML Önizleme",
    "📊 3. Sonuçlar & İndirme"
])

# --- TAB 1: DOSYA YÜKLEME VE İŞLEM ---
with tab_upload:
    st.markdown("""
    <div class="glass-card">
        <h3 style="margin-top:0; color:#E07B00;">1. Excel Dosyanızı Yükleyin</h3>
        <p style="color:#94A3B8; font-size:0.9rem;">
            Dönüştürmek istediğiniz ürün teknik açıklamalarını içeren Excel (.xlsx, .xls) dosyasını yükleyin.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_file, col_opts = st.columns([2, 1])
    
    with col_file:
        uploaded_file = st.file_uploader(
            "Excel Dosyası Seçin",
            type=["xlsx", "xls"],
            label_visibility="collapsed"
        )
        
    with col_opts:
        has_header = st.checkbox("Dosyada Başlık Satırı Var", value=True, help="Eğer dosyanızın ilk satırı başlık değil doğrudan ürün açıklaması ise bu işareti kaldırın.")
        header_row = 0
        if has_header:
            header_row = st.number_input("Başlık Satır İndeksi (0 = 1. Satır):", min_value=0, max_value=20, value=0)

    if uploaded_file is not None:
        try:
            df_input = ExcelProcessor.read_excel_file(uploaded_file, has_header=has_header, header_row=header_row)
            st.success(f"📁 Dosya başarıyla yüklendi! Toplam {len(df_input)} satır tespit edildi.")
            
            # Veri Önizlemesi ve Sütun Seçimi
            col_sel, col_prev = st.columns([1, 2])
            
            with col_sel:
                default_col_idx = 0
                for idx, col in enumerate(df_input.columns):
                    if "aciklama" in str(col).lower() or "açıklama" in str(col).lower():
                        default_col_idx = idx
                        break
                        
                target_column = st.selectbox(
                    "Dönüştürülecek Açıklama Sütunu:",
                    df_input.columns,
                    index=default_col_idx
                )
                
                if len(str(target_column)) > 35:
                    st.warning("💡 **İpucu:** Seçtiğiniz sütun adı uzun bir açıklama metnine benziyor. Eğer Excel dosyanızın en üst satırı başlık değil doğrudan 1. ürün açıklamasıysa, sağ üstteki **'Dosyada Başlık Satırı Var'** kutucuğundaki işareti kaldırın.")
                
                st.markdown("<br>", unsafe_allow_html=True)
                start_button = st.button("🚀 HTML Dönüştürmeyi Başlat", use_container_width=True)
                
            with col_prev:
                st.markdown("**Veri Önizlemesi (İlk 3 Satır):**")
                st.dataframe(df_input.head(3), use_container_width=True)
                
            # Dönüştürme İşlemi Başlatma
            if start_button:
                if not st.session_state["api_key"] or not gemini_service or not selected_model:
                    st.error("⚠️ Lütfen sol menüden geçerli bir API Anahtarı girin ve model seçin.")
                elif df_input.empty:
                    st.error("⚠️ Yüklenen dosyada dönüştürülecek satır bulunamadı!")
                else:
                    st.markdown("---")
                    st.markdown("### ⏳ İşlem Yürütülüyor...")
                    
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    def update_progress(pct, current, total, status_msg):
                        progress_bar.progress(pct)
                        status_text.markdown(f"**İşleniyor ({current}/{total}):** {status_msg}")
                        
                    with st.spinner("Yapay Zeka ürün açıklamalarını Tailwind HTML kodlarına dönüştürüyor..."):
                        df_result, stats = ExcelProcessor.process_dataframe(
                            df=df_input,
                            column_name=target_column,
                            gemini_service=gemini_service,
                            model_name=selected_model,
                            prompt_template=custom_prompt,
                            progress_callback=update_progress,
                            delay_seconds=delay_seconds
                        )
                        
                    st.session_state["df_processed"] = df_result
                    st.session_state["stats"] = stats
                    
                    notification_msg = f"🎉 {stats.get('total', 0)} üründen {stats.get('success', 0)} adedi başarıyla HTML'e dönüştürüldü!"
                    send_desktop_notification("Ürün Açıklama Botu", notification_msg)
                    trigger_browser_notification("Ürün Açıklama Botu", notification_msg)
                    
                    st.success("🎉 Tüm açıklamalar başarıyla dönüştürüldü! Bilgisayarınıza bildirim gönderildi. Lütfen yukarıdaki **'2. Canlı HTML Önizleme'** veya **'3. Sonuçlar & İndirme'** sekmesine geçin.")
                    
        except Exception as e:
            st.error(f"Dosya işlenirken hata oluştu: {e}")
    else:
        st.info("📌 Başlamak için yukarıdaki alandan bir Excel dosyası yükleyin.")

# --- TAB 2: CANLI HTML ÖNİZLEME ---
with tab_preview:
    df_p = st.session_state.get("df_processed")
    if df_p is not None and isinstance(df_p, pd.DataFrame) and len(df_p) > 0:
        st.markdown("### 👁️ Canlı HTML Render & Kod Önizleme")
        st.write("İşlenmiş satırlardan birini seçerek üretilen Tailwind HTML'in gerçek web çıktısını inceleyin.")
        
        row_indices = [f"Satır {i+1}" for i in range(len(df_p))]
        selected_row_str = st.selectbox("İncelemek istediğiniz satırı seçin:", row_indices)
        selected_idx = int(selected_row_str.split(" ")[1]) - 1
        
        selected_html = str(df_p.iloc[selected_idx].get("Yeni_Aciklama_HTML", ""))
        
        col_code, col_view = st.columns([1, 1])
        
        with col_code:
            st.markdown("#### 📝 Ham HTML Kodu")
            st.code(selected_html, language="html")
            
        with col_view:
            st.markdown("#### 🎨 Gerçek E-Ticaret Canlı Render")
            render_tailwind_live_preview(selected_html, height=480)
    else:
        st.info("📌 Önizleme yapabilmek için 1. Sekmeden bir Excel dosyası yükleyip dönüştürme işlemini başlatın.")

# --- TAB 3: SONUÇLAR VE İNDİRME ---
with tab_download:
    df_p = st.session_state.get("df_processed")
    stats = st.session_state.get("stats")
    
    if df_p is not None and isinstance(df_p, pd.DataFrame) and len(df_p) > 0:
        st.markdown("### 📊 İşlem İstatistikleri ve Dışa Aktarma")
        
        if stats:
            render_metric_cards(
                total_rows=stats.get("total", 0),
                processed_rows=stats.get("processed", 0),
                success_count=stats.get("success", 0),
                error_count=stats.get("error", 0)
            )
            
        st.markdown("#### 📋 Dönüştürülmüş Veri Özeti")
        st.dataframe(df_p, use_container_width=True)
        
        excel_data = ExcelProcessor.export_to_excel_bytes(df_p)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            label="📥 Dönüştürülmüş Excel Dosyasını İndir (.xlsx)",
            data=excel_data,
            file_name="Donusturulmus_Urunler_HTML.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )
    else:
        st.info("📌 Henüz indirilecek dönüştürülmüş veri bulunmamaktadır.")
