# coding:utf-8

from PIL import Image


def create_ico(img):
    img = Image.open(img)
    img.save("result.ico")


create_ico("./result.png")