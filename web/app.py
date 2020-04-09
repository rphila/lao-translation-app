#!/usr/bin/env python
from pytesseract import pytesseract as pt
from flask import Flask, render_template, url_for, make_response, request, flash, redirect
from google.cloud import translate_v2 as translate
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
        ocr_text = perform_ocr()
        trans_text = translate_text(ocr_text)
       # return redirect('/')
    return render_template("input.html", trans=trans_text)


def perform_ocr():
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



#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="c:/dev/laolessons/lao-translation-app/GoogleTranslate Project-4778da0a83ca.json"
#print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])

def translate_text(text):
    translate_client = translate.Client()

   # text="ສະບາຍດີ "
    result = translate_client.translate(
        text, target_language="en")

   # print(u'Text: {}'.format(result['input']))
   # print(u'Translation: {}'.format(result['translatedText']))
    #print(u'Detected source language: {}'.format(
    #    result['detectedSourceLanguage']))

    return result['translatedText']


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)