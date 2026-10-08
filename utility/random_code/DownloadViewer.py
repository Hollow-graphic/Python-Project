import os
import sys
import time
import tkinter as tk
from tkinter import filedialog, messagebox

#used AI
class FileMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DownloadViewer")
        self.root.geometry("720x240")
        self.root.resizable(False, False)

        self.running = False
        self.schedule_id = None
        self.path = None
        self.start_time = None
        self.last_time = None
        self.last_size = 0

        tk.Label(root, text="Chemin du fichier :").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.path_entry = tk.Entry(root, width=70)
        self.path_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Button(root, text="Parcourir", command=self.choose_path).grid(row=0, column=2, padx=5, pady=10)
        tk.Button(root, text="Démarrer", command=self.start_monitoring).grid(row=1, column=1, pady=10)
        tk.Button(root, text="Arrêter", command=self.stop_monitoring).grid(row=1, column=2, pady=10)

        self.status_var = tk.StringVar(value="En attente...")
        self.size_var = tk.StringVar(value="Taille : --")
        self.speed_var = tk.StringVar(value="Vitesse : --")
        self.avg_speed_var = tk.StringVar(value="Vitesse moyenne : --")

        tk.Label(root, textvariable=self.status_var, fg="blue").grid(row=2, column=0, columnspan=3, pady=5)
        tk.Label(root, textvariable=self.size_var, fg="green").grid(row=3, column=0, columnspan=3, pady=5)
        tk.Label(root, textvariable=self.speed_var, fg="green").grid(row=4, column=0, columnspan=3, pady=5)
        tk.Label(root, textvariable=self.avg_speed_var, fg="green").grid(row=5, column=0, columnspan=3, pady=5)

    def choose_path(self):
        path = filedialog.askopenfilename(title="Sélectionner un fichier déjà en cours de téléchargement")
        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)

    def start_monitoring(self):
        self.path = self.path_entry.get().strip()
        if not self.path:
            messagebox.showerror("Erreur", "Veuillez saisir un chemin de fichier.")
            return

        self.running = True
        self.start_time = time.monotonic()
        self.last_time = time.monotonic()
        self.last_size = 0
        self.status_var.set("Surveillance en cours...")
        self._schedule_tick()

    def stop_monitoring(self):
        self.running = False
        if self.schedule_id is not None:
            self.root.after_cancel(self.schedule_id)
            self.schedule_id = None
        self.status_var.set("Arrêté")

    def _schedule_tick(self):
        if not self.running:
            return
        self.schedule_id = self.root.after(500, self._tick)

    def _tick(self):
        if not self.running:
            return

        if not os.path.exists(self.path):
            self.status_var.set("Fichier introuvable, attente...")
            self.size_var.set("Taille : 0 octets")
            self.speed_var.set("Vitesse : 0 octets/s")
            self.avg_speed_var.set("Vitesse moyenne : 0 octets/s")
            self._schedule_tick()
            return

        current_size = os.path.getsize(self.path)
        now = time.monotonic()

        if self.last_size == 0 and self.start_time is not None:
            self.last_size = current_size
            self.last_time = now
            self.status_var.set("Fichier détecté, surveillance en cours...")
            self.size_var.set(f"Taille : {self.format_size(current_size)}")
            self.speed_var.set("Vitesse : 0 octets/s")
            self.avg_speed_var.set("Vitesse moyenne : 0 octets/s")
            self._schedule_tick()
            return

        elapsed = now - self.start_time
        delta_time = now - self.last_time
        delta_size = current_size - self.last_size

        current_speed = (delta_size / delta_time) if delta_time > 0 else 0
        avg_speed = (current_size / elapsed) if elapsed > 0 else 0

        self.last_size = current_size
        self.last_time = now

        self.status_var.set("Surveillance en cours...")
        self.size_var.set(f"Taille : {self.format_size(current_size)}")
        self.speed_var.set(f"Vitesse : {self.format_speed(current_speed)}")
        self.avg_speed_var.set(f"Vitesse moyenne : {self.format_speed(avg_speed)}")
        self._schedule_tick()

    @staticmethod
    def format_size(size_bytes):
        if size_bytes < 1024:
            return f"{size_bytes} octets"
        if size_bytes < 1024 * 1024:
            return f"{size_bytes / 1024:.2f} Ko"
        if size_bytes < 1024 * 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.2f} Mo"
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} Go"

    @staticmethod
    def format_speed(speed_bytes_per_sec):
        if speed_bytes_per_sec < 1024:
            return f"{speed_bytes_per_sec:.2f} octets/s"
        if speed_bytes_per_sec < 1024 * 1024:
            return f"{speed_bytes_per_sec / 1024:.2f} Ko/s"
        return f"{speed_bytes_per_sec / (1024 * 1024):.2f} Mo/s"


def console_mode(path):
    print(f"Surveillance du fichier : {path}")
    last_size = 0
    last_time = time.monotonic()
    start_time = time.monotonic()

    while True:
        if not os.path.exists(path):
            print("Fichier introuvable, attente...")
            time.sleep(1)
            continue

        current_size = os.path.getsize(path)
        now = time.monotonic()
        elapsed = now - start_time
        delta_time = now - last_time
        delta_size = current_size - last_size

        current_speed = (delta_size / delta_time) if delta_time > 0 else 0
        avg_speed = (current_size / elapsed) if elapsed > 0 else 0

        print(
            f"\rTaille : {FileMonitorApp.format_size(current_size)} | "
            f"Vitesse : {FileMonitorApp.format_speed(current_speed)} | "
            f"Vitesse moyenne : {FileMonitorApp.format_speed(avg_speed)}",
            end=""
        )

        last_size = current_size
        last_time = now
        time.sleep(1)


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        console_mode(path)
        return

    root = tk.Tk()
    app = FileMonitorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
