import sounddevice as sd
from scipy.io.wavfile import write
import os
import logging

microphone_time = 10  

def record_microphone(file_path):
    """
    Records microphone input and saves it to a file.

    :param file_path: The path to the directory where the microphone recording will be saved.
    """
    fs = 44100
    seconds = microphone_time
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    with open(os.path.join(file_path, "f_microphone.wav"), "wb") as f:
        write(f, fs, myrecording)
    logging.info("Microphone recording saved.")