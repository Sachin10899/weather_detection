from tkinter import * # Importing tkinter library
from tkinter import tk # Importing messagebox from tkinter library
import requests


 
# Weather App
# API: https://openweathermap.org/
# API key: 8a4cf8734ac2d1c6cdd8a5b283d51c04


def data_get():
        city = city_name.get()
        weather_api_URL = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8a4cf8734ac2d1c6cdd8a5b283d51c04"
        data = requests.get(weather_api_URL).json()
        try:
            weather_label1.config(text=data['weather'][0]['main'])
        except KeyError:
            weather_label1.config(text="Weather data not available")
        description_label1.config(text=data['weather'][0]['description'])
        temperatur_labe1.config(text=str(int(data['main']['temp']-273.15))+"°C")
        pressure_label1.config(text=str(data['main']['pressure']))



win = Tk() # Creating a window
win.title("Welcome to my City") # Title of the window
win.configure(bg="light blue") # Background color of the window
win.geometry("500x550") # Size of the window


# Creating a label
name_label = Label(win, text="Weather App",  
                   font=("Time New Roman", 30 ,"bold" ))
name_label.place(x=25,y=50,height=50,width=450)

# Creating a combobox
city_name = StringVar()
list_name= ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = tk.Combobox(win, text="Weather App", values= list_name,
                   font=("Time New Roman", 20 ), textvariable=city_name)
com.place(x=35,y=120,height=50,width=420)

# Creating a label
weather_label = Label(win, text="Weather Climate",  
                   font=("Time New Roman", 19 ))
weather_label.place(x=25,y=270,height=50,width=200)

weather_label1 = Label(win, text="",  
                   font=("Time New Roman", 19 ))
weather_label1.place(x=250,y=270,height=50,width=220)

description_label = Label(win, text="Weather Description",  
                   font=("Time New Roman", 16 ))
description_label.place(x=25,y=340,height=50,width=200)

description_label1 = Label(win, text="",  
                   font=("Time New Roman", 16 ))
description_label1.place(x=250,y=340,height=50,width=220)

temperatur_label = Label(win, text="Weather Temperatur",  
                   font=("Time New Roman", 16 ))
temperatur_label.place(x=25,y=410,height=50,width=200)

temperatur_labe1 = Label(win, text="",  
                   font=("Time New Roman", 16 ))
temperatur_labe1.place(x=250,y=410,height=50,width=220)

pressure_label = Label(win, text="Weather Pressure",  
                   font=("Time New Roman", 18 ))
pressure_label.place(x=25,y=480,height=50,width=200)

pressure_label1 = Label(win, text="",  
                   font=("Time New Roman", 18 ))
pressure_label1.place(x=250,y=480,height=50,width=220)

done_button = Button(win, text="Done", bg="light green", fg="black",
                     font=("Time New Roman", 20 ), command=data_get)
done_button.place(x=200,y=190,height=50,width=100)


win.mainloop() # Running the window
