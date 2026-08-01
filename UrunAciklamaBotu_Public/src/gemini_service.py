"""
Google Gemini API Servisi Modülü
"""
import google.generativeai as genai
from typing import List, Tuple, Optional
from src.utils import clean_html_output

class GeminiService:
    def __init__(self, api_key: str):
        self.api_key = api_key.strip()
        genai.configure(api_key=self.api_key)
        
    def get_available_models(self) -> List[str]:
        """
        API anahtarıyla erişilebilen ve içerik üretimi destekleyen modelleri döndürür.
        """
        available_models = []
        try:
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    model_name = m.name.replace("models/", "")
                    available_models.append(model_name)
        except Exception as e:
            raise RuntimeError(f"Model listesi alınırken hata oluştu: {str(e)}")
            
        return available_models

    def generate_html(self, model_name: str, original_text: str, custom_prompt_template: str) -> Tuple[bool, str]:
        """
        Belirtilen modeli kullanarak ham ürün metnini Tailwind HTML koduna çevirir.
        Döndürür: (başarılı_mı: bool, sonuc_veya_hata: str)
        """
        if not original_text or str(original_text).strip() == "" or str(original_text).lower() in ["nan", "none", "empty"]:
            return True, ""
            
        try:
            if "{original_text}" in custom_prompt_template:
                prompt = custom_prompt_template.format(original_text=str(original_text))
            else:
                prompt = f"{custom_prompt_template}\n\nHAM METİN:\n{original_text}"
        except Exception:
            prompt = f"{custom_prompt_template}\n\nHAM METİN:\n{original_text}"
        
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content(prompt)
            clean_output = clean_html_output(response.text)
            return True, clean_output
        except Exception as e:
            return False, f"Hata: {str(e)}"
