# data/weather_music_data.py

# Bu dosya, hava durumuna göre içerik (Müzik, Cümle, İkon) veritabanıdır.

# data/weather_music_data.py

# Bu dosya, hava durumuna göre içerik (Müzik, Cümle, İkon) veritabanıdır.

FULL_WEATHER_DATA = {
    "Clear": {
        "icon": "sunny.png", # .gif -> .png olarak güncellendi
        "sentences": [
            "Güneş harika parlıyor, tam yürüyüş havası!",
            "Bugün gökyüzü masmavi, enerjini yüksek tut.",
            "Güneş gözlüğünü tak ve anın tadını çıkar.",
            "D vitamini alma zamanı, dışarı çıkmalısın.",
            "Hava açık, zihnin de öyle olsun."
        ],
        "songs": [
            {"artist": "Pharrell Williams", "title": "Happy", "url": "https://music.youtube.com/watch?v=ZbZSe6N_BXs"},
            {"artist": "Daft Punk", "title": "Get Lucky", "url": "https://music.youtube.com/watch?v=5NV6Rdv1a3I"},
            {"artist": "Calvin Harris", "title": "Feel So Close", "url": "https://music.youtube.com/watch?v=dGghkjpNCQ8"}
        ]
    },
    "Clouds": {
        "icon": "cloudy.png", # .gif -> .png olarak güncellendi
        "sentences": [
            "Bulutlar gökyüzünü süslüyor, sakin bir gün.",
            "Biraz gri olabilir ama keyfin yerinde olsun.",
            "Kahveni al ve bulutları izle.",
            "Hava kapalı olsa da senin ışığın yeter.",
            "Tam odaklanıp çalışma havası."
        ],
        "songs": [
            {"artist": "Arctic Monkeys", "title": "Do I Wanna Know?", "url": "https://music.youtube.com/watch?v=bpOSxM0rNPM"},
            {"artist": "Cigarettes After Sex", "title": "Apocalypse", "url": "https://music.youtube.com/watch?v=sElE_BfQ67s"},
            {"artist": "The Neighbourhood", "title": "Sweater Weather", "url": "https://music.youtube.com/watch?v=GCdwKhTtNNw"}
        ]
    },
    "Rain": {
        "icon": "rainy.png", # .gif -> .png olarak güncellendi
        "sentences": [
            "Yağmurun sesi ruhunu dinlendirsin.",
            "Şemsiyeni almayı unutma!",
            "Toprak kokusu huzur veriyor.",
            "Cam kenarında kitap okumak için harika bir an.",
            "Bırak yağmur tüm stresi alıp götürsün."
        ],
        "songs": [
            {"artist": "Adele", "title": "Someone Like You", "url": "https://music.youtube.com/watch?v=hLQl3WQQoQ0"},
            {"artist": "Sam Smith", "title": "Stay With Me", "url": "https://music.youtube.com/watch?v=pB-5XG-DbAA"},
            {"artist": "Lewis Capaldi", "title": "Someone You Loved", "url": "https://music.youtube.com/watch?v=zABLecsR5UE"}
        ]
    },
    "Drizzle": {
        "icon": "rainy.png", # .gif -> .png olarak güncellendi
        "sentences": ["Hafif bir çiseleme var, huzurlu.", "Doğa hafifçe ıslanıyor.", "Yürüyüş için şemsiyeni al.", "Toprak kokusu gelmeye başladı.", "Sakinliğin tadını çıkar."],
        "songs": [
            {"artist": "Billie Eilish", "title": "Ocean Eyes", "url": "https://music.youtube.com/watch?v=viimfQi_pUw"},
            {"artist": "Sam Smith", "title": "Too Good at Goodbyes", "url": "https://music.youtube.com/watch?v=J_ub7Etch2U"},
            {"artist": "Halsey", "title": "Without Me", "url": "https://music.youtube.com/watch?v=ZAfAud_M_mg"}
        ]
    },
    "Thunderstorm": {
        "icon": "rainy.png", # Fırtına için de şimdilik yağmur ikonu kullanılabilir (varsa storm.png)
        "sentences": ["Gök gürlüyor, gücü hisset!", "Dışarısı kıyamet, içerisi güvenli.", "Şimşekleri izlemek büyüleyici.", "Doğanın en güçlü hali.", "Evde kalıp müziğin sesini aç."],
        "songs": [
            {"artist": "Imagine Dragons", "title": "Believer", "url": "https://music.youtube.com/watch?v=7wtfhZwyrcc"},
            {"artist": "The Weeknd", "title": "After Hours", "url": "https://music.youtube.com/watch?v=ygTZZpVkmKg"},
            {"artist": "Kanye West", "title": "Black Skinhead", "url": "https://music.youtube.com/watch?v=q604eed4ad0"}
        ]
    },
    "Snow": {
        "icon": "snow.png", # .gif -> .png olarak güncellendi
        "sentences": ["Kar yağıyor, her yer bembeyaz!", "Sıcak çikolata zamanı.", "Huzurlu bir sessizlik var.", "Lapa lapa yağan karı izle.", "Kışın en güzel anı."],
        "songs": [
            {"artist": "Bon Iver", "title": "Holocene", "url": "https://music.youtube.com/watch?v=TWcyIpul8OE"},
            {"artist": "Taylor Swift", "title": "Exile", "url": "https://music.youtube.com/watch?v=osdoLjUNFnA"},
            {"artist": "AURORA", "title": "Runaway", "url": "https://music.youtube.com/watch?v=d_HlPboLRL8"}
        ]
    },
    "Mist": {
        "icon": "cloudy.png", # Sis için bulut ikonu
        "sentences": ["Sisli bir gün, gizemli.", "Görüş mesafesi düşük ama müzik net.", "Sessizliğin sesi.", "Melankolik bir hava.", "Kendi içine dönme zamanı."],
        "songs": [
            {"artist": "Coldplay", "title": "Fix You", "url": "https://music.youtube.com/watch?v=k4V3Mo61fJM"},
            {"artist": "London Grammar", "title": "Strong", "url": "https://music.youtube.com/watch?v=6drfp_3823I"},
            {"artist": "Sia", "title": "Breathe Me", "url": "https://music.youtube.com/watch?v=ghPcYqn0p4Y"}
        ]
    },
    "Fog": {
        "icon": "cloudy.png", # Sis için bulut ikonu
        "sentences": ["Yoğun sis var, dikkatli ol.", "Şehir siste kaybolmuş.", "Film sahnesi gibi bir gün.", "Biraz ürpertici ama güzel.", "Derin düşüncelere dal."],
        "songs": [
            {"artist": "Radiohead", "title": "No Surprises", "url": "https://music.youtube.com/watch?v=u5CVsCnxyXg"},
            {"artist": "The National", "title": "I Need My Girl", "url": "https://music.youtube.com/watch?v=A-Tod1_tZdU"},
            {"artist": "Interpol", "title": "Leif Erikson", "url": "https://music.youtube.com/watch?v=dkpgz3uQ58U"}
        ]
    },
    "Haze": {
        "icon": "cloudy.png", # Pus için bulut ikonu
        "sentences": ["Hafif puslu bir gün.", "Gözlerini dinlendir.", "Müziğin ritmine kapıl.", "Sakin kal.", "Günün tadını çıkar."],
        "songs": [
            {"artist": "Lana Del Rey", "title": "Summertime Sadness", "url": "https://music.youtube.com/watch?v=TdrL3QxjyVw"},
            {"artist": "The Weeknd", "title": "Blinding Lights", "url": "https://music.youtube.com/watch?v=4NRXx6U8ABQ"},
            {"artist": "Harry Styles", "title": "As It Was", "url": "https://music.youtube.com/watch?v=H5v3kku4y6Q"}
        ]
    }
}

