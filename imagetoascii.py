from PIL import Image, ImageOps
import argparse


def get_args():
    # Creates the parser
    parser = argparse.ArgumentParser(prog="imagetoascii", description="Converts an image to ASCII art.")
    # Define the arguments.
    parser.add_argument("path", metavar="path", type=str, help="The path to the image you want to make into ASCII art.")

    arguments = parser.parse_args()
    return arguments


def turn_to_greyscale(path: str):
    with Image.open(path) as image:
        gray_image: Image = ImageOps.grayscale(image)
        gray_image.show()


if __name__ == "__main__":
    args = get_args()
    path = args.path
    print(path)
    turn_to_greyscale(path)

