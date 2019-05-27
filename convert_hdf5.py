import h5py
import os
from PIL import Image
import numpy as np
import tifffile
import skimage
from skimage import io
from skimage import external
import scipy.io as sio
import shutil


def h5_to_tiff(grp_name, object):
    try:
        n_subgroups = len(object.keys())
        string = object.name[1:]
        os.mkdir(string)

    except:
        n_subgroups = 0
        string = object.name[1:]

        x = 0
        for image in range(object[()].shape[0]):
            value = int(object.name[-4:])
            value += x
            value = str(value).zfill(4)
            filename = f'{object.name[1:-4]}{value}.tif'
            with skimage.external.tifffile.TiffWriter(filename) as tif:
                tif.save(object[()][image], compress=0)
            x += 1

        dataset_list.append(object.name)


def h5_to_raw(grp_name, object):
    try:
        n_subgroups = len(object.keys())
        string = object.name[1:]
        os.mkdir(string)

    except:
        n_subgroups = 0
        string = object.name[1:]

        x = 0
        for image in range(object[()].shape[0]):
            value = int(object.name[-4:])
            value += x
            value = str(value).zfill(4)
            filename = f'{object.name[1:-4]}{value}.raw'
            object[()].tofile(filename)
            x += 1

        dataset_list.append(object.name)


if __name__ == '__main__':
    with h5py.File('image.h5', 'r') as h5f:
        dataset_list = []
        h5f.visititems(h5_to_raw)
