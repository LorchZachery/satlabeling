from image_render import image_render

if __name__ == "__main__":
    fname = "test.tif"
    image = image_render(fname,True)
    image.band(12)
    image.show()
# make sectioning function for each part of the image when not doing 
# the whole image
