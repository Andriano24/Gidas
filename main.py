import ctypes
import random
import sys
import threading
import time

import mss
import win32api
import win32gui

from benchmark import Benchmark
from constants import AMBER_COLOR_BGR, DIALOGUE_ICON_PIXELS_CROP, FIRST_ICON_PIXELS_CROP, FLOUR_COLOR_BGR, MSS_REGION, SECOND_ICON_PIXELS_CROP, SEPARATOR_LINE, SEPARATOR_TIMES, THIRD_ICON_PIXELS_CROP, VERSION

if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

benchmark = Benchmark()

script_active = True
visible_icon = ""

class ImageToFrame:
    def __init__(self, sct_img):
        self.raw = sct_img.raw
        self.width = sct_img.width
        self.stride = sct_img.width * 4

    def __getitem__(self, coords):
        y, x = coords
        offset = (y * self.stride) + (x * 4)

        return (self.raw[offset], self.raw[offset + 1], self.raw[offset + 2])

def is_color_near(current_pixel, target_color, tolerance=5):
    return all(abs(int(c) - int(t)) <= tolerance for c, t in zip(current_pixel[:3], target_color))

def press_interact_key(hwnd ,vk_code=0x46):
    scan_code = win32api.MapVirtualKey(vk_code, 0)
    win32api.PostMessage(hwnd, 0x0100, vk_code, (scan_code << 16) | 1)
    time.sleep(random.uniform(0.06, 0.18))
    win32api.PostMessage(hwnd, 0x0101, vk_code, (scan_code << 16) | (1 << 30) | (1 << 31) | 1)

def monitor_keys():
    global script_active
    
    KEYS = {
        0x78: "TOGGLE",
        0x79: "BENCHMARK",
    }

    last_states = {key: False for key in KEYS}

    while True:
        for vk_code, action in KEYS.items():
            is_down = bool(win32api.GetAsyncKeyState(vk_code) & 0x8000)
            
            if is_down and not last_states[vk_code]:
                if action == "TOGGLE":
                    script_active = not script_active
                    status = "Enabled" if script_active else "Disabled"
                    print(f"[INFO] Dialogue autoskip: {status}")
                
                elif action == "BENCHMARK":
                    benchmark.get_summary()
            
            last_states[vk_code] = is_down

        time.sleep(0.01) 

threading.Thread(target=monitor_keys, daemon=True).start()

print(SEPARATOR_LINE)
print(f"{"G.I.D.A.S - Genshin Impact Dialogue Autoskip Script v" + VERSION:^{SEPARATOR_TIMES}}")
print(f"{"[F9] Toggle script [F10] Show benchmark":^{SEPARATOR_TIMES}}")
print(SEPARATOR_LINE + "\n")
print(f"[INFO] Dialogue autoskip: Enabled")

sct = mss.mss()

def main():
    global visible_icon

    hwnd = win32gui.GetForegroundWindow()
    window_title = win32gui.GetWindowText(hwnd)

    if window_title != "Genshin Impact":
        return

    if not script_active:
        return
    
    image = sct.grab(MSS_REGION)
    frame = ImageToFrame(image)

    if is_color_near(frame[THIRD_ICON_PIXELS_CROP["first"][1], THIRD_ICON_PIXELS_CROP["first"][0]], FLOUR_COLOR_BGR) and is_color_near(frame[THIRD_ICON_PIXELS_CROP["second"][1], THIRD_ICON_PIXELS_CROP["second"][0]], FLOUR_COLOR_BGR):
        if visible_icon != "third":
            print("[INFO] Skipping dialogue...")
            # print("[DEBUG] Hide icon visible")

        press_interact_key(hwnd)
        visible_icon = "third"
        return
    
    if is_color_near(frame[FIRST_ICON_PIXELS_CROP["first"][1], FIRST_ICON_PIXELS_CROP["first"][0]], FLOUR_COLOR_BGR) and is_color_near(frame[FIRST_ICON_PIXELS_CROP["second"][1], FIRST_ICON_PIXELS_CROP["second"][0]], FLOUR_COLOR_BGR):
        if visible_icon != "first":
            print("[INFO] Skipping dialogue...")
            # print("[DEBUG] Auto-play icon visible")

        press_interact_key(hwnd)
        visible_icon = "first"
        return
        
    if is_color_near(frame[SECOND_ICON_PIXELS_CROP["first"][1], SECOND_ICON_PIXELS_CROP["first"][0]], FLOUR_COLOR_BGR) and is_color_near(frame[SECOND_ICON_PIXELS_CROP["second"][1], SECOND_ICON_PIXELS_CROP["second"][0]], FLOUR_COLOR_BGR):
        if visible_icon != "second":
            print("[INFO] Skipping dialogue...")
            # print("[DEBUG] Dialogue review icon visible")

        press_interact_key(hwnd)
        visible_icon = "second"
        return

    if is_color_near(frame[DIALOGUE_ICON_PIXELS_CROP["first"][1], DIALOGUE_ICON_PIXELS_CROP["first"][0]], AMBER_COLOR_BGR) or is_color_near(frame[DIALOGUE_ICON_PIXELS_CROP["second"][1], DIALOGUE_ICON_PIXELS_CROP["second"][0]], AMBER_COLOR_BGR):
        if visible_icon != "dialogue":
            print("[INFO] Skipping dialogue...")
            # print("[DEBUG] Dialogue icon visible")

        press_interact_key(hwnd)
        visible_icon = "dialogue"
        return
    
    visible_icon = ""

try:
    while True:
        start = time.perf_counter()
        main()
        end = time.perf_counter()
        benchmark.update(start, end)
        time.sleep(random.uniform(0.1, 0.2))
except Exception as e:
    print(f"[FATAL] {e}")
except KeyboardInterrupt:
    benchmark.get_summary()
finally:
    try:
        input("\nPress ENTER to close this window...")
    except:
        pass

    sys.exit()