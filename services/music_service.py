# services/music_service.py
import random
from data.weather_music_data import get_weather_data

def get_recommendations(weather_condition):
    """
    Hava durumu anahtar kelimesine (örn: 'Rain') göre
    müzik, ikon ve cümle verilerini getirir.
    """
    # 1. Veri dosyamızdan ilgili havayı çek (Yoksa varsayılan gelir)
    data = get_weather_data(weather_condition)
    
    # 2. 5 cümleden rastgele birini seçip 'daily_quote' olarak ekleyelim
    # (Arayüzde tek cümle göstereceksen bunu kullanırsın)
    selected_quote = random.choice(data['sentences'])
    
    # 3. Veriyi paketleyip döndür
    return {
        "condition": weather_condition,
        "icon": data['icon'],
        "quote": selected_quote,      # Rastgele seçilen 1 cümle
        "all_quotes": data['sentences'], # Tüm cümle listesi (Lazım olursa)
        "songs": data['songs']        # Şarkı listesi
    }