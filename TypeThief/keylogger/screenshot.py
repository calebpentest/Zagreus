from PIL import ImageGrab
import os
import logging

def capture_screenshot(file_path):
    """
    Captures a screenshot and saves it to a file.

    :param file_path: The path to the directory where the screenshot will be saved.
    """
    screenshot = ImageGrab.grab()
    screenshot.save(os.path.join(file_path, "f_screenshot.png"))
    logging.info("Screenshot captured.")