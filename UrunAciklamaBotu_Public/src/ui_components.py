"""
Modern Glassmorphism UI ve Visual Render Bileşenleri
"""
import streamlit as st
import streamlit.components.v1 as components
import os
import base64
from src.config import APP_TITLE, APP_SUBTITLE, LOGO_PATH

def load_image_as_base64(path: str) -> str:
    """Görsel dosyasını base64 formatına çevirir (HTML embed için)."""
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    return ""

def inject_custom_css():
    """
    Gelişmiş Glassmorphism Dark Mode CSS stillerini yükler.
    Sidebar kapatıldığında açma ikonunu görünür tutar.
    """
    custom_css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Streamlit varsayılan gereksiz menülerini gizleme */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    a.header-anchor, h1 a svg, h2 a svg, h3 a svg {display: none !important;}
    [data-testid="stElementToolbar"] {display: none !important; visibility: hidden !important;}

    /* Header Arka Planını Şeffaf Yap (İkonların Görünmesi İçin) */
    header[data-testid="stHeader"] {
        background: transparent !important;
        z-index: 99999 !important;
    }

    /* Sidebar Açma/Kapatma Butonunu DAİMA GÖRÜNÜR ve ŞIK Yap */
    [data-testid="stSidebarCollapseButton"], 
    button[aria-label="Expand sidebar"], 
    button[aria-label="Collapse sidebar"],
    [data-testid="collapsedControl"] {
        visibility: visible !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        color: #E07B00 !important;
        background: rgba(19, 28, 46, 0.85) !important;
        border: 1px solid rgba(224, 123, 0, 0.5) !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
        transition: all 0.2s ease !important;
        z-index: 100000 !important;
    }

    [data-testid="stSidebarCollapseButton"]:hover,
    [data-testid="collapsedControl"]:hover {
        background: #E07B00 !important;
        color: #FFFFFF !important;
        transform: scale(1.05);
    }

    /* Ana Arka Plan */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1a233d 0%, #0b0f19 70%) !important;
    }

    /* Glassmorphism Kartlar */
    .glass-card {
        background: rgba(19, 28, 46, 0.65);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 12px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* Hero Header */
    .hero-container {
        display: flex;
        align-items: center;
        gap: 20px;
        background: linear-gradient(135deg, rgba(224, 123, 0, 0.12) 0%, rgba(19, 28, 46, 0.7) 100%);
        border: 1px solid rgba(224, 123, 0, 0.25);
        border-radius: 20px;
        padding: 24px 30px;
        margin-bottom: 28px;
        backdrop-filter: blur(12px);
    }

    .hero-logo {
        width: 76px;
        height: 76px;
        object-fit: contain;
        filter: drop-shadow(0 4px 12px rgba(224, 123, 0, 0.3));
    }

    .hero-title-group h1 {
        font-size: 2.1rem !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #FFFFFF 0%, #E2E8F0 60%, #E07B00 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0 0 6px 0 !important;
        padding: 0 !important;
    }

    .hero-title-group p {
        color: #94A3B8;
        font-size: 0.95rem;
        margin: 0;
    }

    .badge-v2 {
        display: inline-block;
        background: linear-gradient(135deg, #E07B00 0%, #FF9E2C 100%);
        color: #FFFFFF;
        font-size: 0.72rem;
        font-weight: 700;
        padding: 3px 10px;
        border-radius: 20px;
        text-transform: uppercase;
        letter-spacing: 0.8px;
        margin-left: 10px;
        vertical-align: middle;
        box-shadow: 0 2px 10px rgba(224, 123, 0, 0.4);
    }

    /* Metric Cards */
    .metric-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
        gap: 16px;
        margin-bottom: 24px;
    }

    .metric-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 16px 20px;
        text-align: center;
    }

    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #E07B00;
        line-height: 1.2;
    }

    .metric-label {
        font-size: 0.82rem;
        color: #94A3B8;
        font-weight: 600;
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* Streamlit Buton Özelleştirme */
    .stButton > button {
        background: linear-gradient(135deg, #E07B00 0%, #C46B00 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 28px !important;
        box-shadow: 0 4px 16px rgba(224, 123, 0, 0.35) !important;
        transition: all 0.25s ease !important;
        width: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 22px rgba(224, 123, 0, 0.5) !important;
        background: linear-gradient(135deg, #FF8C00 0%, #E07B00 100%) !important;
    }

    /* Tab Stilleri */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(15, 23, 42, 0.6);
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    .stTabs [data-baseweb="tab"] {
        height: 44px;
        border-radius: 10px;
        color: #94A3B8;
        font-weight: 600;
        padding: 0 20px;
    }

    .stTabs [aria-selected="true"] {
        background: #E07B00 !important;
        color: #FFFFFF !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def render_hero_header():
    """Uygulama üst kısmındaki modern Glassmorphic Hero Banner'ı çizer."""
    logo_base64 = load_image_as_base64(LOGO_PATH)
    img_html = f'<img src="data:image/png;base64,{logo_base64}" class="hero-logo" alt="Logo">' if logo_base64 else ''

    header_html = f"""
    <div class="hero-container">
        {img_html}
        <div class="hero-title-group">
            <h1>{APP_TITLE} <span class="badge-v2">Open-Source</span></h1>
            <p>{APP_SUBTITLE}</p>
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def render_metric_cards(total_rows: int, processed_rows: int, success_count: int, error_count: int):
    """İşlem istatistiklerini kart şeklinde gösterir."""
    html_metrics = f"""
    <div class="metric-container">
        <div class="metric-card">
            <div class="metric-value">{total_rows}</div>
            <div class="metric-label">Toplam Satır</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: #38BDF8;">{processed_rows}</div>
            <div class="metric-label">İşlenen</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: #4ADE80;">{success_count}</div>
            <div class="metric-label">Başarılı</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: #F87171;">{error_count}</div>
            <div class="metric-label">Hata</div>
        </div>
    </div>
    """
    st.markdown(html_metrics, unsafe_allow_html=True)

def trigger_browser_notification(title: str, message: str):
    """Tarayıcı bildirim izni ister ve HTML5 Web Bildirimi gönderir."""
    js_code = f"""
    <script>
    if ("Notification" in window) {{
        if (Notification.permission === "granted") {{
            new Notification("{title}", {{ body: "{message}", icon: "https://cdn-icons-png.flaticon.com/512/190/190411.png" }});
        }} else if (Notification.permission !== "denied") {{
            Notification.requestPermission().then(function (permission) {{
                if (permission === "granted") {{
                    new Notification("{title}", {{ body: "{message}", icon: "https://cdn-icons-png.flaticon.com/512/190/190411.png" }});
                }}
            }});
        }}
    }}
    </script>
    """
    components.html(js_code, height=0, width=0)

def render_tailwind_live_preview(html_content: str, height: int = 420):
    """
    Üretilen Tailwind HTML içeriğini Tailwind CDN ile güvenli bir iframe içerisinde
    gerçek e-ticaret görünümünde render eder.
    """
    if not html_content or html_content.strip() == "":
        st.info("Henüz önizlenecek bir HTML içeriği üretilmedi.")
        return

    full_page = f"""
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
        <style>
            body {{
                font-family: 'Inter', sans-serif;
                background-color: #ffffff;
                color: #1f2937;
                padding: 24px;
                margin: 0;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    components.html(full_page, height=height, scrolling=True)
