import serial
import time
import struct

TTY = "/dev/ttyUSB0"
BAUD = 115200

bt = serial.Serial(port=TTY, baudrate=BAUD)


class RN42:
    hid_kb_report_fmt = struct.Struct("B B B B B B B B")
    hid_mouse_report_fmt = struct.Struct("B B B B")

    def cmd_protector(func):
        """Decorator to maintain state of bluetooth module when exception happended
        """

        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                print("Leaving command mode...")
                while not RN42.send_check("---\r\n", "END\r\n"):
                    print("Try again...")
                raise

        return wrapper

    @staticmethod
    def send_check(send: str, expect: str) -> bool:
        bt.write(send.encode())
        time.sleep(0.5)
        recv = bt.read(bt.inWaiting())
        if recv != expect.encode():
            return False
        return True

    @staticmethod
    def send_print(send: str) -> None:
        bt.write(send.encode())
        time.sleep(0.5)
        recv = bt.read(bt.inWaiting())
        print(recv.decode())

    @cmd_protector
    def cmd_mode(self):
        if not self.send_check("$$$", "CMD\r\n"):
            print("Failed to enter command mode")
            return

        while True:
            cmd = input(">> ")
            if cmd == "q" or cmd == "---":
                while not self.send_check("---\r\n", "END\r\n"):
                    print("Failed to leave command mode, try again...")
                break
            else:
                self.send_print(cmd + "\r\n")

    @cmd_protector
    def reset_module(self):
        if not self.send_check("$$$", "CMD\r\n"):
            print("Failed to enter command mode")
            return

        cmd_pipeline = (
            ("SF,1\r\n", "AOK\r\n", "Restore factory settings"),
            ("SH,0230\r\n", "AOK\r\n", "Set descriptor type to combo mode"),
            ("SU,115K\r\n", "AOK\r\n", "Set UART baud rate to 115200"),
            ("S~,6\r\n", "AOK\r\n", "Set HID profile"),
            ("SN,bt-keyboard-adapter\r\n", "AOK\r\n", "Set module name"),
            ("R,1\r\n", "Reboot!\r\n", "Restart"),
        )

        for i in cmd_pipeline:
            cmd = i[0]
            expect = i[1]
            print(i[2])
            while not self.send_check(cmd, expect):
                print("Try again...")


class BT_Controller(RN42):
    def report_sender(self):
        action = [
            int("0x00", 16),
            int("0x00", 16),
            int("0x54", 16),
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
        ]
        release = [
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
            int("0x00", 16),
        ]
        action_serial = b"\xfd\x09\x01" + self.hid_kb_report_fmt.pack(*action)
        release_serial = b"\xfd\x09\x01" + self.hid_kb_report_fmt.pack(*release)

        # action = [
        #     int("0x00", 16),
        #     int("0x00", 16),
        #     int("0x00", 16),
        #     int("0x20", 16),
        # ]
        # release = [
        #     int("0x00", 16),
        #     int("0x00", 16),
        #     int("0x00", 16),
        #     int("0x00", 16),
        # ]
        # action_serial = b"\xfd\x05\x02" + self.hid_mouse_report_fmt.pack(*action)
        # release_serial = b"\xfd\x05\x02" + self.hid_mouse_report_fmt.pack(*release)
        # print(action_serial)

        bt.write(action_serial)
        bt.write(release_serial)

    def shell(self):
        while True:
            cmd = input("# ")
            if cmd == "cmd":
                self.cmd_mode()
            elif cmd == "reset":
                self.reset_module()
            else:
                self.report_sender()


def main():
    ctrler = BT_Controller()
    ctrler.shell()


if __name__ == "__main__":
    main()
