# coding:utf-8

import argparse
from PIL import Image


def handle_command():
    '命令行参数处理'
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='图片的路径')
    parser.add_argument('-o', '--output', help='是否输出文件')
    parser.add_argument('--width', type=int, default=80)
    parser.add_argument('--heigth', type=int, default=80)

    # 获取命令行参数
    return parser.parse_args()


args = handle_command()


class Ptrancefrom(object):

    def __init__(self, img, width, heigth):
        self.img = img
        self.width = width
        self.heigth = heigth
        self.ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

    def get_char(self, r, b, g, alpha=256):
        if alpha == 0:
            return ' '

        length = len(self.ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1) / length
        return self.ascii_char[int(gray / unit)]

    def print_picture(self):
        im = Image.open(self.img)
        im = im.resize((self.width, self.heigth), Image.NEAREST)
        txt = ""

        for i in range(self.heigth):
            for j in range(self.width):
                txt += self.get_char(*im.getpixel((j, i)))

            txt += '\n'

        print txt
        return txt

    def write_to_file(self):
        txt = self.print_picture()
        if args.output:
            with open(args.output, 'w') as f:
                f.write(txt)
        else:
            with open('output.txt', 'w') as f:
                f.write(txt)

pic = Ptrancefrom(args.filename, args.width, args.heigth)
pic.print_picture()

