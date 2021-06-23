import requests
from datetime import datetime
api_key = "6985052d532342aa76695fc595241323"
location = input("enter the city name:")
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()
temp_city = ((api_data['main']['temp']) - 273.15)
weather = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
str_hmdt = str(hmdt)
wind_spd = api_data['wind']['speed']
str_wind = str(wind_spd)
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
with open("myfile.txt","w") as file:
    file.write(".................................................\n ")
    file.write("weather stats for - {} || {}\n".format(location.upper(),date_time))
    file.write("..................................................\n")
    file.write("current temperature is : {:.2f} deg c\n".format(temp_city))
    file.write("current weather desc : " + weather )
    file.write("\ncurrent humidity : " + str_hmdt )
    file.write("\ncurrent wind speed:" + str_wind)



