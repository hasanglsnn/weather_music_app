# services/weather_service.py
import requests
import config

def get_weather_by_coords(lat, lon):
    """
    Verilen koordinatlar için anlık hava durumunu getirir.
    """
    params = {
        "lat": lat,
        "lon": lon,
        "appid": config.OPENWEATHER_API_KEY,
        "units": "metric", # Santigrat derece için
        "lang": "tr"       # Türkçe açıklama için
    }

    try:
        response = requests.get(config.WEATHER_API_URL, params=params, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            
            # Bize lazım olan verileri çekip temiz bir sözlük yapalım
            weather_info = {
                "main_condition": data['weather'][0]['main'], # Örn: Rain, Clear
                "description": data['weather'][0]['description'], # Örn: Parçalı bulutlu
                "temp": int(data['main']['temp']), # Örn: 24
                "humidity": data['main']['humidity'], # Nem
                "wind_speed": data['wind']['speed'], # Rüzgar
                "city": data['name'],
                "success": True
            }
            return weather_info
        else:
            return {"success": False, "error": f"API Hatası: {response.status_code}"}
            
    except Exception as e:
        return {"success": False, "error": str(e)}