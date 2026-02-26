# Source - https://stackoverflow.com/a/54638435
# Posted by C. Lang, modified by community. See post 'Timeline' for change history
# Retrieved 2026-02-21, License - CC BY-SA 4.0

import ctypes
from ctypes import wintypes
import random
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_KEYBOARD = 1
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
# wintypes.ULONG_PTR = wintypes.WPARAM

class MouseInput(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.WPARAM))
    
class KeyInput(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.WPARAM))
    
    def __init__(self, *args, **kwds):
        super(KeyInput, self).__init__(*args, **kwds)

        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)
            
class HardwareInput(ctypes.Structure):
    _fields_ = (("uMsg", wintypes.DWORD), ("wParamL", wintypes.WORD), ("wParamH", wintypes.WORD))
    
class Input(ctypes.Structure):
    class input(ctypes.Union):
        _fields_ = (("ki", KeyInput), ("mi", MouseInput), ("hi", HardwareInput))

    _anonymous_ = ("_input",)

    _fields_ = (("type", wintypes.DWORD), ("_input", input))

KEYEVENTF_SCANCODE = 0x0008

def press_key(hex_key_code):
    scan = user32.MapVirtualKeyExW(hex_key_code, MAPVK_VK_TO_VSC, 0)
    x = Input(type=INPUT_KEYBOARD, ki=KeyInput(wVk=hex_key_code, wScan=scan, dwFlags=KEYEVENTF_SCANCODE))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def release_key(hex_key_code):
    scan = user32.MapVirtualKeyExW(hex_key_code, MAPVK_VK_TO_VSC, 0)
    x = Input(type=INPUT_KEYBOARD, ki=KeyInput(wVk=hex_key_code, wScan=scan, dwFlags=KEYEVENTF_SCANCODE | KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
    
def hardware_key(hex_key_code=0x46):
    press_key(hex_key_code)
    time.sleep(random.uniform(0.06, 0.18))
    release_key(hex_key_code)
    time.sleep(random.uniform(0.05, 0.15))