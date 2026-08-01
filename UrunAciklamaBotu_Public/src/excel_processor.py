"""
Excel Okuma, Satır Satır Dönüştürme ve Dışa Aktarma İş Mantığı
"""
import pandas as pd
import time
from io import BytesIO
from typing import Tuple, Dict, Any, Callable
from src.gemini_service import GeminiService

class ExcelProcessor:
    @staticmethod
    def read_excel_file(file_stream, has_header: bool = True, header_row: int = 0) -> pd.DataFrame:
        """Yüklenen Excel dosyasını pandas DataFrame olarak okur."""
        try:
            file_stream.seek(0)
            if has_header:
                df = pd.read_excel(file_stream, header=header_row)
            else:
                df = pd.read_excel(file_stream, header=None)
                df.columns = [f"Sütun {i+1} (Metin)" for i in range(len(df.columns))]
            return df
        except Exception as e:
            raise ValueError(f"Excel dosyası okunurken hata oluştu: {str(e)}")

    @staticmethod
    def process_dataframe(
        df: pd.DataFrame,
        column_name: str,
        gemini_service: GeminiService,
        model_name: str,
        prompt_template: str,
        progress_callback: Callable[[float, int, int, str], None] = None,
        delay_seconds: float = 1.2
    ) -> Tuple[pd.DataFrame, Dict[str, int]]:
        """
        DataFrame içerisindeki belirtilen sütunu satır satır Gemini ile işler.
        Döndürür: (güncellenmiş_df, istatistikler_dict)
        """
        df_copy = df.copy()
        total_rows = len(df_copy)
        new_descriptions = []
        success_count = 0
        error_count = 0

        for index, row in df_copy.iterrows():
            val = row[column_name]
            original_text = "" if pd.isna(val) else str(val).strip()

            if not original_text or original_text.lower() in ["nan", "none", "empty", "<na>"]:
                new_descriptions.append("")
                current_status = f"Satır {index + 1}/{total_rows}: Boş metin atlandı."
                if progress_callback:
                    progress_callback((index + 1) / total_rows, index + 1, total_rows, current_status)
                continue

            success, result = gemini_service.generate_html(
                model_name=model_name,
                original_text=original_text,
                custom_prompt_template=prompt_template
            )
            
            if success:
                new_descriptions.append(result)
                success_count += 1
                current_status = f"Satır {index + 1}/{total_rows}: HTML başarıyla üretildi."
            else:
                new_descriptions.append(f"Hata oluştu: {result}")
                error_count += 1
                current_status = f"Satır {index + 1}/{total_rows}: Hata oluştu!"

            progress = (index + 1) / total_rows
            if progress_callback:
                progress_callback(progress, index + 1, total_rows, current_status)

            if delay_seconds > 0 and index < total_rows - 1:
                time.sleep(delay_seconds)

        df_copy["Yeni_Aciklama_HTML"] = new_descriptions
        
        stats = {
            "total": total_rows,
            "processed": total_rows,
            "success": success_count,
            "error": error_count
        }
        
        return df_copy, stats

    @staticmethod
    def export_to_excel_bytes(df: pd.DataFrame) -> bytes:
        """İşlenmiş DataFrame'i Excel dosyası olarak BytesIO akışına yazar."""
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='HTML_Sonuclar')
        return output.getvalue()
