import cv2
import numpy as np


def extract_features(mask):

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return None

    cnt = max(contours, key=cv2.contourArea)

    area = cv2.contourArea(cnt)

    perimeter = cv2.arcLength(
        cnt,
        True
    )

    circularity = (
        4 * np.pi * area /
        (perimeter ** 2)
    ) if perimeter > 0 else 0

    x, y, w, h = cv2.boundingRect(cnt)

    aspect_ratio = w / h

    return {
        "area": area,
        "perimeter": perimeter,
        "circularity": circularity,
        "aspect_ratio": aspect_ratio
    }