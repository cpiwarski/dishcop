'''
Module comment to hide pylint error
'''

import logging
import os
import sys
import time
import cv2


# Declarations
DIR = "/home/pi/Pictures/busted"
FILE = "busted_"
LOG_FORMAT = "%(asctime)-15s %(message)s"
LOG_LEVEL = os.environ.get("LOG_LEVEL").upper()
SLEEP_DURATION = 120


def take_frame(video):
    '''
    take_frame captures an image using the supplied video feed and then
    processes it for motion detection.
    '''
    ret, frame = video.read()

    if frame is None:
        logging.info("failure to take frame. Exiting...")
        sys.exit(0)
    frame = noise_processing(frame)
    return frame


def noise_processing(img):
    '''
    noise_processing receives an image object and processes it to
    remove image noise.
    '''
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(img, (21, 21), 0)
    return frame


def main():
    '''
    The main function governs the operation of the dishcop application.
    '''

    # initialize environment and hardware
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)
    video = cv2.VideoCapture(0)
    if not video.isOpened:
        logging.info("failed to initialize camera")
        sys.exit(0)

    threshold = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]

    # let camera fully initialize
    time.sleep(4)

    # create initial background frame
    background = take_frame(video)

    try:

        # Perpetual video loop
        while True:

            new_frame = take_frame(video)

            # fg_mask = background.apply(frame)
            delta = cv2.absdiff(new_frame, background)

            if threshold.sum() > 100:

                # snap a picture

                # suspend for dish washing duration - test times
                time.sleep(SLEEP_DURATION)
                # motion! Do the thing
                print("yes")
            else:
                # no motion, do nothing.
                print("no")

            time.sleep(SLEEP_DURATION)


    except KeyboardInterrupt:
        logging.info("Application ending.")
        sys.exit(0)

    video.release()


if __name__ == '__main__':
    main()
