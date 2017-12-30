import requests
import datetime
import time

longitude = 5.387827
latitude = 52.156111 
request = "https://api.darksky.net/forecast/{}/{},{}?units=si"
time_machine = "https://api.darksky.net/forecast/{}/{},{},{}?units=si" 
with open("secret_key.txt") as secret_key_file:
    secret_key = secret_key_file.read().replace("\n", "").replace("\r", "")

unixtime = int(time.time())
unixtime_rounded = unixtime // 3600 * 3600 + 3600
now = datetime.datetime.now()
now_time = int(now.strftime("%H")) + 1
today_date = now.strftime("%A %d-%m-%Y") 

print("Available commands: summary_week, forecast_today.")
command = str(input("Command: "))

if command == "summary_week":
    response = requests.get(request.format(secret_key, latitude, longitude))
    forecast = response.json()

    print("\nToday is "+today_date+". The forecast for today is: ")
    print(forecast["currently"]["summary"])
    print(" -"*int(len(forecast["currently"]["summary"])/2))

    for num in range(unixtime+86400, unixtime+604800, 86400):
        time_response = requests.get(time_machine.format(secret_key,
            latitude, longitude, num))
        future = time_response.json()
        day = datetime.datetime.fromtimestamp(num).strftime("%A")
        print("{}: {}".format(day, future["currently"]["summary"]))
elif command == "forecast_today":
    hours_left = 24 - now_time
    end_of_day = unixtime_rounded + hours_left * 3600
    if hours_left == 0:
        tomorrow_date = today_date + datetime.timedelta(days=1)
        end_of_tomorrow = end_of_day + 86400
        print("\nTomorrow is "+tomorrow_date+". The forecast for tomorrow is: ")
        for num in range(unixtime_rounded, end_of_tomorrow, 3600):
            tomorrow_hour_response = requests.get(time_machine.format(secret_key,
                latitude, longitude, num))
            tomorrow_forecast = tomorrow_hour_response.json()
            tomorrow_call_hour = datetime.datetime.fromtimestamp(num).strftime("%H:%M")
            print("{}: {}C with {}mm of {} (prob: {})".format(call_hour,
                tomorrow_forecast["currently"]["temperature"],
                tomorrow_forecast["currently"]["precipIntensity"],
                tomorrow_forecast["currently"]["precipType"],
                tomorrow_forecast["currently"]["precipProbability"]))
    else:
        print("\nToday is "+today_date+". The forecast for today is: ")
        for num in range(unixtime_rounded, end_of_day, 3600):
            hour_response = requests.get(time_machine.format(secret_key,
                latitude, longitude, num))
            today_forecast = hour_response.json()
            call_hour = datetime.datetime.fromtimestamp(num).strftime("%H:%M")
            print("{}: {}C with {}mm of {} (prob: {})".format(call_hour,
                today_forecast["currently"]["temperature"],
                today_forecast["currently"]["precipIntensity"],
                today_forecast["currently"]["precipType"],
                today_forecast["currently"]["precipProbability"]))

