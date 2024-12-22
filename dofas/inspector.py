from pathlib import Path

import cv2
import easyocr
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
            gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            self._gray_img = cv2.resize(gray_img, None, fx=self.scale, fy=self.scale, interpolation=cv2.INTER_AREA)
        return self._gray_img

    @property
    def binary_img(self):
        if self._binary_img is None:
            _, self._binary_img = cv2.threshold(self.gray_img, 165, 255, cv2.THRESH_BINARY)
        return self._binary_img

    def show(self, template: npt.ArrayLike):
        img = cv2.cvtColor(self.gray_img, cv2.COLOR_GRAY2BGR)

        hdv_pos = self.has_template_on_screen(template)
        if hdv_pos is not None:
            cv2.rectangle(img, hdv_pos[0], hdv_pos[1], (0, 0, 255), 1)

        cv2.imshow("img", img)
        cv2.waitKey()

    def has_template_on_screen(self, template: npt.ArrayLike) -> tuple[tuple[int, int], tuple[int, int]]:
        result = cv2.matchTemplate(self.binary_img, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val > 0.8:
            w, h = template.shape[::-1]
            return (max_loc, (max_loc[0] + w, max_loc[1] + h))
        else:
            return None


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
