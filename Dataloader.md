# PytorchGuide

A manual for new starters in our group



## Build your own dataset

The first step for training a deep learning model is to prepare a dataset. There are many tutorials using online datasets such as MINIST and COCO. They are easy to download and these open-source natural image datasets can be used to validate the performance your model. However, since our focus is on medical imaging, it is important to learn to build a medical imaging dataset with actual clinical data. 

There are many different forms of clinical data, including hdr, DICOM, NIFTI and so on. Among these, DICOM and NIFTI are two most popular forms of medical images. [Pydicom](https://github.com/pydicom/pydicom) is a package for DICOM loading, and [Nibabel](https://github.com/nipy/nibabel) is for NIFTI loading. Examples for image loading is shown below:

```python
import pydicom as dcm
img = dcm.dcmread(filename)
imgArr = img.pixel_array

import nibabel as nib
img = nib.load(filename)
imgArr = img.get_fdata()

####imgArr is an array which can be transfered to pytorch.Tensor,numpy.array, and pandas.Dataframe
```



For pytorch, dataset is built and loaded through pytorch.Dataset and pytorch.Dataloader. pytorch.Dataset is a class, an example of which is defined as below:















