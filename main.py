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
# round unixtime to the next hour
unixtime_rounded = unixtime // 3600 * 3600 + 3600
now = datetime.datetime.now()
now_time = int(now.strftime("%H")) + 1
today_date = now.strftime("%A %d-%m-%Y") 

print("Available commands: summary_week, rain_today.")
command = str(input("Command: "))

if command == "summary_week":
    response = requests.get(request.format(secret_key, latitude, longitude))
    forecast = response.json()

    print("\nToday is "+today_date+". The forecast for today is: ")
    print(forecast["currently"]["summary"])
    print(" -"*int(len(forecast["currently"]["summary"])/2))

    for num in range(unixtime+86400, unixtime+604800, 86400):
        time_response = requests.get(time_machine.format(secret_key, latitude, longitude, num))
        future = time_response.json()
        day = datetime.datetime.fromtimestamp(num).strftime("%A")
        print("{}: {}".format(day, future["currently"]["summary"]))
elif command == "rain_today":
    print("\nToday is "+today_date+". The rain-forecast for today is: ")
    hours_left = 24 - now_time
    print(now_time)
    for num in range(hours_left, 24, 3600):
        hour_response = requests.get(time_machine.format(secret_key, latitude, longitude, num))


