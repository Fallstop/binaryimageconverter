
import sys
from PIL import Image
import argparse

def convertImageToBinary(filename):
    image = Image.open(filename)
    imageData = image.tobytes()
    return imageData

def convertBinToImage(filename):
    with open(filename, "rb") as f:
        binaryCollections = f.read()
    return Image.frombytes('L', (len(binaryCollections), 1),binaryCollections)


def main():
    inputBinary = sys.argv[1]
    outputImage = sys.argv[2]

    parser = argparse.ArgumentParser()
    parser.add_argument("binary")
    parser.add_argument("image")
    parser.add_argument("output")
    args = parser.parse_args()

    if args.output == "image":
        output = convertBinToImage(args.binary)
        output.save(args.image)
    elif args.output == "binary":
        output = convertImageToBinary(args.image)
        with open(args.binary,"wb+") as f:
            f.write(output)

    else:
        print("Unknown arg for output: ",args.output)


if __name__ == '__main__':
    main()
