import datetime
from playsound import playsound

#setting variables
hour = int(input("Enter hour :"))
min = int(input("Enter minute :"))
ampm = input("am/pm : ")

#giving 12hour format
if ampm=="pm":
    hour+=12

#checking system time with alarm
while True:
    if hour==datetime.datetime.now().hour and min==datetime.datetime.now().minute:
        print("playing alarm sound")
        playsound("Ek Din Pyaar.mp3")
        break




