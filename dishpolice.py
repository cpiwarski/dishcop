import logging
import os
import sys
import time
import gpiozero
import cv2
import numpy
import picamera


# Declarations
DIR = "/home/pi/Pictures/busted"
FILE = "busted_"
LOG_FORMAT = "%(asctime)-15s %(message)s"
LOG_LEVEL = os.environ.get("LOG_LEVEL").upper()


def take_picture(camera, counter):
    '''
    This function receives a camera object and takes a picture with it, saving
    the image to a file.
    '''
    filename = DIR + FILE + counter
    camera.start_preview()
    camera.capture(filename)
    camera.stop_preview()
    busted_counter += 1


def main():
    '''
    The main function governs the operation of the dishcop application.
    '''

    # initialize environment and hardware
    busted_counter = 0
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
    camera = picamera.PiCamera()

    try:

        print("filler")
    except KeyboardInterrupt:
        logging.info("Application ending.")
        sys.exit(0)


if __name__ == '__main__':
    main()
