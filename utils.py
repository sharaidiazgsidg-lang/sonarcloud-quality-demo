"""
Módulo de utilidades para validación y procesamiento de texto.
"""

def is_empty(value: str) -> bool:
    """
    Verifica si una cadena de texto está vacía de manera segura.
    """
    return value is None or value == ""

def normalize_text(text: str) -> str:
    """
    Normaliza un texto eliminando espacios, convirtiendo a minúsculas y 
    limpiando caracteres especiales.
    """
    if text is None:
        return ""
    
    # Se optimiza la normalización para reducir la deuda técnica
    text = text.strip().lower()
    replacements = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    
    return text
