import keyboard
import time
import pprint
import multiprocessing as mp
import queue

from . import SCAN_CODES_HID_USAGEID_MAPPING, MODIFIER


class KB_Listener:
    def __init__(self, bt_module):
        self.modifier = 0x00
        self.key_hold = 0x00
        self.bt = bt_module
        self.recording = False
        self.replaying = False
        self.replay_buf = []

    def key_press_handler(self, key):
        if keyboard.is_modifier(key.scan_code):
            self.modifier |= MODIFIER[key.scan_code]
        self.key_hold = SCAN_CODES_HID_USAGEID_MAPPING[key.scan_code]
        self.bt.send_report(
            modifier=self.modifier, code=(self.key_hold, 0x00, 0x00, 0x00, 0x00, 0x00)
        )
        # replaying, press F2 again to stop
        if self.replaying:
            if self.key_hold == 0x3B:
                self.replaying = False
        else:
            # F1: start record, prevent nested recording
            if self.key_hold == 0x3A and not self.recording and not self.replaying:
                keyboard.start_recording()
                self.recording = True
            # ESC: stop record
            elif self.key_hold == 0x29:
                try:
                    # the first 2 elements is F1 down, F1 up
                    self.replay_buf = keyboard.stop_recording()[2:]
                except ValueError:  # if not keyboard.start_recording()
                    pass
                finally:
                    self.recording = False
            # F2: play the record
            elif self.key_hold == 0x3B:
                self.replaying = True

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
            if self.replaying:
                child = mp.Process(
                    target=lambda e: keyboard.replay(e), args=(self.replay_buf,)
                )
                child.start()
                child.join()
            else:
                time.sleep(1)


def main():
    listener = KB_Listener()
    listener.listen()


if __name__ == "__main__":
    main()
