import random
import os
import time

echo = False

live_username = r".\web\custom_chat\username.txt"
live_message = r".\web\custom_chat\message.txt"
live_color = r".\web\custom_chat\color.txt"
live_character = r".\web\custom_character\character.txt"

#////////////////////////////#
def hprint(string):
    global echo
    if echo:
        print(string)
def char(value):
    return chr(64+value)
def INT(value):
    return int(value+0.5)
def randint(a, b):
    return random.randint(a, b)
def time_to_vtc():
    return int((time.time() - 946684790)/1850)
def vtc_to_time(vtc):
    return vtc*1850 + 946684790
def find(string, substring):
    for i in substring:
        if string.lower() in i.lower():
            return i
    return None
def find_all(string, substring):
    found = []
    for i in substring:
        if string.lower() in i.lower():
            found.append(i)
    return found
def under_space(string):
    for i in string:
        if i == " ":
            i = "_"
    return string
def random_color():
    return "#{:06X}".format(random.randint(0, 0xFFFFFF))
#////////////////////////////#
def get_windows():
    import win32gui
    windows = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                windows.append((hwnd, title))
                hprint(f"Found window: {title} (HWND: {hwnd})")

    win32gui.EnumWindows(enum_handler, None)
    return windows
def switch_window(hwnd):
    import win32gui
    import win32con
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    win32gui.SetForegroundWindow(hwnd)
    hprint(f"Switched to window with HWND: {hwnd}")
def get_window_by_title(title):
    windows = get_windows()
    for hwnd, win_title in windows:
        if title.lower() in win_title.lower():
            hprint(f"Window found: {win_title} (HWND: {hwnd})")
            return hwnd
    hprint("Window not found")
    return None
def keyboard_input_client(key):
    import win32api
    import win32con
    win32api.keybd_event(key, 0, 0, 0)  # Key down
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)  # Key up
    hprint(f"Simulated key press: {key}")
#////////////////////////////#
def file_read(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()
def file_write(file, string):
    with open(file, "w", encoding="utf-8") as f:
        f.write(string)
#////////////////////////////#
def obs_start_client():
    from obsws_python import ReqClient
    password = os.environ.get("OBS_PASSWORD")
    if not password:
        raise ValueError("OBS_PASSWORD n'est pas défini")
    client = ReqClient(host="localhost", port=4455, password=password)
    print("-----OBS client started-----")
    return client
def obs_change_scene(obs_client, scene_name):
    obs_client.set_current_program_scene(scene_name)
    hprint(f"OBS Scene changed to: {scene_name}")
def obs_refresh_web(obs_client, string):
    obs_client.base_client.req("PressInputPropertiesButton",{"inputName": string,"propertyName": "refreshnocache"})
    hprint(f"OBS Web {string} has been refreshed")
def obs_hide(obs_client, scene, item_id, toggle=False):
    obs_client.set_scene_item_enabled(scene, item_id, toggle)
#////////////////////////////#
# function temporaire #
def string_split(string, separator=" "):
    return string.split(separator)
#////////////////////////////#
def ollama_send_message(MODEL, message):
    import ollama
    try:
        response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": message}])
        if "message" in response and "content" in response["message"]:
            return response["message"]["content"]
        else:
            return str(response)
    except Exception as e:
        print(f"An error occurred while sending message to Ollama: {e}")
        return None
