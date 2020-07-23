# DEV VERSION
import os
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
from skimage import exposure


class image_render:
    """
    The image_render object will render different types of bands of an image 
    for the .tif image formate

    """
    
    def __init__(self, fname, normal_size=True):
        # print(gdal.__version__)
        # opens the whole file
        if normal_size:
            # opening .tif file up to read it and extract bands
            ds = gdal.Open(fname)
            self.data = ds.ReadAsArray()
        # opens a section of the file
        else:
            # TODO: have each section of the file open up for viewing
            self.data = self.tiff_read(fname,0, 1000, 0, 1000)
            
        print(self.data.shape)
        
    def tiff_read(self,fname: str, bands: list=[]) -> np.ndarray:
        """
        Reads a sub-section of the tiff array.  This call 
        > x = tiff_read(fname, i1, i2, j1, j2)
        is equivalent to
        > # read the full image
        > x = x[i1:i2, j1:j2, ...]
        except of course that the first call is much faster and more memory efficient.
        """
        if not os.path.exists(fname):
            raise(FileNotFoundError("<%s> doesn't exist" % fname))
        ds = gdal.Open(fname)
        if ds is None:
            raise(FileNotFoundError("<%s> exists, but failed to open" % fname))
        ny = ds.RasterXSize
        nx = ds.RasterYSize
        sec_y = ny /4
        sec_x = nx /4
        x1,y1 = 0
        x2 = sec_x
        y2 = sec_y
        images 
        while x2 <= nx and y2 <= ny:
            if len(bands)>0:
                band = ds.GetRasterBand(1+bands[0])
                x: np.ndarray = band.ReadAsArray(y1,x1,y2-y1,x2-x1)
                array: np.ndarray = np.zeros((len(bands),x2-x1,y2-y1), dtype=x.dtype)
                array[0,:,:] = x
                for i, b in enumerate(bands):
                    if i>0:
                        band = ds.GetRasterBand(b+1)
                        x: np.ndarray = band.ReadAsArray(y1,x1,y2-y1,x2-x1)
                        array[i,:,:] = x
            else:
                array: np.ndarray = ds.ReadAsArray(y1,x1,y2-y1,x2-x1)
            
            x1 = x2
            y1 = y2
            x2 = x2 + sec_x
            y2 = y2 + sec_y
        return array



    def show(self,cmap='viridis'):
        """
            Shows the image with pil for debuging
        """
        plt.figure(figsize=(10,10))
        plt.imshow(self.img,cmap=cmap)
        plt.show()

    def contrast_enhance_band(self,x, percentile=(0.5, 99.5), gamma=0.5):
        """
            Gamma stretching and percentile stretching for more natural looking images.
        """
        plow, phigh = np.percentile(x, percentile)
        x = exposure.rescale_intensity(x, in_range=(plow, phigh))
        y = (x - x.min()) / (x.max()-x.min())
        y = y ** gamma
        img = (y*255).astype(np.uint8)
        return(img)
    
    def raw_rgb(self):
        # extract rgb bands
        tmp = self.data[3:0:-1,:,:] / self.data.max()
        # convert to 0-255 range
        self.img = np.transpose((255. * tmp), (1,2,0)).astype(np.uint8)
    
    def s2_to_rgb(self,rgb=[2,1,0]):
        r, g, b = rgb
        nb, nx, ny = self.data.shape
        img = np.zeros((nx, ny, 3), dtype = np.uint8)
        img[:,:,0] =  self.contrast_enhance_band(self.data[r, :, :], percentile=(0.5, 99.5), gamma=0.7)
        img[:,:,1] =  self.contrast_enhance_band(self.data[g, :, :], percentile=(0.5, 99.5), gamma=0.7)
        img[:,:,2] =  self.contrast_enhance_band(self.data[b, :, :], percentile=(0.5, 99.5), gamma=0.7)
        self.img = img
        return img
        
    def band(self, band_num):
        if (band_num < self.data.shape[0]) and (band_num > 0):
            self.img = self.contrast_enhance_band(self.data[band_num,:,:], percentile=(0.5,99.5),gamma=0.7)
            return self.img
        else: 
            # raise Exception("Band Selection is outside of range")
            return False