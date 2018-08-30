# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2018/8/30 9:17'

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams


def convert(filename):
    outfile = filename + '.txt'
    args = [filename]

    rsrcmgr = PDFResourceManager()
    outfp = file(outfile, 'w')
    device = TextConverter(rsrcmgr, outfp, codec='utf-8', laparams=LAParams())

    for fname in args:
        fp = file(fname, 'rb')
        process_pdf(rsrcmgr, device, fp, pagenos=set(), maxpages=0, password='', check_extractable=True)
        fp.close()

    device.close()
    outfp.close()


if __name__ == '__main__':
    convert('g:/a.pdf')