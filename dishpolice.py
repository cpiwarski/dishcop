import logging
import os
import sys
import time
import gpiozerp
import picamera


# Declarations
DIR = "/home/pi/Pictures/busted"
LOG_FORMAT = "%(asctime)-15s %(message)s"
LOG_LEVEL = os.environ.get("LOG_LEVEL").upper()


def take_picture(camera):
    '''
    This function receives a camera object and takes a picture with it, saving
    the image to a file.
    '''


def main():
    '''
    The main function governs the operation of the dishcop application.
    '''
    
    # initialize environment and hardware
    logging.basicCconfig(level=LOG_LEVEL, format=LOG_FORMAT)
    camera = picamera.PiCamera()

    try:

        print("filler")
    except KeyboardInterrupt:
        logging.info("Application ending.")
        sys.exit(0)


if __name__ == '__main__':
    main()
