import tkinter as tk
import random
import pygame

from datetime import date
from PIL import Image, ImageTk

# ------------------ CREATING VARIABLE CALLED QUOTES -----------------

with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

# ------------------ DEF HAE_PAIVAN_QUOTE -----------------

# hakee päivän quoten
def hae_paivan_quote():
    today = str(date.today())
    try:
        with open("daily_quote.txt", "r", encoding="utf-8") as f:
            saved_date, saved_quote = f.read().split("|", 1)
        if saved_date == today:
            return saved_quote
    except FileNotFoundError:
        pass

    new_quote = random.choice(quotes)
    with open("daily_quote.txt", "w", encoding="utf-8") as f:
        f.write(f"{today}|{new_quote}")
    return new_quote

# ------------------ WINDOW ------------------

window = tk.Tk()
window.geometry("700x600")

# ------------------ BACKGROUND PHOTO ------------------

bg_image = Image.open("background.jpg")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = tk.Label(window, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ------------------ BUTTON ------------------

button = tk.Button(window, text="KOALA FACT OF THE DAY", command=lambda: label.config(text=hae_paivan_quote()))
button.place(relx=0.5, rely=0.4, anchor="center")

# ------------------ LABEL ------------------

# prints label/quote
label = tk.Label(window, text="", font=("Arial", 12), bg=None)
label.place(relx=0.5, rely=0.5, anchor="center")

# ------------------ MUSIC ------------------

pygame.mixer.init()
pygame.mixer.music.load("tausta.mp3")
pygame.mixer.music.play(-1)

# ------------------ RUN -----------------

# run
window.mainloop()
