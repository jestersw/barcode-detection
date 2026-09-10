from dataclasses import dataclass
from pyzbar import pyzbar


@dataclass(frozen=True)
class BarcodeResult:
    data: str
    type: str
    polygon: tuple


def decode_frame(image):
    results = []
    for d in pyzbar.decode(image):
        polygon = tuple((p.x, p.y) for p in d.polygon)
        results.append(BarcodeResult(d.data.decode("utf-8", "replace"), d.type, polygon))
    return results