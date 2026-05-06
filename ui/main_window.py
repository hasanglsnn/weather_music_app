# ui/main_window.py
import sys
import os
import customtkinter as ctk
import threading
import webbrowser
from PIL import Image, ImageOps, ImageDraw, ImageFont

from services.location_service import get_current_location
from services.weather_service import get_weather_by_coords
from services.music_service import get_recommendations
import config

def resource_path(relative_path):
    """ PyInstaller ile oluşturulan exe için dosya yolunu bulur """
    try:
        # PyInstaller geçici klasörü
        base_path = sys._MEIPASS
    except Exception:
        # Normal çalışma ortamı
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Tema ayarları
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

PLACEHOLDER_COLOR = "#444950"

class WeatherMusicApp(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title(config.APP_TITLE)
        self.master.geometry(config.WINDOW_SIZE)
        self.master.resizable(False, False)
        self.pack(fill="both", expand=True)
        self.configure(fg_color="#18191E")

        # Bulunduğun dosyanın yolu ve assets için mutlak yol hazırla
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        # 'assets' klasörü artık resource_path ile alınmalı
        self.assets_dir = resource_path(os.path.join(os.path.dirname(__file__), 'assets'))

        self.current_urls = ["", "", ""]
        self.loading = False

        self.create_widgets()
        self.async_refresh_data()

    def create_widgets(self):
        # --- KART ALANINI GENİŞLETTİK ---
        self.card = ctk.CTkFrame(self, corner_radius=28, fg_color="#23242B", width=760, height=540)
        self.card.place(relx=0.5, rely=0.5, anchor="center")

        # --- YENİLE BUTONU: SAĞ ÜSTTE, SADECE İKON ---
        self.btn_refresh = ctk.CTkButton(
            self.card,
            text="",
            image=self._get_refresh_icon(20, 20),
            width=44,
            height=44,
            fg_color="#1ed760",
            hover_color="#23bb55",
            corner_radius=22,
            command=self.async_refresh_data
        )
        self.btn_refresh.place(x=706, y=26)  # Kenara yakın, üstte

        # Başlık (şehir ismi)
        self.lbl_city = ctk.CTkLabel(
            self.card,
            text="Konum Aranıyor...",
            font=("Montserrat", 32, "bold"),
            text_color="#FFFFFF",
        )
        self.lbl_city.grid(row=0, column=0, columnspan=2, sticky="w", padx=44, pady=(38, 7))

        # --- HAVA DURUMU KARTI ---
        self.weather_block = ctk.CTkFrame(self.card, fg_color="#24262e", corner_radius=22)
        self.weather_block.grid(row=1, column=0, sticky="nsew", padx=(44,18), pady=(10, 0), ipadx=0, ipady=0)

        self.icon_area = ctk.CTkFrame(self.weather_block, fg_color="transparent")
        self.icon_area.grid(row=0, column=0, padx=(26,7), pady=17, sticky="nsw")
        self.lbl_icon = ctk.CTkLabel(self.icon_area, text="")
        self.lbl_icon.pack()

        self.temp_block = ctk.CTkFrame(self.weather_block, fg_color="transparent")
        self.temp_block.grid(row=0, column=1, padx=(0,26), pady=(8, 14), sticky="w")
        self.lbl_temp = ctk.CTkLabel(
            self.temp_block,
            text="--°C",
            font=("Montserrat", 40, "bold"),
            text_color="#fcb044"
        )
        self.lbl_temp.pack(anchor="w", pady=(0, 2))
        self.lbl_desc = ctk.CTkLabel(
            self.temp_block,
            text="Hava Durumu bekleniyor...",
            font=("Montserrat", 16, "normal"),
            text_color="#bbbbbb"
        )
        self.lbl_desc.pack(anchor="w", pady=(4,0))

        self.lbl_loading = ctk.CTkLabel(
            self.weather_block, text="", font=("Montserrat", 14, "italic"), text_color="#9ca0b3"
        )
        self.lbl_loading.grid(row=1, column=0, columnspan=2, sticky="w", padx=7, pady=(7,1))

        # --- Günün SÖZÜ ---
        self.quote_card = ctk.CTkFrame(self.card, fg_color="#18191E", corner_radius=20)
        self.quote_card.grid(row=1, column=1, sticky="nsew", padx=(18,44), pady=(10,0))
        self.lbl_quote = ctk.CTkLabel(
            self.quote_card, text="", font=("Georgia", 16, "italic"),
            wraplength=318, text_color="#C7DFCE", anchor="w", justify="left"
        )
        self.lbl_quote.pack(padx=22, pady=26, anchor="w")

        # Ayırıcı çizgi
        self.sep = ctk.CTkFrame(self.card, height=2, fg_color="#353640")
        self.sep.grid(row=2, column=0, columnspan=2, pady=(30,10), padx=44, sticky="ew")

        # --- ŞARKI BAŞLIK ---
        self.lbl_songs = ctk.CTkLabel(
            self.card, text="🎵 Senin İçin Seçtiklerimiz",
            font=("Montserrat", 15, "bold"),
            text_color="#1ed760"
        )
        self.lbl_songs.grid(row=3, column=0, columnspan=2, sticky="w", padx=44, pady=(3,0))

        # --- ŞARKI LİSTESİ (yeni grid + spacing) ---
        self.songs_frame = ctk.CTkFrame(self.card, fg_color="#212224", corner_radius=16)
        self.songs_frame.grid(row=4, column=0, columnspan=2, padx=44, pady=(16,18), sticky="ew")
        self.song_buttons = []
        for i in range(3):
            btn = ctk.CTkButton(
                self.songs_frame,
                text=f"Şarkı {i+1}",
                width=440,
                height=49,
                fg_color="#181a1e",
                hover_color="#283345",
                font=("Montserrat", 14, "bold"),
                corner_radius=20,
                command=lambda x=i: self.open_link(x),
                anchor="w",
                text_color="#fff",
                cursor="hand2",
                state="disabled"
            )
            btn.grid(row=i, column=0, sticky="ew", pady=(8, 8), padx=14)
            self.song_buttons.append(btn)

        # Grid/stretch ayarları (büyümeye uygun ve ferah alan)
        self.card.grid_columnconfigure(0, weight=2)
        self.card.grid_columnconfigure(1, weight=1)
        self.card.grid_rowconfigure(1, weight=2)
        self.card.grid_rowconfigure(4, weight=1)
        self.songs_frame.grid_columnconfigure(0, weight=1)
        self.card.grid_rowconfigure(1, weight=2)

    # ---- Threading & Loading ----
    def async_refresh_data(self):
        if self.loading:
            return
        self.set_loading(True)
        threading.Thread(target=self.refresh_data, daemon=True).start()

    def set_loading(self, state=True):
        self.loading = state
        if state:
            self.lbl_city.configure(text="Yükleniyor...")
            self.lbl_loading.configure(text="Veriler API'den çekiliyor, lütfen bekleyin.")
            self.btn_refresh.configure(state="disabled")
            [btn.configure(state="disabled") for btn in self.song_buttons]
        else:
            self.lbl_loading.configure(text="")
            self.btn_refresh.configure(state="normal")

    def refresh_data(self):
        try:
            loc_data = get_current_location()
            if not loc_data['success']:
                self._handle_error("Konum Bulunamadı: {}".format(loc_data.get('error')), konum=True)
                return

            weather_data = get_weather_by_coords(loc_data['lat'], loc_data['lon'])
            if not weather_data['success']:
                if "401" in str(weather_data.get("error")):
                    self._handle_error(
                        "API Anahtarı henüz aktifleşmedi.\nLütfen 5-10 dakika sonra tekrar deneyin.",
                        api=True)
                    return
                else:
                    self._handle_error("Hava Durumu Alınamadı: " + str(weather_data.get('error')))
                    return
            content = get_recommendations(weather_data['main_condition'])
            self.master.after(0, lambda: self.update_ui(loc_data, weather_data, content))

        except Exception as e:
            self._handle_error("Bilinmeyen Hata: " + str(e))
        finally:
            self.master.after(0, lambda: self.set_loading(False))

    def _handle_error(self, msg, konum=False, api=False):
        def _show():
            # Mesaj kutusu yok: CustomTkinter popup yoksa label'ı güncelle
            if api:
                self.lbl_loading.configure(text=msg)
                self.lbl_city.configure(text="API Aktifleşiyor...")
            elif konum:
                self.lbl_loading.configure(text=msg)
                self.lbl_city.configure(text="Konum Hatası")
            else:
                self.lbl_loading.configure(text=msg)
        self.master.after(0, _show)

    # ---- UI Güncelleme ----
    def update_ui(self, loc, weather, content):
        self.lbl_city.configure(text=f"{loc['city']}")
        self.lbl_temp.configure(text=f"{weather['temp']}°C")
        self.lbl_desc.configure(text=f"{weather['main_condition']} - {weather['description'].title()}")
        self.lbl_quote.configure(text=f'"{content.get("quote","")}"')
        # İkon (placeholder: şık bir soru işareti ?)
        icon_name = content.get('icon', None)
        icon_img = self._load_icon(icon_name)
        if icon_img:
            self.lbl_icon.configure(image=icon_img, text="")
            self.lbl_icon.image = icon_img
        else:
            pl_img = self._draw_question_placeholder_img(150, 150)
            self.lbl_icon.configure(image=pl_img, text="")
            self.lbl_icon.image = pl_img
        # Şarkı butonları
        songs = content.get('songs', [])
        for i, btn in enumerate(self.song_buttons):
            if i < len(songs):
                song = songs[i]
                btn.configure(text=f"{song['artist']} - {song['title']}", state="normal")
                self.current_urls[i] = song['url']
            else:
                btn.configure(text="...", state="disabled")
                self.current_urls[i] = ""

        self.set_loading(False)

    # ---- Yardımcı: Şarkı aç ----
    def open_link(self, index):
        url = self.current_urls[index]
        if url:
            webbrowser.open(url)

    # ---- Yardımcı: Icon ve Placeholder Methods ----
    def _load_icon(self, icon_name):
        if not icon_name:
            return None
        # Mutlak path ile asset yeri
        # icon_path = os.path.join(self.assets_dir, icon_name)
        icon_path = resource_path(os.path.join('ui', 'assets', icon_name))
        try:
            if not os.path.exists(icon_path):
                return None
            img = Image.open(icon_path).convert("RGBA")
            img = img.resize((150, 150), Image.LANCZOS)
            img = ImageOps.expand(img, border=2, fill="#23242B")
            # CTkImage ile oluştur
            ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(150, 150))
            return ctk_img
        except Exception:
            return None

    def _draw_question_placeholder_img(self, w, h):
        # Gri yuvarlak kutuda büyük bir '?' karakteri
        img = Image.new("RGBA", (w, h), PLACEHOLDER_COLOR)
        mask = Image.new("L", (w, h), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([0,0,w,h], radius=int(min(w, h)*0.36), fill=255)
        img.putalpha(mask)
        # Soru işareti
        draw_q = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", size=int(h*0.56))
        except:
            font = ImageFont.load_default()  # Sistem font fallback
        text = "?"
        bbox = draw_q.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x = (w - tw) // 2
        y = (h - th) // 2
        draw_q.text((x, y-3), text, fill="#E7E7E7", font=font)
        return ctk.CTkImage(light_image=img, dark_image=img, size=(w, h))

    def _get_refresh_icon(self, w, h):
        # Unicode "🔄" görselini PIL ile hazırlayalım ve CTkImage ile döndür
        img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", int(w*0.95))
        except:
            font = ImageFont.load_default()
        text = u"\U0001F504"  # 🔄 unicode
        bbox = draw.textbbox((0, 0), text, font=font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        draw.text(((w-tw)//2, (h-th)//2-3), text, fill="#232B1E", font=font)
        return ctk.CTkImage(light_image=img, dark_image=img, size=(w, h))

if __name__ == "__main__":
    root = ctk.CTk()
    app = WeatherMusicApp(root)
    root.mainloop()