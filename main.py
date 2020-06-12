import time
from bt_keyboard_adapter.KB_listener import KB_Listener


def main():
    listener = KB_Listener()
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
