# Project Name

## Description

This project is a demonstration of barcode detection and decoding. It includes two modes of operation:
1. **Decode-only**: Uses a pre-trained model to decode barcodes from images.
2. **YOLO Detector**: Uses a YOLO model to detect and decode barcodes from images, requiring pre-trained weights.

## Installation (macOS)

1. Install zbar using Homebrew:
   ```sh
   brew install zbar
   ```

2. Create a virtual environment and install the required dependencies:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Set the `DYLD_LIBRARY_PATH` environment variable:
   ```sh
   export DYLD_LIBRARY_PATH=$(brew --prefix zbar)/lib
   ```

## Running the Project

1. Install the required Python packages:
   ```sh
   pip install python-barcode pillow
   ```

2. Generate a test barcode image:
   ```sh
   python -c "import barcode; from barcode.writer import ImageWriter; barcode.get('ean13', '246528561310', writer=ImageWriter()).save('sample')"
   ```

3. Run the main script with the generated image:
   ```sh
   python -m src.main sample.png
   ```

   **Example Output:**
   ```
   [EAN13] 2465285613105
   {'box_id': 'box-001', 'barcodes': [{'data': '2465285613105', 'type': 'EAN13'}]}
   ```

## Running Tests

Run the tests using pytest:
