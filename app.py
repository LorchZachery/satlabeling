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
fname = "test"

app = Flask(__name__)
app.secret_key = "secret key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/')
def upload_form():
    return render_template('image.html')


@app.route('/', methods=['POST'])
def display_band():
    # getting bnad value from form
    str_band = request.form['band']
    if str_band != '': band = int(str_band)
    
    # checking if rgb is requested
    str_rgb = request.form['rgb']
    if str_rgb != '': rgb = int(str_rgb)
    
    # if not rgb show the band requested`
    if rgb == 0:
        if band < 0:
            flash('No valied band selected')
            return redirect(request.url)
        else:
            # naming the file and checking to make sure it has not already 
            # been created
            filename = fname + '_' + str_band + '.jpg'
            filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
       
            if not os.path.exists(filename): 
                # run render_image class
                # run render_image class
                name = fname + '.tif'
                name = os.path.join(app.config['UPLOAD_FOLDER'], name)
                image = image_render(name,False)
                rend_image = image.band(band)
            
                #turn array into image
                complete_image = Image.fromarray(rend_image)
            
            
    # if rgb is requested       
    else:
        # giving the file a name for later
        str_band = '321'
        band = 321
        filename = fname + '_' + str_band + '.jpg'
        filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        
        # if the file has not been created, create it otherwise skip
        if not os.path.exists(filename): 
            # run render_image class
            name = fname + '.tif'
            name = os.path.join(app.config['UPLOAD_FOLDER'], name)
            image = image_render(name,False)
            rend_image = image.s2_to_rgb()
        
            # turn array into image
            complete_image = Image.fromarray(rend_image)
    
    # if the file had not already been created save it
    # saving file as band number (321 for rgb) in the UPLOAD_FOLDER
    if not os.path.exists(filename): 
        complete_image.save(filename)
       
    return render_template('image.html', band=band)
        
@app.route('/image/<band>')
def display_image(band):
	# getting where the image is saved to display it    
    return redirect(url_for('static', filename='uploads/' + fname + '_' + band + '.jpg'), code=301)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    