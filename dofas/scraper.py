import time

import cv2
import easyocr
import mss
import numpy as np

from dofas import Inspector


class Scraper:
    def __init__(self, hdv_template_path: str):
        self.hdv_template = cv2.imread(hdv_template_path, cv2.IMREAD_GRAYSCALE)

        # Rescale it for faster performances
        self.scale = 0.5
        self.hdv_template = cv2.resize(
            self.hdv_template, None, fx=self.scale, fy=self.scale, interpolation=cv2.INTER_AREA
        )

        self.reader = easyocr.Reader(["fr"])

    def start(self):
        with mss.mss() as sct:
            while True:
                last_time = time.time()

                # Get raw pixels from the screen
                img = np.array(sct.grab(sct.monitors[1]))
                insp = Inspector(img, scale=self.scale)

                r = insp.has_template_on_screen(self.hdv_template)

                # Display the picture
                cv2.imshow("X", img)

                # Display the picture in grayscale
                # cv2.imshow('OpenCV/Numpy grayscale',
                #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

                print(f"{'O' if r else 'x'} - fps: {1 / (time.time() - last_time):.0f}")

                # Press "q" to quit
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    cv2.destroyAllWindows()
                    break
