from pywhatkit import ascii_art
import argparse


# Creates the parser and returns it.
def get_args():
    # Creates the parser
    parser = argparse.ArgumentParser(prog="imagetoascii", description="Converts an image to ASCII art.")
    # Define the arguments.
    parser.add_argument("path", metavar="path", type=str, help="The path to the image you want to make into ASCII art.")

    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    args = get_args()
    path: str = args.path

    # Turns the image into ASCII art.
    ascii_art.image_to_ascii_art(path, "ascii"+path)
