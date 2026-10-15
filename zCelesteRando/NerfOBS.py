import obswebsocket
import os
import random
import glob
import time

password = os.environ.get("OBS_PASSWORD")

ws = obswebsocket.obsws("localhost", 4455, password)
ws.connect()
print("-----OBS client started-----")

# response = ws.call(obswebsocket.requests.GetSourceFilter(
#     sourceName="Celeste",
#     filterName="IncrustationImage",
# ))
# print(response.datain["filterSettings"])

nerf_count = 2
nerfs = ["3D Effect", "Delay", "Défilement", "IncrustationImage"]
nerf = []
for i in range(nerf_count):
    r = random.choice(nerfs)
    while r in nerf:
        r = random.choice(nerfs)
    nerf.append(r)
print(nerf)

def ChangeFilterState(name, bool):
    ws.call(obswebsocket.requests.SetSourceFilterEnabled(
        sourceName="Celeste",
        filterName=name,
        filterEnabled=bool
    ))
    
for n in nerfs:
    if n in nerf:
        ChangeFilterState(n, True)
    else:
        ChangeFilterState(n, False)

for n in nerf:
    match n:
        case "3D Effect":
            r1 = random.randint(-45, 45)
            r2 = random.randint(-45, 45)
            r3 = random.randint(-45, 45)
            print("3D Effect: " + str(r1) + ", " +str(r2) + ", " + str(r3))
            ws.call(obswebsocket.requests.SetSourceFilterSettings(
                sourceName="Celeste",
                filterName="3D Effect",
                filterSettings={
                    "fov": 120,
                    "rot_x": r1,
                    "rot_y": r2,
                    "rot_z": r3
                }
            ))
        case "Delay":
            r = random.randint(2,6)*50
            print("Delay: " + str(r))
            ws.call(obswebsocket.requests.SetSourceFilterSettings(
                sourceName="Celeste",
                filterName="Delay",
                filterSettings={
                    "delay_ms": r
                }
            ))
        case "Défilement":
            r1 = random.randint(-100, 100)
            r2 = random.randint(-100, 100)
            print("Défilement: " + str(r1) + ", " + str(r2))
            ws.call(obswebsocket.requests.SetSourceFilterSettings(
                sourceName="Celeste",
                filterName="Delay",
                filterSettings={
                    "speed_x": r1,
                    "speed_y": r2
                }
            ))
        case "IncrustationImage":
            dirs = [r"C:\Users\Adam\AppData\Roaming\PrismLauncher\instances\fabric 1.21.7 1.0.0\minecraft\screenshots",
                    r"C:\Users\Adam\Desktop\Shortcut\Image\Meme",
                    r"C:\Users\Adam\Desktop\Shortcut\Image"]
            images = glob.glob(os.path.join(random.choice(dirs), "*"))
            image = random.choice(images)
            print("Incrustation: " + image)
            ws.call(obswebsocket.requests.SetSourceFilterSettings(
                sourceName="Celeste",
                filterName="IncrustationImage",
                filterSettings={
                    "image_path": image
                }
            ))

time.sleep(600)

for n in nerfs:
    if n in nerf:
        ChangeFilterState(n, False)
        
ws.disconnect()



exit()
import win32gui
import win32con

windows = []

def get_windows():
    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                windows.append((hwnd, title))

    win32gui.EnumWindows(enum_handler, None)
    return windows

def switch_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)

get_windows()
for i in windows:
    if i[1] == "Celeste":
        celeste_window = i[0]
        break
for i in windows:
    if i[1].startswith("OBS"):
        obs_window = i[0]
        break

switch_window(obs_window)
switch_window(celeste_window)
