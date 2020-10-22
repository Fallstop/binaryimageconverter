
import sys
from PIL import Image
import argparse
import math


def image_dimensions(x):
    output = []
    for i in range(1, x + 1):
        if x % i == 0:
            output.append(i)
    center = output[len(output)//2]
    return (x//center, center)
           

def convertImageToBinary(filename):
    image = Image.open(filename)
    imageData = image.tobytes()
    return imageData

def convertBinToImage(filename):
    with open(filename, "rb") as f:
        binaryCollections = f.read()
    dimensions =  image_dimensions(len(binaryCollections))
    return Image.frombytes('L',dimensions,binaryCollections)


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
