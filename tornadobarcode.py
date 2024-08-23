# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
from reportlab.graphics.barcode import createBarcodeImageInMemory


class BarcodeGenerator(tornado.web.RequestHandler):
    '''
    https://docs.reportlab.com/reportlab/userguide/ch1_intro/
    https://docs.reportlab.com/reportlab/barcode/
    https://www.tornadoweb.org/en/stable/

    Barcode Types: 
        EAN8, EAN13, EAN5, ISBN, UPCA, QR, Code128, Code128Auto
        Standard39, Standard93, MSI, Codebar, Code11, FIM, POSTNET
        Extended39, Extended93, I2of5, ECC200DataMatrix

    '''
    def get(self):
        # you can also review my previous example:
        # https://github.com/xdevsoft/barcodegen
        barcode = createBarcodeImageInMemory(
            'Code128',                  # Refer to barcode types 
            value='123456789012',       # code to be encoded/printed
            width=300, 
            height=60,
            format='png'                # png, gif, tiff
        )

        self.write(barcode)
        # we need to tell the web client regarding our content type
        self.set_header("Content-type",  "image/png")


application = tornado.web.Application([
    (r"/", BarcodeGenerator),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()