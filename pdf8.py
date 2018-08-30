# -*- coding:utf-8 -*-
__author__ = 'zhoujifeng'
__date__ = '2018/8/30 13:35'

import multiprocessing
import os


def pdf2text(pdfName):
    if "pdf" in pdfName:
        txtName = pdfName.replace("pdf", "txt")
        try:
            os.system("python C:/Python27/Scripts/pdf2txt.py -o {} {}".format(txtName, pdfName))
        except Exception:
            print("ERROR: ", pdfName)


if __name__ == "__main__":
    fNames = os.listdir('./')
    pdfNames = [fName for fName in fNames if '.pdf' in fName]
    pool = multiprocessing.Pool(processes=4)
    pool.map(pdf2text, pdfNames)
