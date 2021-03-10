# Copyright (c) 2021 Linaro Limited.

import pathlib
import serial
import shutil
import time

# Serial port name and baudrate
SERIAL_PORT = "/dev/tty.usbserial-14543100"
SERIAL_BAUDRATE = 115200

# Path to image file
BIN_FILE = pathlib.Path(__file__).parent.absolute().parent / "build" / "app" / "mps3_524.bin"
# Path where image file should be copied
BIN_DEST_PATH = "/Volumes/V2M-MPS3/SOFTWARE"

def initiate_reboot():
    try:
        serial_port = serial.Serial(SERIAL_PORT, SERIAL_BAUDRATE, exclusive=False)
    except serial.SerialException:
        print("Unable to open serial port " + SERIAL_PORT)
    else:
        # Send reboot command to mcc terminal
        # Wring the string `reboot\n` is causing data loss. Therefore send
        # individual characters and introduce 100ms delay between each
        # character.
        serial_port.write(b'r')
        time.sleep(0.1)
        serial_port.write(b'e')
        time.sleep(0.1)
        serial_port.write(b'b')
        time.sleep(0.1)
        serial_port.write(b'o')
        time.sleep(0.1)
        serial_port.write(b'o')
        time.sleep(0.1)
        serial_port.write(b't')
        time.sleep(0.1)
        serial_port.write(b'\n')

def copy_application_image():
    shutil.copy(BIN_FILE, BIN_DEST_PATH)


if __name__ == '__main__':
    # Copy application image onto USB drive
    copy_application_image()
    # Sleep for a second
    time.sleep(1)
    # Initiate reboot
    initiate_reboot()
