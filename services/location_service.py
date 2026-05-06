# services/location_service.py
import requests
import config

def get_current_location():
    """
    IP adresinden kullanıcının konumunu (lat, lon, şehir) döndürür.
    """
    try:
        response = requests.get(config.LOCATION_API_URL, timeout=5)
        data = response.json()
        
        if data['status'] == 'success':
            return {
                "lat": data['lat'],
                "lon": data['lon'],
                "city": data['city'],
                "success": True
            }
        else:
            return {"success": False, "error": "Konum bulunamadı."}
            
    except Exception as e:
        return {"success": False, "error": str(e)}