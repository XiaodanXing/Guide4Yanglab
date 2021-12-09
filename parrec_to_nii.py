'''
convert all parrec files in a directory to nifti
https://gist.github.com/jcreinhold/fdd701211191450284c5718502eabbd4
'''

import argparse
from glob import glob
import os
import sys

import nibabel as nib


def arg_parser():
    parser = argparse.ArgumentParser(description='convert all parrec images in a directory to nifti')
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
        fns = glob(os.path.join(args.img_dir, '*.par'))
        if len(fns) == 0:
            fns = glob(os.path.join(args.img_dir, '*.PAR'))
        if len(fns) == 0:
            raise Exception(f'Could not find .par files in {args.img_dir}')
        for fn in fns:
            print(f'Converting image: {fn}')
            img = nib.load(fn)
            _, base, _ = split_filename(fn)
            out_fn = os.path.join(args.out_dir, base + '.nii.gz')
            nifti = nib.Nifti1Image(img.dataobj, img.affine, header=img.header)
            nifti.set_data_dtype('<f4')
            nifti.to_filename(out_fn)
            print(f'Saved to: {out_fn}')
        return 0
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    sys.exit(main())