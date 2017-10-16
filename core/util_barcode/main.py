# coding:utf-8

import barcode
import base64
from barcode.writer import ImageWriter
import StringIO
from PIL import Image

def createbarcodebase64(str=''):
    try:
        EAN = barcode.get_barcode_class('ean13')
        ean = EAN(str, writer=ImageWriter())
        disk = open("result.png","wb")
        fp = StringIO.StringIO()
        ean.write(fp)
        ean.write(disk)
        image = base64.b64encode(buffer(fp.getvalue()))
    except Exception, e:
        return ""
    return image

def barcode_decode(img):
    try:
        import zbarlight
        img = Image.open(img)
        scan_result = zbarlight.scan_codes("ean13", img)
    except Exception as e:
        print e
    else:
        print scan_result
        if scan_result:
            return " ".join(scan_result)
        else:
            return ""

print barcode_decode("./result.png")




