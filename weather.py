from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
from tkinter import font#for wrong inputs 
import requests #for api 

api_key='22ba790184f9d6388bbf21900d8b9d5c'
def getweather(city):
    weather_data=requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    # f string because the expressions delimited by curly braces {}
    if weather_data:
        json_output=weather_data.json()
        city=json_output['name']
        country=json_output['sys']['country']
        weather=json_output['weather']
        wind_speed=json_output['wind']
        temp=json_output['main']['temp']
        output=(city,country,weather,wind_speed,temp)
        return output
    else:
        return None
    
def printer():
    city = searchcity.get()
    weather=getweather(city)
    if weather:
        enteredloc['text'] = '{}, {}'.format(weather[0],weather[1])
        temperature['text']= '{:.2f} K,'.format(weather[4])
        weatheroutput['text']=weather[2]
        
    else:
        messagebox.showerror("raey, Incorrect city")
    
    



root = Tk() #intialize tkinter
root.title("let me tell you the weather")
root.config(background="maroon")
root.geometry("1000x700")
fonta=("calibri",40,"bold")
searchcity=StringVar()
givencity= Entry(root,textvariable=searchcity,bd=5,font=fonta)
givencity.pack()


searchbutton=Button(root,text="search",font=fonta,bg="blue",command=printer)
searchbutton.pack()

enteredloc=Label(root,text='',font=fonta,bg="maroon")
enteredloc.pack()

temperature=Label(root,text='',font=fonta,bg="maroon")
temperature.pack()

weatheroutput=Label(root,text='',font=fonta,bg="maroon")
weatheroutput.pack()

root.mainloop()
