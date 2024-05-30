import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
# from datetime import datetime
import requests
import pytz

def get_weather():
    pass

root = tk.Tk() # قرار دادیم root در متغییر tk یک شیع از کلاس 
root.title("Weather App")
root.geometry("800x450+300+200") # عرضxطول از بیرون+عرض از بیرون+طول
# root.resizable(False, False) # باعث می شه سایز پنجره تغییر نکنه
root.config(bg="white")


# search box
search_img = tk.PhotoImage(file="searchblack.png") # عکسو می خونیم
search_img_lable = tk.Label(root, image=search_img, border=0) #عکسو تبدیل به لیبل کردیم
search_img_lable.pack(pady=15, side=tk.TOP)
text_box = tk.Entry(root, justify="center", width=15, font=("poppins", 25), bg="black", fg="white", border=0)  # محدوده نوشتن شهر ها
text_box.place(x = 254, y = 28)


search_icon = tk.PhotoImage(file="untitled1.png")
search_icon_buttun = tk.Button(root, image=search_icon,border=0, cursor="hand2", bg="black", command = get_weather)
search_icon_buttun.place(x = 532, y=32)


# logo

logo_img = tk.PhotoImage(master=root, file="sun.png")
logo_label = tk.Label(root, image=logo_img, border=0)
logo_label.pack(side=tk.TOP)

# bottom box:
bottom_img = tk.PhotoImage(master=root, file="Untitled.png")
bottom_label = tk.Label(root, image=bottom_img, border=0)
bottom_label.pack(side=tk.BOTTOM)

# City Name:
city_label = tk.Label(root, font = ("arial", 40), fg = "#e355cd")
city_label.place(x=120, y=160)

# Time:
time_label = tk.Label(root, font = ("arial", 20), fg = "#e355cd")
time_label.place(x=120, y=230)

clock = tk.Label(root, font = ("arial", 20), fg = "#e355cd")
clock.place(x=120, y=270)

# Labels:
label1 = tk.Label(root, text="WIND", font=("Helvetica", 15))
root.mainloop()