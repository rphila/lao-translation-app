#!/usr/bin/env python

from flask import Flask, render_template, url_for, make_response, request, flash, redirect
import base64
import util
import os
import logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    trans_text = ""
    ocr_text = ""
    data_uri=""
    filename=""
    if request.method == 'POST':
        # check if image uploaded
        if 'imgtext' not in request.files:
            app.logger.error('No image file in request')
            return 'Fail: Go back, No image file in request'

        img_text = request.files['imgtext']
        filename = img_text.filename

        if img_text.filename == '':
            app.logger.error('No image uploaded')
            return 'Fail: Go back, and upload an image file'


        img_text.save(os.path.join("/app/temp", 'img.jpg'))
        ocr_text = util.perform_ocr()
        trans_text = util.translate_text(ocr_text)
       # return redirect('/')

        data_uri = base64.b64encode(open(os.path.join("/app/temp", 'img.jpg'), 'rb').read()).decode('utf-8')
        img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)

    return render_template("input.html",
                           file=data_uri,
                           file_name=filename,
                           ocr_text=ocr_text,
                           translated_text=trans_text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)