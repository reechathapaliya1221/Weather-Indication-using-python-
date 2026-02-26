from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()  # Get the selected city from combobox
    if not city:  # Check if a city is selected
        w_label1.config(text="Please select a city")
        return

    api_key = "d64667b488ad139a996460393854881e"

    try:
        # Fixed the URL construction
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        data = requests.get(url).json()

        # Update labels with weather data
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["weather"][0]["description"])

        # Convert Kelvin to Celsius and format to 2 decimal places
        temp_celsius = data["main"]["temp"] - 273.15
        temp_label1.config(text=f"{temp_celsius:.2f}°C")

        per_label1.config(text=f"{data['main']['pressure']} hPa")
        hum_label1.config(text=f"{data['main']['humidity']}%")

    except KeyError as e:
        # Handle API errors (like city not found)
        error_msg = data.get("message", "Error fetching data")
        w_label1.config(text=f"Error: {error_msg}")
    except Exception as e:
        w_label1.config(text="Connection Error")


win = Tk()
win.title("Weather indication")
win.config(background="white")
win.geometry("500x650")  # Increased height to accommodate all labels

# Title
title_label = Label(win, text="Weather App",
                    font=("Times New Roman", 20, "bold"),
                    bg="white")
title_label.place(x=120, y=20, height=40, width=250)

# District List
nepal_disricts = [
    "Bhojpur", "Dhankuta", "Ilam", "Jhapa", "Khotang", "Morang",
    "Okhaldhunga", "Panchthar", "Sankhuwasabha", "Solukhumbu",
    "Sunsari", "Taplejung", "Terhathum", "Udayapur",
    "Bara", "Dhanusha", "Mahottari", "Parsa", "Rautahat",
    "Saptari", "Sarlahi", "Siraha",
    "Bhaktapur", "Chitwan", "Dhading", "Dolakha", "Kathmandu",
    "Kavrepalanchok", "Lalitpur", "Makwanpur", "Nuwakot",
    "Ramechhap", "Rasuwa", "Sindhuli", "Sindhupalchok",
    "Arghakhanchi", "Banke", "Bardiya", "Dang", "Eastern Rukum",
    "Gulmi", "Kapilvastu", "Parasi", "Palpa", "Pyuthan",
    "Rolpa", "Rupandehi",
    "Baglung", "Gorkha", "Kaski", "Lamjung", "Manang",
    "Mustang", "Myagdi", "Nawalpur", "Parbat", "Syangja",
    "Tanahun",
    "Dailekh", "Dolpa", "Humla", "Jajarkot", "Jumla",
    "Kalikot", "Mugu", "Salyan", "Surkhet", "Western Rukum",
    "Achham", "Baitadi", "Bajhang", "Bajura", "Dadeldhura",
    "Darchula", "Doti", "Kailali", "Kanchanpur"
]

# Combobox
city_name = StringVar()
com = ttk.Combobox(win,
                   values=nepal_disricts,
                   font=("Times New Roman", 12),
                   textvariable=city_name)
com.place(x=100, y=100, height=35, width=300)
com.set("Select a district")  # Set default text

# Done Button - Fixed: removed () from command
done_button = Button(win,
                     text="Get Weather",
                     font=("Times New Roman", 16, "bold"),
                     bg="green",
                     fg="white",
                     command=data_get)  # Don't put parentheses here
done_button.place(x=150, y=160, height=45, width=200)

# Weather Climate Label
w_label = Label(win, text="Weather Climate:",
                font=("Times New Roman", 16))
w_label.place(x=25, y=220, height=40, width=150)

w_label1 = Label(win, text="",
                 font=("Times New Roman", 16),
                 bg="lightgray", relief=SUNKEN)
w_label1.place(x=180, y=220, height=40, width=280)

# Weather Description Label
wb_label = Label(win, text="Description:",
                 font=("Times New Roman", 16))
wb_label.place(x=25, y=270, height=40, width=150)

wb_label1 = Label(win, text="",
                  font=("Times New Roman", 16),
                  bg="lightgray", relief=SUNKEN)
wb_label1.place(x=180, y=270, height=40, width=280)

# Temperature Label
temp_label = Label(win, text="Temperature:",
                   font=("Times New Roman", 16))
temp_label.place(x=25, y=320, height=40, width=150)

temp_label1 = Label(win, text="",
                    font=("Times New Roman", 16),
                    bg="lightgray", relief=SUNKEN)
temp_label1.place(x=180, y=320, height=40, width=280)

# Pressure Label
per_label = Label(win, text="Pressure:",
                  font=("Times New Roman", 16))
per_label.place(x=25, y=370, height=40, width=150)

per_label1 = Label(win, text="",
                   font=("Times New Roman", 16),
                   bg="lightgray", relief=SUNKEN)
per_label1.place(x=180, y=370, height=40, width=280)

# Humidity Label
hum_label = Label(win, text="Humidity:",
                  font=("Times New Roman", 16))
hum_label.place(x=25, y=420, height=40, width=150)

hum_label1 = Label(win, text="",
                   font=("Times New Roman", 16),
                   bg="lightgray", relief=SUNKEN)
hum_label1.place(x=180, y=420, height=40, width=280)

# Additional info or status
status_label = Label(win, text="Select a district and click 'Get Weather'",
                     font=("Times New Roman", 12),
                     bg="white", fg="blue")
status_label.place(x=100, y=480, height=30, width=300)

win.mainloop()