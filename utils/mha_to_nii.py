#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nii_to_tif
convert all mha files in a directory to nifti
Author: Jacob Reinhold (jacob.reinhold@jhu.edu)
Link: https://gist.github.com/jcreinhold/a26d6555b0e7aa28b79757f766640dd6
"""

import argparse
from glob import glob
import os
import sys

import itk


def arg_parser():
    parser = argparse.ArgumentParser(description='convert all mha images in a directory to nifti')
    parser.add_argument('img_dir', type=str)
    parser.add_argument('out_dir', type=str)
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
        fns = glob(os.path.join(args.img_dir, '*.mha'))
        if len(fns) == 0:
            raise Exception(f'Could not find .mha files in {args.img_dir}')
        for fn in fns:
            print(f'Converting image: {fn}')
            img = itk.imread(fn)
            _, base, _ = split_filename(fn)
            out_fn = os.path.join(args.out_dir, base + '.nii.gz')
            itk.imwrite(img, out_fn)
            print(f'Saved to: {out_fn}')
        return 0
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    sys.exit(main())