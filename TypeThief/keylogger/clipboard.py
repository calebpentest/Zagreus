import win32clipboard
import win32con
import os
import logging

def copy_clipboard(file_path):
    """
    Copies the current clipboard contents to a file.

    :param file_path: The path to the directory where the clipboard contents will be saved.
    """
    clipboard_file = os.path.join(file_path, "f_clipboard.txt")
    try:
        win32clipboard.OpenClipboard()
        if win32clipboard.IsClipboardFormatAvailable(win32con.CF_TEXT):
            pasted_data = win32clipboard.GetClipboardData(win32con.CF_TEXT)
            if pasted_data:
                pasted_data = pasted_data.decode("utf-8")
                with open(clipboard_file, "a") as f:
                    f.write(f"Clipboard Data:\n{pasted_data}\n")
            else:
                with open(clipboard_file, "a") as f:
                    f.write("Clipboard is empty\n")
        else:
            with open(clipboard_file, "a") as f:
                f.write("Text data not available in clipboard\n")
    except win32clipboard.error as e:
        logging.error(f"Clipboard access error: {e}")
    finally:
        win32clipboard.CloseClipboard()