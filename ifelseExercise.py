import time

current_time = time.strftime("%H:%M:%S")
print(current_time)

hour = int(time.strftime("%H"))
minute = int(time.strftime("%M"))
second = int(time.strftime("%S"))

print(hour, minute, second)

if 5 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
elif 17 <= hour < 21:
    print("Good Evening")
else:
    print("Good Night")