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

1. Generate a test barcode image:
   ```sh
   python -m python_barcode code128 "123456789012" > sample.png
   ```

2. Run the main script with the generated image:
   ```sh
   python -m src.main sample.png
   ```

   **Example Output:**
   ```
   Decoding barcode from sample.png
   Decoded barcode: 123456789012
   ```

## Running Tests

Run the tests using pytest:
