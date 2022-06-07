import requests

API_KEY="3cc778ffefe86bc2e5ed9ccc5e32ba69"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

city=input("Enter a city name: ")

request_url= f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(request_url)

if response.status_code == 200:
    data=response.json()
    weather=data['weather'][0]['main']
    temp=round(data['main']['temp']-272.15,2)
    print(("The Weather is: {}\nThe temperature is: {} Celsius").format(weather,temp))
else:
    print("An error occured.")