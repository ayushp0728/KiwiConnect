import os

def increase_brightness():
    """
    Increase brightness by sending an AppleScript command to simulate pressing the brightness up key.
    """
    os.system("osascript -e 'tell application \"System Events\" to key code 144'")

def decrease_brightness():
    """
    Decrease brightness by sending an AppleScript command to simulate pressing the brightness down key.
    """
    os.system("osascript -e 'tell application \"System Events\" to key code 145'")

# Example usage
if __name__ == "__main__":
    print("Increase or decrease brightness using the functions.")
