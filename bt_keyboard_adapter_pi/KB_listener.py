import keyboard
import time
import pprint

from . import SCAN_CODES_HID_USAGEID_MAPPING, MODIFIER


class KB_Listener:
    def __init__(self, bt_module):
        self.modifier = 0x00
        self.key_hold = 0x00
        self.bt = bt_module

    def key_press_handler(self, key):
        if keyboard.is_modifier(key.scan_code):
            self.modifier |= MODIFIER[key.scan_code]
        self.key_hold = SCAN_CODES_HID_USAGEID_MAPPING[key.scan_code]
        self.bt.send_report(
            modifier=self.modifier, code=(self.key_hold, 0x00, 0x00, 0x00, 0x00, 0x00)
        )

    def key_release_handler(self, key):
        if keyboard.is_modifier(key.scan_code):
            self.modifier &= ~MODIFIER[key.scan_code]
        self.bt.send_report(self.modifier)  # send empty data packet

    def register(self):
        for k in SCAN_CODES_HID_USAGEID_MAPPING:
            keyboard.on_press_key(k, self.key_press_handler)
            keyboard.on_release_key(k, self.key_release_handler)

    def listen(self):
        self.register()
        while True:
            time.sleep(1)


def main():
    listener = KB_Listener()
    listener.listen()


if __name__ == "__main__":
    main()
