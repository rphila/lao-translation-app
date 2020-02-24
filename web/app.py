#!/usr/bin/env python
from pytesseract import pytesseract as pt
from flask import Flask, render_template, url_for, make_response, request, flash, redirect
import datetime
import os
import codecs
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    trans_text = ""
    if request.method == 'POST':
        img_text = request.files['imgtext']

        img_text.save(os.path.join("/app/temp", 'img.jpg'))
        trans_text = ocr()
       # return redirect('/')
    return render_template("input.html", trans = trans_text)


def ocr():
    pt.run_tesseract('/app/temp/img.jpg', 'file_ocr',  extension=".jpg", lang='lao') #'eng')

    txt = ""
    with codecs.open("/app/file_ocr.txt",encoding="utf-8") as f:
        for line in f:
            txt += line

  #  f = open("/app/file_ocr.txt",'r') 
  #  logging.debug(f.read())
  #  print("TEST", flush=True)
  #  txt = f.read()
  #  f.close()
  
    return txt


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)