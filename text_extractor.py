import pytesseract
import os
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'D:\\Document\\Vannaro\\Projects\\OCR\\Tesseract-OCR\\tesseract.exe'


def images_to_text(pdf, start_page, end_page, dimension, input_path, output_path):
    """
    This function first crop the image to obtain only in-line text (exclude page number and header).
    Then using pytesseract to extract text from each image and write into a single text file.
    """
    file = open(os.path.join(output_path, f"{pdf}_{start_page}_{end_page}.txt"), "w")

    for i in range(start_page, end_page + 1):
        idx = os.path.join(input_path, f"{pdf}/{pdf}_{i}.jpg")
        print("get text from image:", idx)
        image = Image.open(idx)
        cropped_image = image.crop(dimension)
        text = str(pytesseract.image_to_string(cropped_image))
        file.write(text)
    file.close()


def main():
    # Constants
    pdf_filename = 'term_paper'
    start_page = 1
    end_page = 12
    crop_dimension = [150, 500, 3900, 5400]  # (left, top, right, bottom)
    image_path = 'input/images/'
    output = 'output'

    images_to_text(pdf_filename, start_page, end_page, crop_dimension, image_path, output)


if __name__ == '__main__':
    main()
