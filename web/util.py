from pytesseract import pytesseract as pt
from google.cloud import translate_v2 as translate
import codecs
import logging


def perform_ocr():

    pt.run_tesseract('/app/temp/img.jpg', 'file_ocr',  extension=".jpg", lang='lao')

    txt = ""
    with codecs.open("/app/file_ocr.txt", encoding="utf-8") as f:
        for line in f:
            txt += line + '\n'

    return txt


def translate_text(text):

    translate_client = translate.Client()

    result = translate_client.translate(text, target_language="en")

    logging.debug("Input: " + result['input'])
    logging.debug("Detected source language: " + result['detectedSourceLanguage'])
    logging.debug("Translation: " + result['translatedText'])
    return result['translatedText']