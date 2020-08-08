import os
import psycopg2
import urllib.request
from PIL import Image
import numpy as np
from binascii import a2b_base64
import base64
from io import BytesIO
import cv2

from flask import Flask, flash, request, redirect, url_for, render_template, send_file, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    print(os.getcwd())
    return render_template('draw.html')
       
@app.route('/get_post_json', methods=['POST'])
def get_post_json():    
    data = request.form['canvas_data']
    print(data)
    response = urllib.request.urlopen(data)
    with open('image.png', 'wb') as f:
        f.write(response.file.read())
        
    im = Image.open('image.png')
    
    ni = np.array(im)
    
    color = ni[:,:,2] > 1
    
    Image.fromarray((color*255).astype(np.uint8)).save('result.png')
    
    return jsonify(status="success", data=data)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)