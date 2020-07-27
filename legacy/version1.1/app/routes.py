import os
import psycopg2
import urllib.request
from PIL import Image
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
from app.image_render import image_render
from app import app
from app.forms import BandForm


fname = "test"


"""
when the form is submitted requesting an image
this function is called and render and saves the band requested
"""
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def bands():
    form = BandForm()
    str_band = "Select band"
    filename = None
    if form.validate_on_submit():
        rgb = form.rgb.data
        band = form.band_num.data
        if rgb or band is not None:
            str_band = 'Band' + str(band)
            # if not rgb show the band requested`
            if not rgb:
                # naming the file and checking to make sure it has not already 
                # been created
                filename = fname + '_' + str(band) + '.jpg'
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                
                if not os.path.exists(filepath): 
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
                print("here")
                # giving the file a name for later
                str_band = 'RGB band'
                filename = fname + '_321.jpg'
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                
                
                # if the file has not been created, create it otherwise skip
                if not os.path.exists(filepath): 
                    # run render_image class
                    name = fname + '.tif'
                    name = os.path.join(app.config['UPLOAD_FOLDER'], name)
                    image = image_render(name,False)
                    rend_image = image.s2_to_rgb()
                
                    # turn array into image
                    complete_image = Image.fromarray(rend_image)
            
            # if the file had not already been created save it
            # saving file as band number (321 for rgb) in the UPLOAD_FOLDER
            if not os.path.exists(filepath): 
                complete_image.save(filepath)
    # clearing forms
    form.band_num.data = None
    form.rgb.data = False
    return render_template('index.html', title=str_band, form=form, filename=filename)
    

"""
access to the image where it is saved in order to display it
"""    
@app.route('/images/<filename>')
def display_image(filename):
	# getting where the image is saved to display it    
    return redirect(url_for('static', filename='uploads/' + filename), code=301)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    