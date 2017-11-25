import requests
import datetime
import time

# global vars for easy change
longitude = 5.387827
latitude = 52.156111 
request = "https://api.darksky.net/forecast/{}/{},{}?units=si"
time_machine = "https://api.darksky.net/forecast/{}/{},{},{}?units=si" 
with open("secret_key.txt") as secret_key_file:
    secret_key = secret_key_file.read().replace("\n", "").replace("\r", "")
unixtime = int(time.time())

now = datetime.datetime.now()
today_date = now.strftime("%A %d-%m-%Y") 

response = requests.get(request.format(secret_key, latitude, longitude))
forecast = response.json()

print("Today is "+today_date+". The forecast for today is: ")
print(forecast["currently"]["summary"])
print(" -"*int(len(forecast["currently"]["summary"])/2))

for num in range(unixtime, unixtime+604800, 86400):
    time_response = requests.get(time_machine.format(secret_key, latitude, longitude, num))
    future = time_response.json()
    day = datetime.datetime.fromtimestamp(num).strftime("%A")
    print("{}: {}".format(day, future["currently"]["summary"]))