# --- DÜZELTİLMİŞ EXTRA_CATEGORIES ---
# Artık tam yapıya sahip, for döngüsüne gerek yok.
EXTRA_CATEGORIES = {
    "Smoke": {
        "icon": "cloudy.png",
        "sentences": [
            "Hava biraz dumanlı, görüş mesafesi düşük olabilir.",
            "Hava kalitesi düşük, dışarıda fazla kalmamaya çalış.",
            "Pencereleri kapalı tutmak iyi bir fikir olabilir.",
            "Bu puslu havada sakinleştirici müzikler iyi gider.",
            "Dikkatli ol, hava biraz boğucu."
        ],
        "songs": [
            {"artist": "Lana Del Rey", "title": "Dark Paradise", "url": "https://music.youtube.com/watch?v=JRWox-i6aAk"},
            {"artist": "Arctic Monkeys", "title": "Fire and the Thud", "url": "https://music.youtube.com/watch?v=I7rkCHBHPN8"},
            {"artist": "Depeche Mode", "title": "Enjoy the Silence", "url": "https://music.youtube.com/watch?v=aGSKrC7dGcY"}
        ]
    },
    "Dust": {
        "icon": "cloudy.png",
        "sentences": [
            "Havada toz var, maske takmak isteyebilirsin.",
            "Görüş mesafesi kısıtlı, dikkatli ol.",
            "Hava biraz rahatsız edici, iç mekanda kal.",
            "Bu tozlu havada zihnini müziğe ver.",
            "Sakin kal, toz bulutu dağılacaktır."
        ],
        "songs": [
            {"artist": "Linkin Park", "title": "Leave Out All The Rest", "url": "https://music.youtube.com/watch?v=yZIummTz9mM"},
            {"artist": "Radiohead", "title": "Street Spirit (Fade Out)", "url": "https://music.youtube.com/watch?v=LCJblaUkkfc"},
            {"artist": "Placebo", "title": "Running Up That Hill", "url": "https://music.youtube.com/watch?v=x5GuBa4Bbnw"}
        ]
    },
    "Sand": {
        "icon": "cloudy.png",
        "sentences": [
            "Kum fırtınası olabilir, pencereleri kapat.",
            "Dışarı çıkarken gözlerini koru.",
            "Hava turuncu ve puslu, farklı bir atmosfer.",
            "Bu havada güçlü müzikler iyi hissettirebilir.",
            "Güvende kal, bu da geçecek."
        ],
        "songs": [
            {"artist": "Kaleo", "title": "Way Down We Go", "url": "https://music.youtube.com/watch?v=0-7IHOXkiV8"},
            {"artist": "Imagine Dragons", "title": "Natural", "url": "https://music.youtube.com/watch?v=V5M2WZiAy6k"},
            {"artist": "AWOLNATION", "title": "Sail", "url": "https://music.youtube.com/watch?v=tgIqecROs5M"}
        ]
    },
    "Ash": {
        "icon": "cloudy.png",
        "sentences": [
            "Havada volkanik kül olabilir, dikkat!",
            "Kesinlikle maske tak ve dışarı çıkma.",
            "Gökyüzü grileşti, güvenli bir yerde kal.",
            "Bu olağandışı durumda müziğe sığın.",
            "Haberleri takip et ve güvende kal."
        ],
        "songs": [
            {"artist": "Billie Eilish", "title": "bury a friend", "url": "https://music.youtube.com/watch?v=HUHC9tYz8ik"},
            {"artist": "Nine Inch Nails", "title": "The Day the World Went Away", "url": "https://music.youtube.com/watch?v=TwYfE-z6E6Q"},
            {"artist": "Bring Me The Horizon", "title": "Sleepwalking", "url": "https://music.youtube.com/watch?v=lir3dzYIhz0"}
        ]
    },
    "Squall": {
        "icon": "rainy.png",
        "sentences": [
            "Ani ve şiddetli bir rüzgar var!",
            "Dışarısı kıyamet, içerisi güvenli.",
            "Hava birden patladı, dikkatli ol.",
            "Bu enerjik havada enerjik müzikler dinle.",
            "Fırtınanın geçmesini bekle."
        ],
        "songs": [
            {"artist": "Muse", "title": "Knights of Cydonia", "url": "https://music.youtube.com/watch?v=G_sBOsh-vyI"},
            {"artist": "Thirty Seconds to Mars", "title": "The Kill", "url": "https://music.youtube.com/watch?v=8yvGCAvOAfM"},
            {"artist": "Linkin Park", "title": "Faint", "url": "https://music.youtube.com/watch?v=LYU-8IFcDPw"}
        ]
    },
    "Tornado": {
        "icon": "rainy.png",
        "sentences": [
            "TORNADO UYARISI! Hemen sığınağa git.",
            "Pencerelerden uzak dur, iç odalara geç.",
            "Bu çok tehlikeli bir durum, güvende kal.",
            "Panik yapma, güvenli bir yerde bekle.",
            "Haberleri dinle ve talimatlara uy."
        ],
        "songs": [
            {"artist": "Muse", "title": "Hysteria", "url": "https://music.youtube.com/watch?v=3dm_5qWWDV8"},
            {"artist": "Rage Against the Machine", "title": "Bulls on Parade", "url": "https://music.youtube.com/watch?v=3L4YrGaR8E4"},
            {"artist": "Nine Inch Nails", "title": "The Hand That Feeds", "url": "https://music.youtube.com/watch?v=q1bGqYh8aKM"}
        ]
    }
}

# --- VERİ BİRLEŞTİRME ---
# Artık döngü yerine doğrudan update metodunu kullanıyoruz.
FULL_WEATHER_DATA.update(EXTRA_CATEGORIES)

def get_weather_data(condition):
    """
    Verilen hava durumu (condition) için veri döndürür.
    Eğer condition listede yoksa varsayılan olarak 'Clear' döndürür.
    """
    # Burada bir sorun yok, doğru kullanım.
    return FULL_WEATHER_DATA.get(condition, FULL_WEATHER_DATA.get("Clear"))