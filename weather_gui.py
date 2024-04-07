# Weather App! by Kunal dharpure

import tkinter as tk
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    api_key = "017dc23f15e96f7cc6e86c85ea6d8daf" 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url).json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=f"{int(data['main']['temp'] - 273.15)}°C")
    wp_label1.config(text=f"{data['main']['pressure']} hPa")

def on_enter(event):
    done_button.config(bg='purple', fg='white')

def on_leave(event):
    done_button.config(bg='green', fg='black')


win = tk.Tk()
win.configure(bg="lightblue")
win.title("Weather App")
img = tk.PhotoImage(file="cloudy.png")
win.iconphoto(win, img)

# Set window size and position
window_width = 500
window_height = 570

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_coordinate = (screen_width // 2) - (window_width // 2)
y_coordinate = (screen_height // 2) - (window_height // 2)

# Set the window geometry to be centered on the screen
win.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")


# Header Label
header_label = tk.Label(win, text="Weather App!", font=("Georgia", 30, "bold"), fg="green", bg="lightblue")
header_label.place(x=25, y=20, width=450)

# City Selection Dropdown
list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
             "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
             "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
             "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
             "Delhi", "Puducherry"]

city_name = tk.StringVar()
city_combobox = ttk.Combobox(win, values=list_name, font=("Comic sans MS", 14), textvariable=city_name)
city_combobox.place(x=25, y=80, width=450, height=50)

# Weather Details Labels
labels_info = [("Weather Climate:", 260), ("Weather Description:", 330), ("Temperature:", 400), ("Pressure:", 470)]

for label_text, y_coord in labels_info:
    label = tk.Label(win, text=label_text, font=("Comic sans MS", 15, "bold"), bg="lightblue")
    label.place(x=25, y=y_coord, width=210)

    info_label = tk.Label(win, text="", font=("Comic sans MS", 14, "bold"), fg="purple", bg="lightblue")
    info_label.place(x=250, y=y_coord, width=210)

    if label_text == "Temperature:":
        wt_label1 = info_label
    elif label_text == "Weather Climate:":
        w_label1 = info_label
    elif label_text == "Weather Description:":
        wb_label1 = info_label
    elif label_text == "Pressure:":
        wp_label1 = info_label

# Button to Get Weather Data
done_button = tk.Button(win, text="Get Weather", font=("Georgia", 13, "bold"), bg="green", command=data_get)
done_button.place(x=200, y=150, width=130)

# Bind events to handle hover effect
done_button.bind("<Enter>", on_enter)
done_button.bind("<Leave>", on_leave)


win.mainloop()
