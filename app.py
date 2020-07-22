import os
import psycopg2
import urllib.request
from PIL import Image
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
from image_render import image_render


UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
fname = "static/uploads/test.tif"


app = Flask(__name__)
app.secret_key = "secret key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def upload_form():
    return render_template('image.html')

@app.route('/', methods=['POST'])
def display_band():
   
    str_band = request.form['band']
    if str_band != '': band = int(str_band)
    
    str_rgb = request.form['rgb']
    if str_rgb != '': rgb = int(str_rgb)
    
    if rgb == 0:
        
        if band < 0:
            flash('No valied band selected')
            return redirect(request.url)
        else:
            # run render_image class
            image = image_render(fname,True)
            rend_image = image.band(band)
            im = Image.fromarray(rend_image)
            
            #image.show()
            #print('upload_image filename: ' + filename)
            
    else:
        str_band = '321'
        band = 321
        image = image_render(fname,True)
        rend_image = image.s2_to_rgb()
        im = Image.fromarray(rend_image)
    
    filename = os.path.join(app.config['UPLOAD_FOLDER'], str_band)
    im.save(filename + '.jpg')
       
    return render_template('image.html', band=band)
        
@app.route('/image/<band>')
def display_image(band):
	#print('display_image filename: ' + filename)
    print("here5")
    return redirect(url_for('static', filename='uploads/' + band + '.jpg'), code=301)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    