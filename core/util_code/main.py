# coding:utf-8


import hashlib
import base64


def md5_encode(text=""):
    md5 = hashlib.md5()
    md5.update(text)
    return md5.hexdigest()


def base64_encode(text=""):
    return base64.b64encode(text)


def base64_pic(img):
    f = open(img, 'rb')
    return base64.b64encode(f.read())


def base64_decode(text=""):
    return base64.b64decode(text)


print base64_pic("./result.png")
