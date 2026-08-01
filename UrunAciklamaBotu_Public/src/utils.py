"""
Yardımcı Fonksiyonlar, Metin İşleme ve Sistem Bildirimleri
"""
import re
import subprocess
import sys

def clean_html_output(raw_text: str) -> str:
    """
    AI tarafından döndürülen ham metinden ```html ... ``` ve benzeri
    markdown etiketlerini temizler.
    """
    if not raw_text:
        return ""
    
    clean_text = re.sub(r"^```(?:html)?\s*", "", raw_text, flags=re.MULTILINE)
    clean_text = re.sub(r"\s*```$", "", clean_text, flags=re.MULTILINE)
    
    return clean_text.strip()

def validate_api_key(api_key: str) -> bool:
    """
    API anahtarının temel biçimini kontrol eder.
    """
    if not api_key:
        return False
    return len(api_key.strip()) > 10

def send_desktop_notification(title: str, message: str):
    """
    Windows İşletim Sistemi Masaüstü Bildirimi (Toast / Action Center) gönderir.
    """
    try:
        if sys.platform == "win32":
            ps_script = f"""
            Add-Type -AssemblyName System.Windows.Forms
            $global:balloon = New-Object System.Windows.Forms.NotifyIcon
            $balloon.Icon = [System.Drawing.SystemIcons]::Information
            $balloon.BalloonTipTitle = '{title}'
            $balloon.BalloonTipText = '{message}'
            $balloon.Visible = $true
            $balloon.ShowBalloonTip(7000)
            """
            subprocess.Popen(
                ["powershell", "-NoProfile", "-Command", ps_script],
                creationflags=subprocess.CREATE_NO_WINDOW
            )
    except Exception as e:
        print(f"Masaüstü bildirimi gönderilirken hata: {e}")
