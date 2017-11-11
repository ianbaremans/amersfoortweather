import requests
import datetime

# global vars for easy change
locationlong = 5.387827
locationlat = 52.156111 
base_url = "https://api.darksky.net/forecast/{}/{},{}?units=si&exclude="
with open("secret_key.txt") as secret_key_file:
    secret_key = secret_key_file.read().replace("\n", "").replace("\r", "")

now = datetime.datetime.now()
today_date = now.strftime("%A %d-%m-%Y") 

response = requests.get(base_url.format(secret_key, locationlat, locationlong))
forecast = response.json()
print(today_date)
print(forecast["daily"]["summary"])

