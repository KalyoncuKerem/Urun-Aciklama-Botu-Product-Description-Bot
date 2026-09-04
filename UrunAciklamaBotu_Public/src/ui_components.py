"""
Modern Anti-Slop UI & Visual Render Bileşenleri
Tasarım Referansları: Design DNA, Taste-Skill, Scroll-Craft, Anthropic Skills
Marka Renkleri: #ff9610 (Sıcak Kehribar/Turuncu), #009cf3 (Elektrik Gök Mavisi)
"""
import streamlit as st
import streamlit.components.v1 as components
import os
import base64
from src.config import (
    APP_TITLE,
    APP_SUBTITLE,
    BRAND_PRIMARY_COLOR,
    BRAND_SECONDARY_COLOR,
    BRAND_DARK_BG,
    BRAND_SURFACE_BG,
    LOGO_PATH
)

def load_image_as_base64(path: str) -> str:
    """Görsel dosyasını base64 formatına çevirir (HTML embed için)."""
    if os.path.exists(path):
        with open(path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    return ""

def inject_custom_css():
    """
    Anti-Slop, yüksek zevkli modern stüdyo CSS stillerini yükler.
    Klişe mor/neon AI efektleri ve aşırı blur kaldırılmıştır.
    Bileşenler yumuşak kenarlı (14-22px squircle), duyarlı ve dokunsal geri bildirimle donatılmıştır.
    """
    custom_css = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    :root {{
        --brand-orange: {BRAND_PRIMARY_COLOR};
        --brand-orange-hover: #ffaa33;
        --brand-blue: {BRAND_SECONDARY_COLOR};
        --brand-blue-hover: #1ab0ff;
        --bg-base: {BRAND_DARK_BG};
        --bg-surface: {BRAND_SURFACE_BG};
        --bg-elevated: #182236;
        --border-subtle: rgba(255, 255, 255, 0.08);
        --border-hover: rgba(255, 150, 16, 0.35);
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --text-muted: #64748B;
        --radius-sm: 10px;
        --radius-md: 14px;
        --radius-lg: 18px;
        --radius-xl: 24px;
    }}

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: var(--text-primary);
    }}

    /* Streamlit varsayılan gereksiz menülerini ve Deploy butonunu gizleme */
    #MainMenu {{visibility: hidden !important; display: none !important;}}
    footer {{visibility: hidden !important; display: none !important;}}
    .stDeployButton,
    [data-testid="stDeployButton"],
    [data-testid="stAppDeployButton"],
    div[class*="stDeployButton"],
    div[data-testid="stToolbarActions"],
    header[data-testid="stHeader"] [data-testid="stToolbarActions"],
    header[data-testid="stHeader"] [data-testid="stToolbar"],
    header[data-testid="stHeader"] button[kind="header"],
    header[data-testid="stHeader"] div:has(> button[data-testid*="header"]),
    .stAppToolbar {{
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
        width: 0 !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }}
    a.header-anchor, h1 a svg, h2 a svg, h3 a svg {{display: none !important;}}
    [data-testid="stElementToolbar"] {{display: none !important; visibility: hidden !important;}}

    /* Kompakt ve Simetrik Sayfa Izgarası (Balanced Centered Shell) */
    .block-container {{
        max-width: 1120px !important;
        padding-top: 1.25rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }}

    /* Ana Arka Plan: Mat ve derin arduvaz stüdyo dokusu (Klişe parıltı içermez) */
    .stApp {{
        background: radial-gradient(circle at 50% -10%, #152033 0%, var(--bg-base) 65%) !important;
        background-attachment: fixed !important;
    }}

    /* Header Arka Planını Şeffaf Yap */
    header[data-testid="stHeader"] {{
        background: transparent !important;
        z-index: 99999 !important;
    }}

    /* Sidebar Açma/Kapatma Butonunu DAİMA GÖRÜNÜR ve ŞIK Yap */
    [data-testid="stSidebarCollapseButton"], 
    button[aria-label="Expand sidebar"], 
    button[aria-label="Collapse sidebar"],
    [data-testid="collapsedControl"] {{
        visibility: visible !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        color: var(--brand-orange) !important;
        background: rgba(19, 27, 42, 0.9) !important;
        border: 1px solid rgba(255, 150, 16, 0.4) !important;
        border-radius: var(--radius-md) !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
        z-index: 100000 !important;
    }}

    [data-testid="stSidebarCollapseButton"]:hover,
    [data-testid="collapsedControl"]:hover {{
        background: var(--brand-orange) !important;
        color: #0c1017 !important;
        transform: scale(1.06);
        box-shadow: 0 6px 20px rgba(255, 150, 16, 0.4) !important;
    }}

    /* Sidebar Genel Tasarımı */
    [data-testid="stSidebar"] {{
        background: #0E1522 !important;
        border-right: 1px solid var(--border-subtle) !important;
    }}

    /* Anti-Slop Yüzey Kartları (Kompakt ve Simetrik) */
    .studio-card {{
        background: var(--bg-surface);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 16px 18px;
        margin-bottom: 12px;
        box-shadow: 0 4px 16px -4px rgba(0, 0, 0, 0.35);
        transition: border-color 0.2s ease;
    }}

    .studio-card:hover {{
        border-color: rgba(255, 150, 16, 0.25);
    }}

    /* Hero Header: Kompakt, Karakterli ve Simetrik */
    .hero-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        background: linear-gradient(135deg, rgba(255, 150, 16, 0.07) 0%, rgba(0, 156, 243, 0.04) 50%, var(--bg-surface) 100%);
        border: 1px solid rgba(255, 150, 16, 0.18);
        border-radius: var(--radius-lg);
        padding: 14px 22px;
        margin-bottom: 12px;
        box-shadow: 0 4px 18px -6px rgba(0, 0, 0, 0.45);
    }}

    .hero-left {{
        display: flex;
        align-items: center;
        gap: 14px;
    }}

    .hero-logo {{
        width: 48px;
        height: 48px;
        object-fit: contain;
        border-radius: var(--radius-sm);
        filter: drop-shadow(0 2px 10px rgba(255, 150, 16, 0.25));
    }}

    .hero-title-group h1 {{
        font-size: 1.45rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.025em !important;
        color: #FFFFFF !important;
        margin: 0 0 2px 0 !important;
        padding: 0 !important;
        display: flex;
        align-items: center;
        gap: 8px;
    }}

    .hero-title-group h1 span.highlight {{
        color: var(--brand-orange);
    }}

    .hero-title-group p {{
        color: var(--text-secondary);
        font-size: 0.84rem;
        margin: 0;
        line-height: 1.35;
    }}

    .badge-studio {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(0, 156, 243, 0.12);
        color: var(--brand-blue);
        border: 1px solid rgba(0, 156, 243, 0.3);
        font-size: 0.72rem;
        font-weight: 700;
        padding: 4px 12px;
        border-radius: 9999px;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }}

    .badge-tag {{
        display: inline-block;
        background: rgba(255, 150, 16, 0.12);
        color: var(--brand-orange);
        border: 1px solid rgba(255, 150, 16, 0.3);
        font-size: 0.7rem;
        font-weight: 700;
        padding: 2px 10px;
        border-radius: 9999px;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }}

    /* 3 Adımlı Sezgisel Süreç Çubuğu (Kompakt ve Dengeli) */
    .stepper-container {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: rgba(19, 27, 42, 0.6);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-md);
        padding: 8px 18px;
        margin-bottom: 14px;
        gap: 8px;
    }}

    .step-item {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 0.82rem;
        font-weight: 600;
        color: var(--text-muted);
        transition: all 0.2s ease;
    }}

    .step-item.active {{
        color: #FFFFFF;
    }}

    .step-item.completed {{
        color: var(--brand-blue);
    }}

    .step-circle {{
        width: 22px;
        height: 22px;
        border-radius: 9999px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.72rem;
        font-weight: 700;
        background: rgba(255, 255, 255, 0.05);
        color: var(--text-muted);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}

    .step-item.active .step-circle {{
        background: var(--brand-orange);
        color: #0c1017;
        border-color: var(--brand-orange);
        box-shadow: 0 0 10px rgba(255, 150, 16, 0.45);
    }}

    .step-item.completed .step-circle {{
        background: var(--brand-blue);
        color: #FFFFFF;
        border-color: var(--brand-blue);
    }}

    .step-divider {{
        flex: 1;
        height: 2px;
        background: rgba(255, 255, 255, 0.08);
        margin: 0 10px;
        border-radius: 2px;
    }}

    .step-divider.active {{
        background: linear-gradient(90deg, var(--brand-orange), var(--brand-blue));
    }}

    /* Dokunsal ve Yumuşak Butonlar (Kompakt) */
    .stButton > button {{
        background: linear-gradient(180deg, #ffa834 0%, var(--brand-orange) 100%) !important;
        color: #0B0F17 !important;
        font-weight: 800 !important;
        font-size: 0.92rem !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        border-radius: var(--radius-sm) !important;
        padding: 9px 18px !important;
        box-shadow: 0 2px 10px rgba(255, 150, 16, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.35) !important;
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
        width: 100%;
        letter-spacing: -0.01em;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 18px rgba(255, 150, 16, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.45) !important;
        background: linear-gradient(180deg, #ffb24d 0%, #ff9e24 100%) !important;
    }}

    .stButton > button:active {{
        transform: translateY(0) scale(0.98) !important;
        box-shadow: 0 2px 6px rgba(255, 150, 16, 0.3) !important;
    }}

    /* İndirme Butonu (Download Button) */
    .stDownloadButton > button {{
        background: linear-gradient(180deg, #1ab0ff 0%, var(--brand-blue) 100%) !important;
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 0.92rem !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        border-radius: var(--radius-sm) !important;
        padding: 9px 18px !important;
        box-shadow: 0 2px 12px rgba(0, 156, 243, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.35) !important;
        transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
        width: 100%;
        letter-spacing: -0.01em;
    }}

    .stDownloadButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 156, 243, 0.45), inset 0 1px 0 rgba(255, 255, 255, 0.45) !important;
        background: linear-gradient(180deg, #38bdff 0%, #0593e6 100%) !important;
    }}

    .stDownloadButton > button:active {{
        transform: translateY(0) scale(0.98) !important;
    }}

    /* Tab Stilleri: Eşit Bölünmüş Simetrik Hap Konteyner */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 4px;
        background: rgba(19, 27, 42, 0.7);
        padding: 4px;
        border-radius: var(--radius-md);
        border: 1px solid var(--border-subtle);
        margin-bottom: 14px;
        display: flex;
        width: 100%;
    }}

    .stTabs [data-baseweb="tab"] {{
        flex: 1;
        height: 38px;
        border-radius: var(--radius-sm);
        color: var(--text-secondary);
        font-weight: 600;
        font-size: 0.88rem;
        padding: 0 12px;
        justify-content: center;
        text-align: center;
        transition: all 0.2s ease;
        border: none !important;
    }}

    .stTabs [data-baseweb="tab"]:hover {{
        color: #FFFFFF;
        background: rgba(255, 255, 255, 0.04);
    }}

    .stTabs [aria-selected="true"] {{
        background: var(--brand-orange) !important;
        color: #0c1017 !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 10px rgba(255, 150, 16, 0.3) !important;
    }}

    /* Form Elemanları (Input, Select, Slider) */
    div[data-baseweb="input"] > div,
    div[data-baseweb="select"] > div {{
        background-color: var(--bg-elevated) !important;
        border: 1px solid var(--border-subtle) !important;
        border-radius: var(--radius-sm) !important;
        color: #FFFFFF !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
    }}

    div[data-baseweb="input"] > div:focus-within,
    div[data-baseweb="select"] > div:focus-within {{
        border-color: var(--brand-blue) !important;
        box-shadow: 0 0 0 3px rgba(0, 156, 243, 0.22) !important;
    }}

    /* Dosya Yükleme Dropzone (Kompakt) */
    [data-testid="stFileUploader"] section {{
        background-color: var(--bg-surface) !important;
        border: 2px dashed rgba(255, 150, 16, 0.35) !important;
        border-radius: var(--radius-md) !important;
        padding: 16px 14px !important;
        transition: all 0.25s ease !important;
    }}

    [data-testid="stFileUploader"] section:hover {{
        border-color: var(--brand-orange) !important;
        background-color: rgba(255, 150, 16, 0.04) !important;
    }}

    /* İlerleme Çubuğu (Progress Bar) */
    .stProgress > div > div > div > div {{
        background: linear-gradient(90deg, var(--brand-orange) 0%, var(--brand-blue) 100%) !important;
        border-radius: 9999px !important;
    }}

    .stProgress > div > div > div {{
        background-color: rgba(255, 255, 255, 0.06) !important;
        border-radius: 9999px !important;
    }}

    /* Metrik Kartları (Kompakt ve 4'lü Simetrik) */
    .metric-container {{
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 10px;
        margin-bottom: 14px;
    }}

    .metric-card {{
        background: var(--bg-surface);
        border: 1px solid var(--border-subtle);
        border-radius: var(--radius-sm);
        padding: 12px 14px;
        text-align: center;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }}

    .metric-card:hover {{
        transform: translateY(-2px);
        border-color: rgba(255, 255, 255, 0.16);
    }}

    .metric-value {{
        font-size: 1.55rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        line-height: 1.1;
    }}

    .metric-label {{
        font-size: 0.72rem;
        color: var(--text-secondary);
        font-weight: 600;
        margin-top: 3px;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}

    /* Responsive Medya Sorguları */
    @media (max-width: 768px) {{
        .hero-container {{
            flex-direction: column;
            align-items: flex-start;
            padding: 14px;
        }}
        .hero-logo {{
            width: 42px;
            height: 42px;
        }}
        .hero-title-group h1 {{
            font-size: 1.3rem !important;
        }}
        .stepper-container {{
            flex-direction: column;
            align-items: flex-start;
            gap: 10px;
        }}
        .step-divider {{
            display: none;
        }}
        .metric-container {{
            grid-template-columns: 1fr 1fr;
        }}
    }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def render_hero_header():
    """Anti-Slop, modern stüdyo Hero Banner'ı çizer."""
    logo_base64 = load_image_as_base64(LOGO_PATH)
    img_html = f'<img src="data:image/png;base64,{logo_base64}" class="hero-logo" alt="Logo">' if logo_base64 else ''

    header_html = f"""
    <div class="hero-container">
        <div class="hero-left">
            {img_html}
            <div class="hero-title-group">
                <h1>
                    {APP_TITLE}
                    <span class="badge-tag">v2.5</span>
                </h1>
                <p>{APP_SUBTITLE}</p>
            </div>
        </div>
        <div class="hero-right">
            <span class="badge-studio">E-Commerce Studio</span>
        </div>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def render_stepper(current_step: int = 1):
    """
    Kullanıcının iş akışındaki mevcut durumunu gösteren 3 adımlı süreç çubuğu.
    current_step: 1 (Yükleme), 2 (İşleme), 3 (Önizleme & İndir)
    """
    step1_cls = "completed" if current_step > 1 else ("active" if current_step == 1 else "")
    step2_cls = "completed" if current_step > 2 else ("active" if current_step == 2 else "")
    step3_cls = "completed" if current_step > 3 else ("active" if current_step == 3 else "")

    div1_cls = "active" if current_step >= 2 else ""
    div2_cls = "active" if current_step >= 3 else ""

    stepper_html = f"""
    <div class="stepper-container">
        <div class="step-item {step1_cls}">
            <div class="step-circle">{'✓' if current_step > 1 else '1'}</div>
            <span>1. Excel Yükle & Sütun Seç</span>
        </div>
        <div class="step-divider {div1_cls}"></div>
        <div class="step-item {step2_cls}">
            <div class="step-circle">{'✓' if current_step > 2 else '2'}</div>
            <span>2. AI HTML Dönüştürme</span>
        </div>
        <div class="step-divider {div2_cls}"></div>
        <div class="step-item {step3_cls}">
            <div class="step-circle">{'✓' if current_step > 3 else '3'}</div>
            <span>3. Canlı Önizle & İndir</span>
        </div>
    </div>
    """
    st.markdown(stepper_html, unsafe_allow_html=True)

def render_metric_cards(total_rows: int, processed_rows: int, success_count: int, error_count: int):
    """İşlem istatistiklerini marka renkli squircle kartlar şeklinde gösterir."""
    html_metrics = f"""
    <div class="metric-container">
        <div class="metric-card">
            <div class="metric-value" style="color: {BRAND_PRIMARY_COLOR};">{total_rows}</div>
            <div class="metric-label">Toplam Satır</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: {BRAND_SECONDARY_COLOR};">{processed_rows}</div>
            <div class="metric-label">İşlenen</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: #10B981;">{success_count}</div>
            <div class="metric-label">Başarılı</div>
        </div>
        <div class="metric-card">
            <div class="metric-value" style="color: {'#EF4444' if error_count > 0 else '#64748B'};">{error_count}</div>
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

def render_tailwind_live_preview(html_content: str, device_mode: str = "desktop", height: int = 500):
    """
    Üretilen Tailwind HTML içeriğini Tailwind CDN ile iframe içerisinde render eder.
    device_mode:
      - 'desktop': Tarayıcı penceresi simülasyonu
      - 'mobile': 375px genişliğinde gerçekçi akıllı telefon çerçeve simülatörü (iPhone tarzı çentik ve yumuşak kenarlar)
    """
    if not html_content or html_content.strip() == "":
        st.info("📌 Henüz önizlenecek bir HTML içeriği üretilmedi.")
        return

    safe_body = html_content.replace('</script>', '<\\/script>')

    if device_mode == "mobile":
        full_page = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <script src="https://cdn.tailwindcss.com"></script>
            <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
            <style>
                * {{ box-sizing: border-box; }}
                body {{
                    margin: 0;
                    padding: 10px 0;
                    background-color: transparent;
                    display: flex;
                    justify-content: center;
                    font-family: 'Plus Jakarta Sans', sans-serif;
                }}
                .phone-chassis {{
                    width: 375px;
                    background: #ffffff;
                    border: 9px solid #1E293B;
                    border-radius: 40px;
                    box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(255, 255, 255, 0.1);
                    overflow: hidden;
                    display: flex;
                    flex-direction: column;
                }}
                .phone-notch-bar {{
                    background: #1E293B;
                    height: 22px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                .phone-speaker {{
                    width: 50px;
                    height: 4px;
                    background: #0f172a;
                    border-radius: 4px;
                }}
                .phone-screen {{
                    padding: 18px 16px;
                    background: #ffffff;
                    color: #1f2937;
                    max-height: 560px;
                    overflow-y: auto;
                }}
                .phone-screen::-webkit-scrollbar {{
                    width: 4px;
                }}
                .phone-screen::-webkit-scrollbar-thumb {{
                    background: #cbd5e1;
                    border-radius: 4px;
                }}
            </style>
        </head>
        <body>
            <div class="phone-chassis">
                <div class="phone-notch-bar">
                    <div class="phone-speaker"></div>
                </div>
                <div class="phone-screen">
                    {safe_body}
                </div>
            </div>
        </body>
        </html>
        """
        components.html(full_page, height=620, scrolling=False)
    else:
        full_page = f"""
        <!DOCTYPE html>
        <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <script src="https://cdn.tailwindcss.com"></script>
            <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
            <style>
                * {{ box-sizing: border-box; }}
                body {{
                    margin: 0;
                    padding: 0;
                    background-color: transparent;
                    font-family: 'Plus Jakarta Sans', sans-serif;
                }}
                .browser-window {{
                    background: #ffffff;
                    border-radius: 16px;
                    border: 1px solid rgba(255, 255, 255, 0.12);
                    box-shadow: 0 16px 40px -10px rgba(0, 0, 0, 0.5);
                    overflow: hidden;
                }}
                .browser-header {{
                    background: #0F172A;
                    padding: 10px 16px;
                    display: flex;
                    align-items: center;
                    gap: 8px;
                    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
                }}
                .dot {{
                    width: 10px;
                    height: 10px;
                    border-radius: 9999px;
                }}
                .dot-red {{ background: #EF4444; }}
                .dot-yellow {{ background: #F59E0B; }}
                .dot-green {{ background: #10B981; }}
                .browser-url {{
                    margin-left: 12px;
                    background: rgba(255, 255, 255, 0.07);
                    padding: 3px 12px;
                    border-radius: 6px;
                    font-size: 0.74rem;
                    color: #94A3B8;
                    font-family: 'JetBrains Mono', monospace;
                }}
                .browser-content {{
                    padding: 24px;
                    background: #ffffff;
                    color: #1f2937;
                    max-height: {height}px;
                    overflow-y: auto;
                }}
            </style>
        </head>
        <body>
            <div class="browser-window">
                <div class="browser-header">
                    <div class="dot dot-red"></div>
                    <div class="dot dot-yellow"></div>
                    <div class="dot dot-green"></div>
                    <div class="browser-url">store.preview/product-details.html</div>
                </div>
                <div class="browser-content">
                    {safe_body}
                </div>
            </div>
        </body>
        </html>
        """
        components.html(full_page, height=height + 60, scrolling=True)
