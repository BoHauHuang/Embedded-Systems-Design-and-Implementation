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
        #print(self.key_hold)
        # press F1 start record
        if self.key_hold == 0x3A:
            keyboard.start_recording()
        # press esc stop record
        if self.key_hold == 0x29:
            self.record_list = keyboard.stop_recording()[2:]
            #print(self.record_list)
        # press F2 to play the record
        if self.key_hold == 0x3B:
            keyboard.play(self.record_list)
            '''
            replay_modifier = 0x00
            for event in self.record_list[:-1]:  # discard the esc down for quiting record
                k = event.scan_code
                event = str(event).replace("KeyboardEvent", "")
                [k, action] = event.split(" ")
                action = action[:-1]

                if action == "down":
                    if keyboard.is_modifier(key.scan_code):
                        replay_modifier |= MODIFIER[key.scan_code]
                    self.bt.send_report(modifier=replay_modifier, code=(k_id, 0x00, 0x00, 0x00, 0x00, 0x00))
                else:
                    if keyboard.is_modifier(key.scan_code):
                        replay_modifier &= ~MODIFIER[key.scan_code]
                    self.bt.send_report(replay_modifier)
            '''
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
