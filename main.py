# main.py
import tkinter as tk
from ui.main_window import WeatherMusicApp

def main():
    # Ana Tkinter penceresini oluştur
    root = tk.Tk()
    
    # Uygulamayı başlat
    app = WeatherMusicApp(root)
    
    # Pencereyi ekranda tut
    root.mainloop()

if __name__ == "__main__":
    main()