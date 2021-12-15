# Frequently Asked Questions

### 1. Cannot start pycharm: No JRE found Error (Weixun Luo, 2021.12.1)

![avatar](images/Q1.jpg)



A: The version of pycharm does not match with the version of JAVA. Please use pycharm-2021.1.2, which works on our servers.







### 2. Could not load dynamic library 'libcupti.so.11.1' (Jiahao Huang, 2021.12.1) 

A: Please find detailed instructions on [Q2](faqs/Q2.md)

1. FIND IT:
   Input:
   `find ./ -name 'libcupti.so.11.1'`

   Get:
   `./anaconda3/lib/python3.6/site-packages/nvidia/cuda_cupti/lib/libcupti.so.11.1`

2. ADD IT:
   Input:
   `vim ~/.bashrc`

   Add to the final line:
   `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/xx/anaconda3/lib/python3.6/site-packages/nvidia/cuda_cupti/lib/`

   Refresh:
   `source ~/.bashrc`


3. (Appendix)

   Github Repo:

   https://github.com/NVIDIA/tensorflow

   How to use tf1.15 in cuda11

   https://segmentfault.com/a/1190000040354322

   Could not load dynamic library？

   https://github.com/tensorflow/tensorflow/issues/45930#issuecomment-770342299

   How to use vim?

   https://www.myfreax.com/how-to-save-file-in-vim-quit-editor/



### 3. The user account I created did not enter bash automatically (Jiahao Huang, 2021.12.10)

A: It might because you create their account with `useradd -m`. Please do remember to add users with `adduser`. If this already happens, you can help them enter bash automatically by revising /etc/passwd. Enter passwd file with

```
sudo vim /etc/passwd
```

and add /bin/bash/ for them manually.

![avatar](images/Q3.png)

### 4. I want to process images by batches with a for-loop, but there are tons of them. I don't want to wait that long.  (Xiaodan Xing, 2021.12.15)

A: Multiprocessing is a good tool to accelerate your for-loops. By using multiple processes, multiple images can be pre-processed at a same time, and by doing so, you can save a lot of time.  Let take CT windowing as an example. 

```python
import multiprocessing
import nibabel as nib
import numpy as np
import os

def ImagePreprocess(filename,window_level=-600,window_width=1200):
    img = nib.load('CTfiles/%s'%filename)
    img_arr = img.get_fdata()
    
    # clipping
    low_value = window_level - window_width/2
	high_value = window_level + window_width/2
    img_arr[np.where(img_arr <= low_value)] = low_value
    img_arr[np.where(img_arr >= high_value)] = high_value
    
    img_clipped = nib.Nifti1Image(img_arr, img.affine, img.header)
    nib.save(img_clipped,'CTfiles_clipped/%s'%filename)


if __name__ == '__main__':
    filenames = os.listdir('CTfiles_clipped/')
                           
    # Create a multiprocessing Pool
    pool = multiprocessing.Pool(16)  
    pool.map(ImagePreprocess, filenames)
    pool.close()
    pool.join()

```

