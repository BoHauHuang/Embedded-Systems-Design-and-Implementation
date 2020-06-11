import keyboard
import time
import pprint
from Constant import SCAN_CODES_NAME_MAPPING


def key_press(key):
    print("press ", key.name, key.scan_code)  # TODO: send packet


def key_release(key):
    print("release ", key.name, key.scan_code)  # TODO: send end packet


for k in SCAN_CODES_NAME_MAPPING:
    keyboard.on_press_key(k, key_press)
    keyboard.on_release_key(k, key_release)

while True:
    time.sleep(1)
