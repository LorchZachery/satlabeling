from image_render import image_render

if __name__ == "__main__":
    fname = "C://Users//Cadet_Admin//Desktop//sat_labeling//static//uploads//test.tif"
    image = image_render(fname,False)
    image.band(1)
    image.show()
# make sectioning function for each part of the image when not doing 
# the whole image
