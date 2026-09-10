class BarcodeDetector:
    def __init__(self, weights=None):
        self.model = None
        if weights:
            try:
                from ultralytics import YOLO
                self.model = YOLO(weights)
            except Exception:
                self.model = None

    def rois(self, image):
        h, w = image.shape[:2]
        if self.model is None:
            return [(0, 0, w, h)]
        boxes = []
        for r in self.model(image, verbose=False):
            for b in r.boxes.xyxy.cpu().numpy().astype(int):
                x1, y1, x2, y2 = b
                boxes.append((x1, y1, x2 - x1, y2 - y1))
        return boxes or [(0, 0, w, h)]