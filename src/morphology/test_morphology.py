import cv2

from morphology import extract_features
from screening import classify_cell


mask = cv2.imread(
    "data/test_masks/test.png",
    cv2.IMREAD_GRAYSCALE
)

features = extract_features(mask)

print(features)

result = classify_cell(features)

print(result)