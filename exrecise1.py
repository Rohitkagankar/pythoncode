import time
timestamp=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)

if (hour>0 and hour<12):
    print("good morning rohit..")
elif (hour>=12 and hour<18):
    print("good afternoon rohit")
else:
    print("good night rohit...")