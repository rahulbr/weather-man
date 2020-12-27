"""
Weather Man
"""

import cv2


WIDTH = 1920
HEIGHT = 1080

def main():

    # Start the camera.
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while (True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Capture an Image

    # Save the file to disk

    # Write log.

    # initialise pygame

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Run
    main()
