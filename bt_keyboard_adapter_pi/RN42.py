import serial
import time
import struct


class RN42:
    hid_kb_report_header = b"\xfd\x09\x01"
    hid_mouse_report_header = b"\xfd\x05\x02"
    hid_kb_report_fmt = struct.Struct("B B B B B B B B")
    hid_mouse_report_fmt = struct.Struct("B B B B")

    def __init__(self, port, baudrate):
        self.bt = serial.Serial(port=port, baudrate=baudrate)

    def cmd_protector(func):
        """Decorator to maintain state of bluetooth module when exception happended
        """

        def wrapper(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except:
                print("Leaving command mode...")
                while not self.send_check("---\r\n", "END\r\n"):
                    print("Try again...")
                raise

        return wrapper

    def send_check(self, send: str, expect: str) -> bool:
        self.bt.write(send.encode())
        time.sleep(0.5)
        recv = self.bt.read(self.bt.inWaiting())
        if recv != expect.encode():
            return False
        return True

    def send_print(self, send: str) -> None:
        self.bt.write(send.encode())
        time.sleep(0.5)
        recv = self.bt.read(self.bt.inWaiting())
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

    def send_report(self, modifier=0x00, code=((0x00,) * 6)):
        report_data = [modifier, 0x00, *code]
        report = self.hid_kb_report_header + self.hid_kb_report_fmt.pack(*report_data)
        self.bt.write(report)


def main():
    rn42 = RN42("/dev/ttyUSB0", 115200)
    while True:
        cmd = input("# ")
        if cmd == "cmd":
            rn42.cmd_mode()
        elif cmd == "reset":
            rn42.reset_module()
        else:
            pass


if __name__ == "__main__":
    main()
