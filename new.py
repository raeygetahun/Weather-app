import requests
api_key='22ba790184f9d6388bbf21900d8b9d5c'   
inp=input("city: ")
weather_data=requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={inp}&appid={api_key}")
print(weather_data.json())