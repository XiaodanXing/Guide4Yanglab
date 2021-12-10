# PytorchGuide

A manual for new starters in our group



## Build your own dataset

The first step for training a deep learning model is to prepare a dataset. There are many tutorials using online datasets such as MINIST and COCO. They are easy to download and these open-source natural image datasets can be used to validate the performance your model. However, since our focus is on medical imaging, it is important to learn to build a medical imaging dataset with actual clinical data. 

### Load your medical images

There are many different forms of clinical data, including hdr, DICOM, NIFTI and so on. Among these, DICOM and NIFTI are two most popular forms of medical images. [Pydicom](https://github.com/pydicom/pydicom) is a package for DICOM loading, and [Nibabel](https://github.com/nipy/nibabel) is for NIFTI loading. Examples for image loading is shown below:

```python
import pydicom as dcm
img = dcm.dcmread(filename)
imgArr = img.pixel_array

import nibabel as nib
img = nib.load(filename)
imgArr = img.get_fdata()

####imgArr is an array which can be transfered to pytorch.Tensor, numpy.array, and pandas.Dataframe.
```

Other types of data for deep learning includes .h5 files and images files such as .png and .jpg files. 

```python
import h5py
f = h5py.File(filename, 'r')
imgArr = f[tag] 
###tag is the keys of arrays.

from PIL import Image
img = Image.open(filename)
```

A few datasets are saved in the .mha format. In the [utils](utils/), we provided some useful tools to read this format. For Nifti files and Dicom files, the 3D image array is saved in one file, while for MHA files, the 3D array is saved separately in several 2D slice files. If you, unluckily, encountered MHA files,  please download the [utils](utils/). And input below commands to transfer them into Nifti. 

```shell
python mha_to_nii.py input_dir output_dir
```

Here, input_dir is the directory of MHA files, and output_dir is the path of the output Nifti file.   



### Preprocessings of medical images

For different modalities, we use different preprocessing procedure. It is always useful to carefully pre-process your data.

#### CT images

Window width and window level

#### MR images

histogram match, registration, N3-registration

#### PET images

TBD



### Upload your medical images into Pytorch. Dataset

For pytorch, dataset is built and loaded through pytorch.Dataset and pytorch.Dataloader. pytorch.Dataset is a class, an example of which is defined as below:

```python
import pandas as pd
import os
import numpy as np
from PIL import Image, ImageOps
from torchvision import transforms
from torch.utils.data import Dataset

train_transform = transforms.Compose([
    # Data augmentations:
	# transforms.ColorJitter(brightness=0.7, contrast=0.8, saturation=0.8),
    # transforms.RandomVerticalFlip(),
    # transforms.RandomHorizontalFlip(),
    # transforms.RandomRotation(10),
    transforms.Resize([256,256]),
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
    # for 3-channel RGB inputs:
    # transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

class DatasetCT2Dlung(Dataset):
    def __init__(self):  # define the list of your files

        self.imlist = pd.read_csv('/home/xiaodan/filelist.csv',
                                  index_col=0)
        self.imlist.index = np.arange(self.imlist.shape[0])
        
		# imlist is a list contains all your files. I prefer to save them in a csv file. It is also okay to use:
        # self.imlist = os.listdir(/path/to/your/image/files)
        # to generate file lists. 
        

    def __getitem__(self, idx):# how to get one file in your filelist
        if idx < len(self.imlist):
            img_name = self.imlist.iloc[idx].filename # the name of the image file
            status = self.imlist.iloc[idx]['label'] # the label of the image file

            img = Image.open(img_name)
            img = ImageOps.grayscale(img)# it is a grey scale medical image, so we only need one color channel
            img = train_transform_lung(img)# transform this image into pytorch.Tensor
            
            return img,status
    def __len__(self):
    	return len(self.imlist)
```

I prefer to save all codes related to my dataset in a python file named 'CustomDataset.py'. It is okay to save it in other different places. 



### Use your custom dataset in your models

In your main running file, you shall import your custom dataset as 

``` python
from CustomDataset import DatasetCT2Dlung
from torch.utils.data import DataLoader

dataset = DatasetCT2Dlung()
dataloader = DataLoader(dataset, batch_size=opt.batchSize,
                                         shuffle=True, num_workers=int(opt.workers))

```

Here, batch_size is the number of images per batch. It is impossible to load all our training images into our model at the same time, so 'train by batches' here means that we sample some images to optimize parameters, and then sample some other images for a further optimization. When we trained our network on all training images, an EPOCH is completed.  Num_workers is the number of parallel workers for CPU during data loading. 











