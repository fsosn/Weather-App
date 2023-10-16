import tkinter as tk
from tkinter import ttk, PhotoImage, Canvas, Scrollbar
import sys
from fetch import *

def on_canvas_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

if len(sys.argv) < 2 or len(sys.argv[1]) == 0:
    print("Usage: python app.py api_key [language]")
    raise ValueError("Invalid or missing API key.")

API = sys.argv[1]
LANGUAGE = sys.argv[2] if len(sys.argv) == 3 else 'en-us'

root = tk.Tk()
root.title("Weather Forecast App")

icon_image = PhotoImage(file="images/app_icon.png")
root.iconphoto(True, icon_image)

style = ttk.Style()
style.configure("TButton", padding=(10, 5), font=('Helvetica', 10))

left_frame = ttk.Frame(root, padding="20")
left_frame.grid(row=0, column=0, sticky="ns")

city_label = ttk.Label(left_frame, text="Enter the city:")
city_label.grid(row=0, column=0, padx=(10, 5), sticky="w")

city_entry = ttk.Entry(left_frame, width=30)
city_entry.grid(row=0, column=1, padx=(0, 10), sticky="ew")

current_conditions_button = ttk.Button(left_frame, text="Current conditions", command=lambda: fetch_current_conditions(API, city_entry, weather_display, LANGUAGE))
current_conditions_button.grid(row=1, column=0, columnspan=2, pady=(10, 5), sticky="ew")

hourly_forecast_button = ttk.Button(left_frame, text="Next 12 hours", command=lambda: fetch_twelve_hour_forecast(API, city_entry, weather_display, LANGUAGE))
hourly_forecast_button.grid(row=2, column=0, columnspan=2, pady=(0, 5), sticky="ew")

forecast_button = ttk.Button(left_frame, text="Tomorrow", command=lambda: fetch_tomorrows_forecast(API, city_entry, weather_display, LANGUAGE))
forecast_button.grid(row=3, column=0, columnspan=2, pady=(0, 5), sticky="ew")

daily_forecast_button = ttk.Button(left_frame, text="5-day Forecast", command=lambda: fetch_five_day_forecast(API, city_entry, weather_display, LANGUAGE))
daily_forecast_button.grid(row=4, column=0, columnspan=2, pady=(0, 5), sticky="ew")

right_frame = ttk.Frame(root, padding="20")
right_frame.grid(row=0, column=1, sticky="nsew")

weather_display_label = ttk.Label(right_frame, text="Weather Information:")
weather_display_label.grid(row=0, column=0, padx=(10, 5), sticky="w")

canvas = Canvas(right_frame, height=300, width=400)
canvas.grid(row=1, column=0, sticky="nsew")

frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

scrollbar = Scrollbar(right_frame, orient="vertical", command=canvas.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
canvas.configure(yscrollcommand=scrollbar.set)

weather_display = ttk.Label(frame, text="", justify="left", padding=(10, 10))
weather_display.grid(row=0, column=0, sticky="ew")

frame.bind("<Configure>", on_canvas_configure)

root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
