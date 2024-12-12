from pathlib import Path

import cv2
import easyocr
import numpy.typing as npt


ASSETS_FOLDER = Path(__file__).resolve().parent / "assets"
HDV_TEMPLATE = cv2.imread(ASSETS_FOLDER / "hdv_template.png", cv2.IMREAD_GRAYSCALE)


class Inspector:
    def __init__(self, img: npt.ArrayLike, reader: easyocr.Reader = None):
        self.img = img
        self._gray_img = None
        self._binary_img = None

        self.reader = reader

    @property
    def gray_img(self):
        if self._gray_img is None:
            self._gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        return self._gray_img

    @property
    def binary_img(self):
        if self._binary_img is None:
            _, self._binary_img = cv2.threshold(self.gray_img, 165, 255, cv2.THRESH_BINARY)
        return self._binary_img

    def show(self):
        cv2.imshow("Original image", self.img)
        cv2.imshow("Grayscale image", self.gray_img)
        cv2.imshow("Binary image", self.binary_img)
        cv2.waitKey()

    def has_hdv_opened(self) -> bool:
        # orb = cv2.ORB_create(nfeatures=1000)

        # keypoints1, descriptors1 = orb.detectAndCompute(self.binary_img, None)
        # keypoints2, descriptors2 = orb.detectAndCompute(HDV_TEMPLATE, None)

        # print(descriptors1, descriptors2)

        # bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        # matches = bf.match(descriptors1, descriptors2)

        # matches = sorted(matches, key=lambda x: x.distance)

        # print(len(matches))

        # return len(matches) >= 10

        x = self.reader.readtext(self.binary_img, min_size=300, batch_size=5)
        print([a[1] for a in x])

        # h, w = HDV_TEMPLATE.shape
        # for scale in [1, 0.5, 0.75, 0.25, 1.5]:
        #     resized_template = cv2.resize(HDV_TEMPLATE, (int(w * scale), int(h * scale)))

        #     result = cv2.matchTemplate(self.binary_img, resized_template, cv2.TM_CCOEFF_NORMED)
        #     cv2.imshow(f"result", result)
        #     cv2.waitKey()
        #     if np.any(result > 0.8):
        #         return True

        # return False

        # result = cv2.matchTemplate(self.binary_img, HDV_TEMPLATE, cv2.TM_CCOEFF_NORMED)
        # return np.any(result > 0.8)


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
