import keyboard
import time
import pprint

from . import SCAN_CODES_HID_USAGEID_MAPPING, MODIFIER, NAME_MAPPING_TO_SCAN_CODES


class KB_Listener:
    def __init__(self, bt_module):
        self.modifier = 0x00
        self.key_hold = 0x00
        self.bt = bt_module
        self.record_list = None

    def key_press_handler(self, key):
        if keyboard.is_modifier(key.scan_code):
            self.modifier |= MODIFIER[key.scan_code]
        self.key_hold = SCAN_CODES_HID_USAGEID_MAPPING[key.scan_code]
        self.bt.send_report(
            modifier=self.modifier, code=(self.key_hold, 0x00, 0x00, 0x00, 0x00, 0x00)
        )

        # press F1 to record
        if self.key_hold == 0x3A:
            self.record_list = keyboard.record() # default: until 'esc' pressed

        # press F2 to play the record
        if self.key_hold == 0x3B:
            for event in self.record_list[:-1]:  # discard the esc down for quiting record
                event = event.replace("KeyboardEvent", "")
                [k, action] = event.split(" ")
                k = k[1:]
                action = action[:-1]
                k_id = SCAN_CODES_HID_USAGEID_MAPPING[NAME_MAPPING_TO_SCAN_CODES[k]]

                if action == "down":
                    if keyboard.is_modifier(key.scan_code):
                        self.modifier |= MODIFIER[key.scan_code]
                    self.bt.send_report(modifier=self.modifier, code=(k, 0x00, 0x00, 0x00, 0x00, 0x00))
                else:
                    if keyboard.is_modifier(key.scan_code):
                        self.modifier &= ~MODIFIER[key.scan_code]
                    self.bt.send_report(self.modifier)

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
