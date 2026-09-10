import sys
import cv2
from src.vision.decoder import decode_frame
from src.vision.detector import BarcodeDetector
from src.core.processor import BoxAggregator


def process_image(path, detector, aggregator):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(path)
    for x, y, w, h in detector.rois(image):
        roi = image[y:y + h, x:x + w]
        results = decode_frame(roi)
        aggregator.add(results)
        for r in results:
            print(f"[{r.type}] {r.data}")


def main():
    paths = sys.argv[1:]
    if not paths:
        print("usage: python -m src.main <image> [image ...]")
        return
    detector = BarcodeDetector()
    aggregator = BoxAggregator(box_id="box-001")
    for p in paths:
        process_image(p, detector, aggregator)
    print(aggregator.payload())


if __name__ == "__main__":
    main()