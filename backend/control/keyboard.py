# keyboard.py
import Quartz

key_code_map = {
    "a": 0x00,
    "b": 0x0B,
    "c": 0x08,
    "d": 0x02,
    "e": 0x0E,
    "f": 0x03,
    # Add more key mappings
    "space": 0x31,
    "enter": 0x24,
    # ...
}

def handle_keyboard_input(key):
    key = key.lower()
    key_code = key_code_map.get(key)
    if key_code is not None:
        # Key down event
        key_down = Quartz.CGEventCreateKeyboardEvent(None, key_code, True)
        # Key up event
        key_up = Quartz.CGEventCreateKeyboardEvent(None, key_code, False)
        # Post events
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, key_down)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, key_up)
    else:
        print(f"Key '{key}' not found in key code map.")
