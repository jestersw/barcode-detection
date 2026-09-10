class BoxAggregator:
    def __init__(self, box_id):
        self.box_id = box_id
        self._codes = {}

    def add(self, results):
        for r in results:
            self._codes[r.data] = r.type

    def payload(self):
        return {
            "box_id": self.box_id,
            "barcodes": [{"data": d, "type": t} for d, t in self._codes.items()],
        }