import json
import urllib.request
import smtplib

from email.message import EmailMessage


url = 'https://api.darksky.net/forecast//28.6024,-81.2001'

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

#data["hourly"]["data"][14]["ozone"]


hourspassedtocheck = 15

temp = data["hourly"]["data"][hourspassedtocheck]["temperature"]
windGust = data["hourly"]["data"][hourspassedtocheck]["windGust"]
windSpeed = data["hourly"]["data"][hourspassedtocheck]["windSpeed"]
precipProbability = data["hourly"]["data"][hourspassedtocheck]["precipProbability"]

message = "Temp is " + str(temp) + "F Windspeed is " + str(windSpeed) +"mph with gusts at " + str(windGust) +"mph Probabibilty of rain is " + str(precipProbability)+"%"

def shouldYouRidethebike(temp, windGust, windSpeed, precipProbability, message):
    if(precipProbability < 50 and windGust < 25 and windSpeed < 15 and temp < 100 ):
        message = message + "\nWith this information it is a good day to ride!"
    else:
        message = message +"\nWith this information is is not a good day to ride. :("
    print(message)

shouldYouRidethebike(temp, windGust, windSpeed, precipProbability, message)

with open("Output.txt", "w") as text_file:
    print(message, file = text_file)

with open("Output.txt") as fp:
    msg = EmailMessage()
    msg.set_content(fp.read())

msg['Subject'] = "Dad does this work?"
msg['From'] = ""
msg['To'] = ""

s  = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()
