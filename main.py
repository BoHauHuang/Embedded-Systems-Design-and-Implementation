#!/usr/bin/env python3

from bt_keyboard_adapter_rpi.KB_listener import KB_Listener
from bt_keyboard_adapter_rpi.RN42 import RN42
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("port")
args = parser.parse_args()

def main():
    rn42 = RN42(args.port, 115200)
    listener = KB_Listener(bt_module=rn42)
    listener.listen()


if __name__ == "__main__":
    main()
