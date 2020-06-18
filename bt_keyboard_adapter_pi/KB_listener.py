import keyboard
import time
import pprint
import multiprocessing as mp
import queue

from . import SCAN_CODES_HID_USAGEID_MAPPING, MODIFIER


class KB_Listener:
    def __init__(self,bt_module):
        self.modifier = 0x00
        self.key_hold = 0x00
        self.bt = bt_module
        self.recording = False
        self.replaying = False
        self.replay_buf = []

        self.pre_key = 0x00
        self.macro_key = 0x00

    def key_press_handler(self, key):
        if keyboard.is_modifier(key.scan_code):
            self.modifier |= MODIFIER[key.scan_code]
        self.key_hold = SCAN_CODES_HID_USAGEID_MAPPING[key.scan_code]
        if self.key_hold != self.macro_key:
            self.bt.send_report(
                modifier=self.modifier, code=(self.key_hold, 0x00, 0x00, 0x00, 0x00, 0x00)
            )

        # replaying, press macro again to stop
        if self.replaying:
            if self.key_hold == self.macro_key:
                self.replaying = False
        else:
            if self.recording:
                # macro: stop record
                if self.key_hold == self.macro_key and self.recording:
                    try:
                        # the first 2 elements is F1 down, F1 up
                        self.replay_buf = keyboard.stop_recording()[2:]
                    except ValueError:  # if not keyboard.start_recording()
                        pass
                    finally:
                        self.recording = False
            else:
                # F1: assign macro key
                if self.pre_key == 0x3f:
                    self.macro_key = self.key_hold
                # F2: start record, prevent nested recording
                elif self.key_hold == 0x40:
                    keyboard.start_recording()
                    self.recording = True
                # macro: play the record
                elif self.key_hold == self.macro_key:
                    self.replaying = True
                
        self.pre_key = self.key_hold

    def key_release_handler(self, key):
        if keyboard.is_modifier(key.scan_code):
            self.modifier &= ~MODIFIER[key.scan_code]
        if self.key_hold != self.macro_key:
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
