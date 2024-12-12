from pathlib import Path

import cv2
import easyocr
import numpy as np
import numpy.typing as npt


ASSETS_FOLDER = Path(__file__).resolve().parent / "assets"
HDV_TEMPLATE = cv2.imread(ASSETS_FOLDER / "hdv_template.png", cv2.IMREAD_GRAYSCALE)


class Inspector:
    def __init__(self, img: npt.ArrayLike, scale: float = 1.0):
        self.img = img
        self._gray_img = None
        self._binary_img = None

        self.scale = scale

    @property
    def gray_img(self):
        if self._gray_img is None:
            self._gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return self._gray_img

    @property
    def binary_img(self):
        if self._binary_img is None:
            _, binary_img = cv2.threshold(self.gray_img, 165, 255, cv2.THRESH_BINARY)
            self._binary_img = cv2.resize(binary_img, None, fx=self.scale, fy=self.scale, interpolation=cv2.INTER_AREA)
        return self._binary_img

    def show(self):
        cv2.imshow("Original image", self.img)
        cv2.imshow("Grayscale image", self.gray_img)
        cv2.imshow("Binary image", self.binary_img)
        cv2.waitKey()

    def has_template_on_screen(self, template: npt.ArrayLike) -> bool:
        result = cv2.matchTemplate(self.binary_img, template, cv2.TM_CCOEFF_NORMED)
        return np.any(result > 0.8)


def extract_template_from(img_path: str, template_path: str, hdv_name: str):
    insp = Inspector(cv2.imread(img_path))

    reader = easyocr.Reader(["fr"])
    ocr_results = reader.readtext(insp.binary_img)

    hdv_pos = None
    for pos, text, _ in ocr_results:
        if text == hdv_name:
            hdv_pos = pos
            break
    else:
        raise ValueError(f"Can't find the word `{hdv_name}` in the given screenshot...")

    (x1, y1), _, (x2, y2), _ = hdv_pos

    hdv_template = insp.binary_img[y1:y2, x1:x2]
    cv2.imwrite(template_path, hdv_template)
