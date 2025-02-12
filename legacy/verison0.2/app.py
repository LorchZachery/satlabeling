import os
import psycopg2
import urllib.request
from PIL import Image
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
from image_render import image_render
from forms import BandForm

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
fname = "test"

app = Flask(__name__)
app.secret_key = "secret key"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

"""
uploads the basic form before an image is selected
"""
@app.route('/')
def upload_form():
    return render_template('image.html')

"""
when the form is submitted requesting an image
this function is called and render and saves the band requested
"""
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
            
            # error handling if band outside of range
            if rend_image is False:
                flash("Band outside of range")
                return redirect(request.url)
            else:
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
    

"""
access to the image where it is saved in order to display it
"""    
@app.route('/image/<band>')
def display_image(band):
	# getting where the image is saved to display it    
    return redirect(url_for('static', filename='uploads/' + fname + '_' + band + '.jpg'), code=301)


"""
dev work
"""
@app.route('/test')
def form_test():
    form = BandForm()
    return render_template('test.html', title='Testing', form=form)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    