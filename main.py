
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
           

def convertImageToBinary(args):
    image = Image.open(args.image)
    imageData = image.tobytes()
    return imageData

def convertBinToImage(args):
    with open(args.binary, "rb") as f:
        binaryCollections = f.read()
    if not args.fullColour:
        print("Using single colour")
        dimensions =  image_dimensions(len(binaryCollections))
        image = Image.frombytes('L',dimensions,binaryCollections)
    else:
        print("Using colour")
        dimensions =  image_dimensions(int(len(binaryCollections)/3))
        print(dimensions)
        image = Image.frombytes('RGB',dimensions,binaryCollections)
    return image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("binary", help="The path to the binary/data")
    parser.add_argument("image", help="The path to the image")
    parser.add_argument("output", help="The direction to convert the data (Either: 'image' or 'binary')")
    parser.add_argument("-rgb","--fullColour",action="store_true",required=False,help="Store the data in the colour bands, not just greyscale",dest="fullColour")
    args = parser.parse_args()

    if args.output == "image":
        output = convertBinToImage(args)
        output.save(args.image)
    elif args.output == "binary":
        output = convertImageToBinary(args)
        with open(args.binary,"wb+") as f:
            f.write(output)

    else:
        print("Unknown arg for output: ",args.output)


if __name__ == '__main__':
    main()
