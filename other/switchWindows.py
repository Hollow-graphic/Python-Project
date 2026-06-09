import tkinter as tk
import win32gui
import win32con
import random
import time


# -----------------------------
# Récupération fenêtres
# -----------------------------
def get_windows():
    windows = []

    def enum_handler(hwnd, _):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                windows.append((hwnd, title))

    win32gui.EnumWindows(enum_handler, None)
    return windows


# -----------------------------
# Focus fenêtre
# -----------------------------
def focus_window(hwnd):
    try:
        # 1. essayer focus direct
        win32gui.SetForegroundWindow(hwnd)
    except:
        try:
            # 2. petit trick Windows
            win32gui.ShowWindow(hwnd, 5)  # SW_SHOW
            win32gui.SetForegroundWindow(hwnd)
        except:
            pass


# -----------------------------
# APP
# -----------------------------
class WindowSwitcher(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Auto Window Switcher")
        self.geometry("700x550")

        # STATE
        self.auto_switch = False
        self.interval = 10
        self.last_switch = time.time()
        self.last_hwnd = None

        # UI
        self.status_label = tk.Label(self, text="Auto-switch: OFF", font=("Arial", 12))
        self.status_label.pack()

        self.timer_label = tk.Label(self, text="Timer: 10s", font=("Arial", 12))
        self.timer_label.pack()

        self.selected_label = tk.Label(self, text="Selected: none", font=("Arial", 10))
        self.selected_label.pack()

        tk.Button(self, text="TOGGLE AUTO SWITCH", command=self.toggle_auto).pack(fill=tk.X)
        tk.Button(self, text="Refresh windows", command=self.refresh).pack(fill=tk.X)
        tk.Button(self, text="Switch now", command=self.switch_random).pack(fill=tk.X)

        # LIST FRAME
        self.frame = tk.Frame(self)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.windows = []
        self.vars = []

        self.refresh()
        self.loop()

    # -----------------------------
    # toggle auto
    # -----------------------------
    def toggle_auto(self):
        self.auto_switch = not self.auto_switch
        self.status_label.config(
            text=f"Auto-switch: {'ON' if self.auto_switch else 'OFF'}"
        )

    # -----------------------------
    # refresh windows
    # -----------------------------
    def refresh(self):
        for w in self.frame.winfo_children():
            w.destroy()

        self.windows = get_windows()
        self.vars = []

        for hwnd, title in self.windows:
            var = tk.BooleanVar()
            tk.Checkbutton(self.frame, text=title, variable=var).pack(anchor="w")
            self.vars.append((var, hwnd, title))

    # -----------------------------
    # switch random (no repeat)
    # -----------------------------
    def switch_random(self):
        selected = [(hwnd, title) for var, hwnd, title in self.vars if var.get()]

        if not selected:
            self.selected_label.config(text="Selected: none")
            return

        # remove last window to avoid repetition
        filtered = [w for w in selected if w[0] != self.last_hwnd]

        if not filtered:
            filtered = selected

        hwnd, title = random.choice(filtered)

        focus_window(hwnd)

        self.selected_label.config(text=f"Selected: {title}")

        self.last_hwnd = hwnd
        self.last_switch = time.time()

    # -----------------------------
    # main loop
    # -----------------------------
    def loop(self):
        elapsed = time.time() - self.last_switch
        remaining = max(0, self.interval - int(elapsed))

        self.timer_label.config(text=f"Timer: {remaining}s")

        if self.auto_switch and elapsed >= self.interval:
            self.switch_random()

        self.after(200, self.loop)


# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    WindowSwitcher().mainloop()