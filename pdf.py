# -*- coding:utf-8 -*-
import os
from datetime import datetime

__author__ = 'zhoujifeng'
__date__ = '2018/8/30 9:12'

from io import StringIO
from io import open

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

PATH = r"论政府从官僚制向合作制的转变.pdf"


# PATH = r"重新发现官僚制西方公共行政理论对官僚制的再思考.pdf"


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


def saveTxt(txt):
    with open(file_name, "a", encoding='gb18030') as f:
        f.write(txt)


if __name__ == '__main__':
    time_start = datetime.now()
    print('-----------------------转换开始-----------------------')
    file_name = os.path.split(PATH)[1].replace('pdf', 'txt')

    txt = readPDF(open(PATH, 'rb'))

    print('-----------------------转换结束-----------------------')
    print('-----------------------正在写入-----------------------')
    print(txt)
    saveTxt(txt)
    print('-----------------------写入完成-----------------------')
    time_stop = datetime.now()
    print('共耗时：', str(time_stop - time_start).split('.')[0])
