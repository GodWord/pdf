# -*- coding:utf-8 -*-


__author__ = 'zhoujifeng'
__date__ = '2018/8/30 10:25'

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf


def convert_pdf(path, page=1):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, pageno=page, laparams=laparams)

    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()

    str = retstr.getvalue()
    retstr.close()
    return str


file = r'重新发现官僚制西方公共行政理论对官僚制的再思考.pdf'
with open('test.txt', 'a') as f:
    f.write(convert_pdf(file))
print(convert_pdf(file))
