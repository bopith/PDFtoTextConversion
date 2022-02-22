import os

from pdf2image import convert_from_path
from timeit import default_timer as timer


def pdf_to_images(pdf, path):
    """
    This function convert a pdf file into multiple images as inputs for text extraction.
    :param pdf_file_path: path to the pdf file
    :param output_path: path to the output images
    :return: images of individual page split from the pdf file
    """

    pdf_file_path = f'input/{pdf}.pdf'
    output_path = f'{path}/{pdf}'
    try:
        os.makedirs(output_path)
    except OSError:
        if not os.path.isdir(output_path):
            raise

    # Convert PDF to images
    try:
        images = convert_from_path(pdf_file_path, dpi=500)

        counter = 1
        for page in images:
            idx = os.path.join(output_path, f"{pdf}_{counter}.jpg")
            page.save(idx, 'JPEG')
            print("save image:", idx)
            counter += 1
    except Exception as e:
        print(f"pdf cannot be converted to images: {e}")


def main():
    # Constants
    pdf_filename = 'term_paper'
    image_path = 'input/images/'

    start = timer()
    pdf_to_images(pdf_filename, image_path)
    print("Conversion period:", timer() - start, "seconds")


if __name__ == '__main__':
    main()
