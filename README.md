# PDF to Text Conversion
This repository contains the scripts to generate texts from PDF files.

Despite using some particular libraries for PDF to text such as pypdf2 and PDFminer, 
pdf2image and Tesseract are the main libraries for this project. 

We divide the process into 2 main steps in order to extract only the main text and 
ignore unnecessary text in the page header and footer.

## Libraries

- pdf2image: 1.16.0
- pytesseract: 0.3.6

## Process
1. Run `ocr.py` to generate multiple images from a given PDF file.
2. Run `text_to_speech.py` to convert those images into a text file.

Or simply run `main.py` to automatically generate text file from a given PDF file.

