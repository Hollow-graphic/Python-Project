import ctypes
from ctypes import wintypes
from PIL import Image

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

# Trouver la fenêtre
hwnd = user32.FindWindowW(None, "Hollow Knight Silksong")

if not hwnd:
    raise Exception("Fenêtre introuvable")

# Récupérer la taille de la fenêtre
rect = wintypes.RECT()
user32.GetClientRect(hwnd, ctypes.byref(rect))

width = rect.right
height = rect.bottom

# DC de la fenêtre
hwnd_dc = user32.GetDC(hwnd)

# DC compatible
mem_dc = gdi32.CreateCompatibleDC(hwnd_dc)
bitmap = gdi32.CreateCompatibleBitmap(hwnd_dc, width, height)

gdi32.SelectObject(mem_dc, bitmap)

# Capture de la fenêtre, même si elle est derrière une autre
user32.PrintWindow(hwnd, mem_dc, 0)

# Récupérer les pixels
class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ("biSize", wintypes.DWORD),
        ("biWidth", wintypes.LONG),
        ("biHeight", wintypes.LONG),
        ("biPlanes", wintypes.WORD),
        ("biBitCount", wintypes.WORD),
        ("biCompression", wintypes.DWORD),
        ("biSizeImage", wintypes.DWORD),
        ("biXPelsPerMeter", wintypes.LONG),
        ("biYPelsPerMeter", wintypes.LONG),
        ("biClrUsed", wintypes.DWORD),
        ("biClrImportant", wintypes.DWORD),
    ]

class BITMAPINFO(ctypes.Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),
        ("bmiColors", wintypes.DWORD * 3),
    ]

bmi = BITMAPINFO()
bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
bmi.bmiHeader.biWidth = width
bmi.bmiHeader.biHeight = -height
bmi.bmiHeader.biPlanes = 1
bmi.bmiHeader.biBitCount = 32
bmi.bmiHeader.biCompression = 0

buffer = ctypes.create_string_buffer(width * height * 4)

gdi32.GetDIBits(
    mem_dc,
    bitmap,
    0,
    height,
    buffer,
    ctypes.byref(bmi),
    0
)

image = Image.frombuffer(
    "RGBA",
    (width, height),
    buffer,
    "raw",
    "BGRA",
    0,
    1
)

image.save("./zServerPlayBatch/screenshot.png")

# Nettoyage
gdi32.DeleteObject(bitmap)
gdi32.DeleteDC(mem_dc)
user32.ReleaseDC(hwnd, hwnd_dc)