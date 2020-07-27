import os
import psycopg2
import urllib.request
from PIL import Image
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template, send_file
from werkzeug.utils import secure_filename
from osgeo import gdal
from app.image_render import image_render
from app import app
from app.forms import BandForm, UploadForm






@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def select_image():
    form = UploadForm()
    
    if form.validate_on_submit():
        
        if 'file' not in request.files:
            
            flash('No file part')
            return render_template('index.html', form=form)
        file = request.files['file']
        if file.filename == '':
            
            flash('No image selected for uploading')
            return render_template('index.html', form=form)
        if file:
            filename = secure_filename(file.filename)
            # commeting out save for development, suggested is selecting a file with the 
            # same name as .tif that isnt a .tif because of how big they are
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            fname, extension = os.path.splitext(filename)
           
            folder = 'app/static/uploads/' + fname
            if not os.path.exists(folder):
                os.makedirs(folder)
            return redirect(url_for('bands', imagefolder=fname)) 
            #render_template('section.html',title="Select Band", form=BandForm(), fname=fname)
    return render_template('index.html', form=form)





"""
when the form is submitted requesting an image
this function is called and render and saves the band requested
"""
@app.route('/<imagefolder>/', methods=['GET', 'POST'])
@app.route('/<imagefolder>', methods=['GET', 'POST'])
def bands(imagefolder):

    def section_image(fname):
        name = fname + '.tif'
        name = os.path.join(app.config['UPLOAD_FOLDER'],name)
        image = image_render(name,False)
        section = "section_1"
        fname = fname + '/' + section
        folder = 'app/static/uploads/' + fname
        if not os.path.exists(folder):
            os.makedirs(folder)
        return image, fname, section
    
    image_section, fname, section = section_image(imagefolder)
    
    form = BandForm()
    str_band = "Select band"
    filename = None
    if form.validate_on_submit():
        rgb = form.rgb.data
        band = form.band_num.data
        if rgb or band is not None:
            str_band = 'Band_' + str(band)
            # if not rgb show the band requested`
            if not rgb:
                # naming the file and checking to make sure it has not already 
                # been created
                filename = imagefolder + '_' + section + '_' + str(band) + '.jpg'
                filepath = os.path.join(app.config['UPLOAD_FOLDER'],fname, filename)
                
                if not os.path.exists(filepath): 
                    # run render_image class
                    # run render_image class
                    rend_image = image_section.band(band)
                    
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
                str_band = 'RGB band'
                filename = imagefolder + '_' + section + '_321.jpg'
                filepath = os.path.join(app.config['UPLOAD_FOLDER'],fname,filename)
                
                
                # if the file has not been created, create it otherwise skip
                if not os.path.exists(filepath): 
                    # run render_image class
                    #name = fname + '.tif'
                    #name = os.path.join(app.config['UPLOAD_FOLDER'],name)
                    #image = image_render(name,False)
                    rend_image = image_section.s2_to_rgb()
                
                    # turn array into image
                    complete_image = Image.fromarray(rend_image)
            
            # if the file had not already been created save it
            # saving file as band number (321 for rgb) in the UPLOAD_FOLDER
            if not os.path.exists(filepath): 
                complete_image.save(filepath)
    # clearing forms
    form.band_num.data = None
    form.rgb.data = False
    print("here")
    
    print(imagefolder)
    print(section)
    print(filename)
    return render_template('section.html', title=str_band, form=form, filename=filename, imagefolder=imagefolder, section=section)
    

"""
access to the image where it is saved in order to display it
"""    
@app.route('/<imagefolder>/<section>/<filename>')
def display_image(filename, section, imagefolder):
	# getting where the image is saved to display it
    full_filename = 'uploads/' + imagefolder + '/' + section + '/' + filename
    print(full_filename)
    return redirect(url_for('static', filename=full_filename), code=301)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    