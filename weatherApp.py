import tkinter as tk 
import requests
import time
import pprintpp

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6f925ade4ec98875b91af57b6363cd03"
    
    json_data = requests.get(api).json()   #fetching api data

    # Exception handling whether data is fetched or not
    try : 
        condition = json_data["weather"][0]['main']
        try:
            condition = json_data["weather"][0]['main']
        except:
            pass
        # Extracting data from the api which is of our use 
        temp = int(json_data["main"]["temp"] - 273.15)
        min_temp = int(json_data["main"]["temp_min"] - 273.15)
        max_temp = int(json_data["main"]["temp_max"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
        sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] - json_data['timezone']))
        sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] - json_data['timezone']))

        final_info = condition + "\n" + str(temp) + "°C"
        final_data = "\n"+ "Max Temp : " + str(max_temp)+ "°C" + "\n" + "Min temp : " + str(min_temp)+ "°C" + "\n" + "Pressure : " + str(pressure) + "\n" + "Humidity : " + str(humidity) + "\n" + "Wind : " + str(wind) + "\n" + "Sunrise : " + str(sunrise)+ "AM" + "\n" + "Sunset : " + str(sunset)+ "PM" + "\n\n" 
        label1.config(text = final_info)
        label2.config(text = final_data)
    except KeyError:
        label1.config(text = "City not found")
        label2.config(text = " ")

canvas  = tk.Tk()
canvas.geometry("500x400")
canvas.title("Weather App by Md Arif")

f = ("Terminal",15,"bold")
t = ("Terminal",35,"bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20, padx = 20)
textfield.focus()
textfield.bind('<Return>',getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()


canvas.mainloop()


