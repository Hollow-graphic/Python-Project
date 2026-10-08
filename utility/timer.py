import time
import winsound

minuter = 10
print("start")
winsound.Beep(1000, 500)
while True:
    for i in range(minuter):
        time.sleep(60)
        print(f"{i+1}:00")
    while True:
        winsound.Beep(1000, 500)
        time.sleep(1)
