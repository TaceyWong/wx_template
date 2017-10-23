# coding:utf-8

"""
1、图片旋转、统一正则化（横向水平，统一大小）
2、图片蒙版（屏蔽掉无关信息）
    + 分片裁剪
    + 或 添加分割标志，位置标识
3、接口封装
"""
from PIL import Image

from requests import Session


def crop(img, boxs):
    img = Image.open(img)
    result = []
    for box in boxs:
        result.append(img.crop(box))
    return result


def thumbnail(img, w, h):
    img = Image.open(img)
    img.thumbnail((w, h), Image.ANTIALIAS)
    return img


class OCROnlineBase(object):
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    index_url = ""
    request = Session()

    def init_request(self):
        headers = {
            "user-agent": self.ua
        }
        self.request.get(self.index_url, headers=headers)

    def upload_pic(self, pic_file):
        pass

    def get_result(self):
        pass

    def start_convert(self):
        pass

    def run(self):
        pass


class WDOCR(OCROnlineBase):
    index_url = "http://ocr.wdku.net/"

    def upload(self, img):
        upload_url = "http://api.wdku.net/ocr/Upload.php"
        files = {'file': open(img, 'rb')}
        self.request.post(upload_url, files=files)

    def run(self):
        self.init_request()


class PDFDOOCR(OCROnlineBase):
    index_url = "http://www.pdfdo.com/image-to-txt.aspx"
