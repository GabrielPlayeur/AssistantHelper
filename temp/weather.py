# importing requests and json
import requests

class requestWeatherApi:
   def __init__(self, API_KEY):
      self.API_KEY = API_KEY

      self.URL_BASE = f"https://api.openweathermap.org/data/2.5/weather?"

      self.lastCity = {}

      self.printInfoWeather()

   def sendRequest(self, city) -> None:
      url = f"{self.URL_BASE}q={city}&appid={self.API_KEY}"
      reponse = requests.get(url)
      if self._checkRequestStatus(reponse):
         self.lastCity = self._makeRequestJson(reponse)
         self.printInfoWeather()
      else:
         print("Error in the request.",reponse.status_code)

   def _makeRequestJson(self, reponse) -> dict:
      data = reponse.json()
      main = data['main']
      return {"city":data["name"],"temp":round(main['temp']-273.15,2),"humidity":main['humidity'],"pressure":main['pressure'],"weather_report":data['weather'][0]['description']}

   def printInfoWeather(self) -> None:
      if self.lastCity.get("temp") is not None:
         print(f"{self.lastCity['city']:-^50}\n\tTemperature: {self.lastCity['temp']}°\n\tHumidity: {self.lastCity['humidity']}%\n\tPressure: {self.lastCity['pressure']}Pa\n\tWeather Report: {self.lastCity['weather_report']}\n{'':-^50}")
      else:
         print(f"{'':-^50}\n\tNo city entered\n{'':-^50}")

   def _checkRequestStatus(self, reponse) -> bool:
      if reponse.status_code == 200:
         return True
      else:
         return False

API_KEY = "513cf5bef2bd3c00f2b188521ba509d9"
CITY = "Sevremoine"
weather = requestWeatherApi(API_KEY)
weather.sendRequest(CITY)