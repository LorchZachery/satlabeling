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
from app.azure_connect import Azure_Connect, Azure_Upload
from app.database import Database


azure = Azure_Connect("scihub")
azure.get_file_info()
Paths = azure.get_paths()
Files = azure.get_files()
azure_upload = Azure_Upload("imagebands/uploads")
database = Database()
"""
Displays home index page, just to get it started
"""
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    print("here inex")
    form = BandForm()
    str_band = "Select band"
    name = None
    form.band_num.data = None
    form.rgb.data = False
    if form.validate_on_submit():
        filename=Paths[0]
        number = "0"
        return redirect(url_for('bands', number=number), code=302)
    return render_template('index.html', title=str_band, form=form, name=name, number=None)



"""
function to orgainize code, gets the rgb band of the imgae
"""
def get_rgb_info(number):
    # giving the file a name for later
    filename = Paths[number]
    str_band = 'RGB band'
    name = Files[number].split('/')[3].split('.')[0] + '_321'+ '.jpg'
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], name)
    complete_image = None
    # if the file has not been created, create it otherwise skip
    if not azure_upload.exists(name): 
        # run render_image class
        image = image_render(filename,False)
        rend_image = image.s2_to_rgb()
    
        # turn array into image
        complete_image = Image.fromarray(rend_image)
    return str_band, filepath, name, complete_image

"""
when the form is submitted requesting an image
this function is called and render and saves the band requested
"""
@app.route('/<number>', methods=['GET', 'POST'])
@app.route('/<number>/', methods=['GET', 'POST'])
def bands(number):
    print("here bands")
    print(number)
    if number:
        number = int(number)
    form = BandForm()
    str_band = "Select band"
    name = None
    filename = Paths[number]
    if form.validate_on_submit():
        
        rgb = form.rgb.data
        band = form.band_num.data
        if rgb or band is not None:
            str_band = 'Band' + str(band)
            # if not rgb show the band requested
            if not rgb:
                # naming the file and checking to make sure it has not already 
                # been created
                name = Files[number].split('/')[3].split('.')[0] + '_' + str(band)+ '.jpg'
                filepath = os.path.join(app.config['UPLOAD_FOLDER'],name )
                
                if not azure_upload.exists(name): 
                    # run render_image class
                    # run render_image class
                    image = image_render(filename,False)
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
                str_band, filepath, name, complete_image = get_rgb_info(number)
                
            # if the file had not already been created save it
            # saving file as band number (321 for rgb) in the UPLOAD_FOLDER
            if not azure_upload.exists(name):
                complete_image.save(filepath)
                azure_upload.upload_file(filepath,name)
                os.remove(filepath)
    #make rgb the default for better viewing
    if name is None:
        str_band, filepath, name, complete_image = get_rgb_info(number)
        # if the file had not already been created save it
        # saving file as band number (321 for rgb) in the UPLOAD_FOLDER
        if not azure_upload.exists(name):
                complete_image.save(filepath)
                azure_upload.upload_file(filepath,name)
                os.remove(filepath)
    
    # sending to database the label

    default_name = '0'
    label = request.form.get('label',default_name)
    if label!='0':
        id = Files[number].split('/')[3].split('.')[0] + '_sectioned.tif'
        database.add_data(id, 1, label)
   
    # clearing forms
    form.band_num.data = None
    form.rgb.data = False
    utm = None
    year = None
    date = None
    file = None
    url = None
    # if a number (image) is requested, give the information about the image 
    # to the html file index.html
    if (number or number==0) and (name is not None):
        info = Files[number].split('/')
        utm = info[0]
        year = info[1]
        date = info[2]
        file = info[3]
        url = azure_upload.get_img_url_with_blob_sas_token(name)
    print(url)
    return render_template('index.html', title=str_band, form=form,name=name, number=number, utm=utm, year=year, date=date, file=file, url=url )
    

"""
navigation to next and prev images
"""
@app.route('/<command>/<number>')
def nav_image(command, number):
    number = int(number)
    if len(Paths) <= (number + 1):
        flash("last image in list")
        return redirect(url_for('bands', number=number), code=302)
    
    if command == 'next':
        return redirect(url_for('bands', number=number + 1), code=302)
    
    else:
        if (number -1) < 0:
            flash("This is the first image in the list")
            return redirect(url_for('bands', number=number), code=302)
        return redirect(url_for('bands', number=number-1), code=302)
        
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    