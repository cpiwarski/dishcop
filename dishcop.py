'''
Module comment to hide pylint error
'''

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


def main():
    '''
    The main function governs the operation of the dishcop application.
    '''

    # initialize environment and hardware
    busted_counter = 0
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
    background = cv2.createBackgroundSubtractorMOG2()


    # initialize video stream
    video = cv2.VideoCapture(0)
    if not video.isOpened:
        logging.info("failed to initialize camera")
        sys.exit(0)

    try:

        # Perpetual video loop
        while True:

            ret, frame = video.read()
            
            if frame is None:
                break

            fg_mask = background.apply(frame)

            cv.imshow("frame", frame)
            cv.imshow("Mask", fg_mask)


    except KeyboardInterrupt:
        logging.info("Application ending.")
        sys.exit(0)

    video.release()


if __name__ == '__main__':
    main()
