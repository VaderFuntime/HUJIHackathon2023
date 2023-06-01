from deep_translator import GoogleTranslator


def heb_to_eng(text: str) -> str:
    translated = GoogleTranslator(source='iw', target='en').translate(text=text)
    return translated

def eng_to_heb(text: str) -> str:
    translated = GoogleTranslator(source='en', target='iw').translate(text=text)
    return translated
