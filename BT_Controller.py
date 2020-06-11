import serial
import time

TTY = "/dev/ttyUSB0"
BAUD = 115200

bt = serial.Serial(port=TTY, baudrate=BAUD)

class BT_Controller:
    def __init__(self):
        pass

    def send_check(self, send: str, expect: str) -> bool:
        bt.write(send.encode())
        time.sleep(0.2)
        recv = bt.read(bt.inWaiting())
        if recv != expect.encode():
            return False
        return True

    def send_print(self, send: str) -> None:
        bt.write(send.encode())
        time.sleep(0.2)
        recv = bt.read(bt.inWaiting())
        print(recv.decode())

    def cmd_mode(self):
        if not self.send_check("$$$", "CMD\r\n"):
            print("Failed to enter command mode")
            return

        try:
            while True:
                cmd = input(">> ")
                if cmd == "q" or cmd == "---":
                    while not self.send_check("---\r\n", "END\r\n"):
                        print("Failed to leave command mode, try again...")
                    break
                else:
                    self.send_print(cmd + "\r\n")
        except:
            print("Leaving command mode...") # maintain state of bluetooth module
            while not self.send_check("---\r\n", "END\r\n"):
                print("Try again...")
            raise

    def shell(self):
        while True:
            cmd = input("# ")
            if cmd == "cmd":
                self.cmd_mode()

def main():
    ctrler = BT_Controller()
    ctrler.shell()


if __name__ == "__main__":
    main()
