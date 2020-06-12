from bt_keyboard_adapter_pi.KB_listener import KB_Listener
from bt_keyboard_adapter_pi.RN42 import RN42


def main():
    rn42 = RN42("/dev/ttyUSB0", 115200)
    listener = KB_Listener(bt_module=rn42)
    listener.listen()


if __name__ == "__main__":
    main()
