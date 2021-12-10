#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nii_to_tif
command line executable to convert 3d nifti images to 
individual tiff images along a user-specified axis
call as: python nii_to_tif.py /path/to/nifti /path/to/tif
(append optional arguments to the call as desired)
Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Since the original volumes are floating point numbers, we recommend to go with the TIFF image format which supports such types.

More description:
    This command-line script takes a directory of NIfTI images and creates a directory of corresponding 2D TIFF images (with some options to create slices based on axis and to only create slices from a portion of the image in order to avoid background slices).
"""

import argparse
from glob import glob
import os
import sys

from PIL import Image
import nibabel as nib
import numpy as np


def arg_parser():
    parser = argparse.ArgumentParser(description='split 3d image into multiple 2d images')
    parser.add_argument('img_dir', type=str, 
                        help='path to nifti image directory')
    parser.add_argument('out_dir', type=str, 
                        help='path to output the corresponding tif image slices')
    parser.add_argument('-a', '--axis', type=int, default=2, 
                        help='axis of the 3d image array on which to sample the slices')
    parser.add_argument('-p', '--pct-range', nargs=2, type=float, default=(0.2,0.8),
                        help=('range of indices, as a percentage, from which to sample ' 
                              'in each 3d image volume. used to avoid creating blank tif '
                              'images if there is substantial empty space along the ends '
                              'of the chosen axis'))
    return parser


def split_filename(filepath):
    path = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    base, ext = os.path.splitext(filename)
    if ext == '.gz':
        base, ext2 = os.path.splitext(base)
        ext = ext2 + ext
    return path, base, ext


def main():
    try:
        args = arg_parser().parse_args()
        fns = glob(os.path.join(args.img_dir, '*.nii*'))
        for fn in fns:
            _, base, ext = split_filename(fn)
            img = nib.load(fn).get_data().astype(np.float32).squeeze()
            if img.ndim != 3:
                print(f'Only 3D data supported. File {base}{ext} has dimension {img.ndim}. Skipping.')
                continue
            start = int(args.pct_range[0] * img.shape[args.axis])
            end = int(args.pct_range[1] * img.shape[args.axis])
            for i in range(start, end):
                I = Image.fromarray(img[i,:,:], mode='F') if args.axis == 0 else \
                    Image.fromarray(img[:,i,:], mode='F') if args.axis == 1 else \
                    Image.fromarray(img[:,:,i], mode='F')
                I.save(os.path.join(args.out_dir, f'{base}_{i:04}.tif'))
        return 0
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    sys.exit(main())