from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import PyPDF2
import datetime
import random
import fitz
import datetime
import random
import sys
now = datetime.datetime.now()

import pdf2image
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Users\My\AppData\Local\Tesseract-OCR\tesseract.exe"

app = Flask(__name__, static_folder='', static_url_path='')


@app.route('/pdf1')
def upload_file():
    return render_template('pdf.html')
@app.route('/pdfdata1', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
            f=request.files['file']
            f.save(f.filename)
            images = pdf2image.convert_from_path(f.filename)
            text = " "
            for pg, img in enumerate(images):
               text = text + pytesseract.image_to_string(img)
            date = str(now.strftime("%Y-%m-%d"))
            rand = str(random.randint(1, 10000))
            seq = date + rand
            file_name_pdf = 'output_data' + seq + '.txt'
            with open(file_name_pdf,'w') as fo:
             fo.write(text)
             fo.close()
    return "Successfully data extracted file is save"
if __name__=='__main__':
    app.run(debug=True)