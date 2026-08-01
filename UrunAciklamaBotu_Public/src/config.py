"""
Uygulama Yapılandırması ve Prompt Şablon Rehberi (Public/Open-Source Edition)
"""
import os

APP_TITLE = "Ürün Açıklama Dönüştürücü"
APP_SUBTITLE = "E-ticaret ürün teknik detaylarını SEO uyumlu, estetik Tailwind HTML şablonlarına çevirin."
BRAND_NAME = "E-Ticaret Botu"
BRAND_PRIMARY_COLOR = "#E07B00"
BRAND_DARK_BG = "#0B0F19"

# Görsel Yolları
LOGO_PATH = os.path.join("assets", "UAB.png")

# ==============================================================================
# PROMPT ŞABLON REHBERİ (PROMPT TEMPLATE GUIDE)
# 
# Not: Bu alana kendi e-ticaret sitenizin tasarımına uygun özel Tailwind HTML
# prompt şablonunuzu yazabilirsiniz.
# 
# KRİTİK KURAL:
# Prompt içinde dönüştürülecek ham ürün metninin geleceği yere mutlaka
# `{original_text}` değişkenini ekleyiniz.
# ==============================================================================

DEFAULT_SYSTEM_PROMPT = """Sen profesyonel bir e-ticaret içerik editörüsün. Görevin, sana verilen karmaşık ve ham ürün teknik özelliklerini aşağıdaki HTML şablonuna göre yeniden yazmaktır.

[PROMPT OLUŞTURMA REHBERİ]:
1. ROL VE GÖREV: Yapay zekaya bir e-ticaret editörü rolü verin.
2. FORMAT KURALLARI: Sadece HTML kodu döndürmesini, ekstra açıklama ve ```html tag'i eklememesini belirtin.
3. KENDİ HTML / TAILWIND ŞABLONUNUZU BURAYA EKLEYİN:
   Örnek Yapı:
   - Başlık: <h2 class="text-2xl font-bold">[ÜRÜN BAŞLIĞI]</h2>
   - Açıklama: <p class="text-base text-gray-700">[SEO Uyumlu Genel Açıklama]</p>
   - Özellik Tablosu: <table class="w-full">...</table>
   - Liste: <ul class="list-disc pl-5">...</ul>

İŞLENECEK HAM METİN:
{original_text}"""
