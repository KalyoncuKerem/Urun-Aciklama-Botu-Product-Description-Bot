import streamlit as st
import pandas as pd
import os
from src.config import (
    APP_TITLE,
    BRAND_PRIMARY_COLOR,
    BRAND_SECONDARY_COLOR,
    DEFAULT_SYSTEM_PROMPT,
    LOGO_PATH
)
from src.ui_components import (
    inject_custom_css,
    render_hero_header,
    render_stepper,
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

# 4. Hero Header & Süreç Göstergesi Render
render_hero_header()

current_step = 1
if st.session_state.get("df_processed") is not None and len(st.session_state["df_processed"]) > 0:
    current_step = 3
render_stepper(current_step=current_step)

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
    col_left, col_right = st.columns([1, 1], gap="medium")
    
    with col_left:
        st.markdown(f"""
        <div class="studio-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <strong style="color:{BRAND_PRIMARY_COLOR}; font-size:0.95rem;">📂 1. Excel Dosyası</strong>
                <span class="badge-tag">.xlsx / .xls</span>
            </div>
            <p style="color:#94A3B8; font-size:0.82rem; margin:0;">
                Ürün açıklamalarını içeren Excel dosyasını seçin.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader(
            "Excel Dosyası Seçin",
            type=["xlsx", "xls"],
            label_visibility="collapsed"
        )
        
        c_opt1, c_opt2 = st.columns([1, 1])
        with c_opt1:
            has_header = st.checkbox("Başlık Satırı Var", value=True, help="İlk satır başlık değil doğrudan ürün açıklaması ise işareti kaldırın.")
        with c_opt2:
            header_row = 0
            if has_header:
                header_row = st.number_input("Başlık İndeksi (0 = 1. Satır):", min_value=0, max_value=20, value=0)

    df_input = None
    with col_right:
        if uploaded_file is not None:
            try:
                df_input = ExcelProcessor.read_excel_file(uploaded_file, has_header=has_header, header_row=header_row)
                
                st.markdown(f"""
                <div class="studio-card">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                        <strong style="color:{BRAND_SECONDARY_COLOR}; font-size:0.95rem;">📋 2. Sütun Seçimi</strong>
                        <span class="badge-studio">{len(df_input)} Satır Bulundu</span>
                    </div>
                    <p style="color:#94A3B8; font-size:0.82rem; margin:0;">
                        Dönüştürülecek açıklama sütununu belirleyin.
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                default_col_idx = 0
                for idx, col in enumerate(df_input.columns):
                    if "aciklama" in str(col).lower() or "açıklama" in str(col).lower():
                        default_col_idx = idx
                        break
                        
                target_column = st.selectbox(
                    "Dönüştürülecek Açıklama Sütunu:",
                    df_input.columns,
                    index=default_col_idx,
                    label_visibility="collapsed"
                )
                
                if len(str(target_column)) > 35:
                    st.caption("💡 Seçilen sütun adı metne benziyor. Gerekirse 'Başlık Satırı Var' kutusunu kaldırın.")
                    
                st.dataframe(df_input.head(3), height=140, use_container_width=True)
            except Exception as e:
                st.error(f"Dosya işlenirken hata oluştu: {e}")
        else:
            st.markdown(f"""
            <div class="studio-card" style="height:100%; display:flex; flex-direction:column; justify-content:center;">
                <strong style="color:#FFFFFF; font-size:0.95rem; margin-bottom:8px; display:block;">ℹ️ Hızlı Başlangıç Rehberi</strong>
                <ul style="color:#94A3B8; font-size:0.82rem; line-height:1.6; padding-left:18px; margin:0;">
                    <li><strong>Sol Panelden</strong> Excel dosyanızı seçin veya sürükleyin.</li>
                    <li><strong>Sağ Panelde</strong> ürün metnini içeren sütunu doğrulayın.</li>
                    <li><strong>Aşağıdaki Butonla</strong> AI Tailwind HTML üretimini başlatın.</li>
                    <li>İşlem bitiminde <strong>Masaüstü & Mobil</strong> önizleme hazır olur.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

    if uploaded_file is not None and df_input is not None and not df_input.empty:
        st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
        c_act1, c_act2, c_act3 = st.columns([1, 2, 1])
        with c_act2:
            start_button = st.button("🚀 HTML Dönüştürmeyi Başlat", use_container_width=True)
            
        if start_button:
            if not st.session_state["api_key"] or not gemini_service or not selected_model:
                st.error("⚠️ Lütfen sol menüden geçerli bir API Anahtarı girin ve model seçin.")
            else:
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
                
                st.success("🎉 Tüm açıklamalar başarıyla dönüştürüldü! Lütfen yukarıdaki **'2. Canlı HTML Önizleme'** veya **'3. Sonuçlar & İndirme'** sekmesine geçin.")

# --- TAB 2: CANLI HTML ÖNİZLEME ---
with tab_preview:
    df_p = st.session_state.get("df_processed")
    if df_p is not None and isinstance(df_p, pd.DataFrame) and len(df_p) > 0:
        st.markdown("### 👁️ Canlı HTML Render & Kod Önizleme")
        st.write("İşlenmiş satırlardan birini seçerek üretilen Tailwind HTML'in gerçek web çıktısını inceleyin.")
        
        col_ctrl1, col_ctrl2 = st.columns([1, 1])
        with col_ctrl1:
            row_indices = [f"Satır {i+1}" for i in range(len(df_p))]
            selected_row_str = st.selectbox("İncelemek istediğiniz satırı seçin:", row_indices)
            selected_idx = int(selected_row_str.split(" ")[1]) - 1
            selected_html = str(df_p.iloc[selected_idx].get("Yeni_Aciklama_HTML", ""))
            
        with col_ctrl2:
            device_choice = st.radio(
                "Önizleme Cihaz Modu:",
                ["💻 Masaüstü Tarayıcı", "📱 Mobil E-Ticaret (375px)"],
                horizontal=True
            )
            device_mode = "mobile" if "Mobil" in device_choice else "desktop"
        
        col_code, col_view = st.columns([1, 1])
        
        with col_code:
            st.markdown("#### 📝 Ham HTML Kodu")
            st.code(selected_html, language="html")
            
        with col_view:
            st.markdown("#### 🎨 Gerçek E-Ticaret Canlı Render")
            render_tailwind_live_preview(selected_html, device_mode=device_mode, height=480)
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
