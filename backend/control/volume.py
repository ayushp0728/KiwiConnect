import os

def set_volume(level: int):
    """
    Set system volume to a given level (0-100).
    Uses macOS system commands to adjust volume.
    """
    if level < 0 or level > 100:
        raise ValueError("Volume level must be between 0 and 100")
    
    # Use macOS's `osascript` command to set volume
    os.system(f"osascript -e 'set volume output volume {level}'")

def increase_volume(increment: int = 10):
    """
    Increase volume by a given increment.
    """
    os.system(f"osascript -e 'set volume output volume ((output volume of (get volume settings)) + {increment})'")

def decrease_volume(decrement: int = 10):
    """
    Decrease volume by a given decrement.
    """
    os.system(f"osascript -e 'set volume output volume ((output volume of (get volume settings)) - {decrement})'")
