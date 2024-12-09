# utils.py
import re

def clean_text(text: str) -> str:
    """
    Limpa o texto removendo caracteres especiais e tornando tudo minúsculo.
    """
    text = text.lower()
    text = re.sub(r'[^a-zA-Zá-úÁ-Ú0-9\s]', '', text)
    text = text.strip()
    return text
