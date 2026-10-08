import time
import winsound

winsound.Beep(1000, 500)
for i in range(20):
    print(f"{i}:00")
    time.sleep(60)
while True:
    winsound.Beep(1000, 500)
    time.sleep(1)