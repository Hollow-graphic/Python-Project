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
print(celeste_window)
print(obs_window)