from image_render import image_render

if __name__ == "__main__":
    fname = "test_image.tif"
    image = image_render(fname,True)
    image.band(12)
    image.show()
