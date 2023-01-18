# A practical guide for CUDA reinstallation
This is a practical guide for CUDA reinstallation if you have conflict packages. It is worth noting that this tutorial is for a reinstallation for nvidia drivers, CUDA-toolkits and CuDnn. 

All solutions, actions, operations here are validated by Xiaodan Xing at May 3rd, 2022. They might not work in a date after this date. 


## Update Cuda and Cudnn
Credit to [Best practice for upgrading CUDA and cuDNN for tensorflow](https://stackoverflow.com/questions/50213021/best-practice-for-upgrading-cuda-and-cudnn-for-tensorflow) and [Install CUDA 11.2, cuDNN 8.1.0, PyTorch v1.8.0 (or v1.9.0), and python 3.9 on RTX3090 for deep learning](https://medium.com/analytics-vidhya/install-cuda-11-2-cudnn-8-1-0-and-python-3-9-on-rtx3090-for-deep-learning-fcf96c95f7a1).

### Install NVIDIA DRIVER

Step 1: Remove original Cuda files. **Check /usr/local/ to see if there's any folder named "Cuda" left.** For me there were still folders named CUDA or CUDA-xx.x, so I removed them. Please be cautious for this operation. 

```
sudo apt-get --purge remove cuda
sudo apt-get autoremove
dpkg --list |grep "^rc" | cut -d " " -f 3 | xargs sudo dpkg --purge
```

Step 2: Then set up the Unbuntu by

```
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y build-essential cmake unzip pkg-config
sudo apt-get install -y libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
sudo apt-get install -y libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install -y libxvidcore-dev libx264-dev
sudo apt-get install -y libgtk-3-dev
sudo apt-get install -y libopenblas-dev libatlas-base-dev liblapack-dev gfortran
sudo apt-get install -y libhdf5-serial-dev graphviz
sudo apt-get install -y python3-dev python3-tk python-imaging-tk
sudo apt-get install -y linux-image-generic linux-image-extra-virtual
sudo apt-get install -y linux-source linux-headers-generic
```

Step 3: Add graphics PPA
```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt-get update
```

Step 4: Search available drivers
```
ubuntu-drivers devices
```
![图片](https://user-images.githubusercontent.com/30890745/166504728-1a30e940-f5b3-49cc-a7e6-7510e3743943.png)


Step 5: Install the driver with the best version. I choose driver-460 here because of the requirement of StyleGAN2-ada-PyTorch. Please select 510 if you are working on an RTX3090 device.
```
sudo apt-get install nvidia-driver-460
```

Step 6: Reboot your computer after installation. After rebooting, verify the driver installation by

```
nvidia-smi
```


### Install CUDA-toolkit-v11.2
Step 1. Install CUDA-toolkit by

```
wget https://developer.download.nvidia.com/compute/cuda/11.2.2/local_installers/cuda_11.2.2_460.32.03_linux.run
sudo sh cuda_11.2.2_460.32.03_linux.run
```

***Remember: DO NOT check the option of installing the driver!!!***

In [Yifan's blog](https://medium.com/analytics-vidhya/install-cuda-11-2-cudnn-8-1-0-and-python-3-9-on-rtx3090-for-deep-learning-fcf96c95f7a1), this line is written in bold and italic texts. I guess this is super important, but I do not know what will happen if the driver is installed simultaneously. To not install the driver, the installation page of CUDA should be like

![图片](https://user-images.githubusercontent.com/30890745/166521580-5262001d-ca62-4ad1-ba48-772688e53cfa.png)

After the installation, you will see the result below.
![图片](https://user-images.githubusercontent.com/30890745/166521626-06dd5009-dc95-475c-a152-cc2832460ede.png)

Step 2. Update environmental variable

Set environmental variables in the `~/.bashrc` by

```
cd ~
vim ./.bashrc
```

Then paste the below lines into your bashrc file. 
```
export PATH=/usr/local/cuda-11.2/bin${PATH:+:${PATH}}
export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
export CUDA_HOME=/usr/local/cuda
```
Remember to update your bashrc file by
```
source ./.bashrc
```

### Install cuDnn-v8.1.0

Step 1. Download cuDnn-v8.1.0 from [here](https://developer.nvidia.com/rdp/cudnn-archive)

Step 2. Select a correct version of CuDnn. I also tried *cuDNN v8.1.1 (Feburary 26th, 2021), for CUDA 11.0,11.1 and 11.2*,*cuDNN v8.2.0 (April 23rd, 2021), for CUDA 11.x*, *cuDNN v8.2.0 (April 23rd, 2021), for CUDA 11.x* and *cuDNN v8.2.1 (June 7th, 2021), for CUDA 11.x*. They all worked perfectly for me and my RTX3090.

```
tar -zvxf cudnn-11.2-linux-x64-v8.1.0.77.tgz
```

Step 3. Set up environmental variables for CuDnn by adding the following at the end of `~/.bashrc`.

```
export LD_LIBRARY_PATH=/home/xiaodan/cuda/lib64:$LD_LIBRARY_PATH
```

Step 4. To verify the installation, check `nvidia-smi`, and `nvcc -V`.

## Update PyTorch or downgrade PyTorch
If the target is to use PyTorch in your device (i.e., you do not care which version of pytorch you will be using) please find a PyTorch-v1.11.0 downloading command [here](https://pytorch.org/get-started/locally/).

For the official PyTorch implementation of StyleGAN2, PyTorch-v1.7.x is required. Please find corresponding commands [here](https://pytorch.org/get-started/previous-versions/). 

```
# CUDA 11.1
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
```

I always find the above conda command not working for me. Please use the pip wheel downloading command instead.

```
# CUDA 11.0
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html
```
Please do not worry if the version of cudatoolkit here does not match the CUDA version we just downloaded. It won't be a problem if you run codes from [StyleGAN2](https://github.com/NVlabs/stylegan2-ada-pytorch).




# Problems I encountered

1. When using `apt-get update`, 
```
The following signatures couldn't be verified because the public key is not available (The key number)
```
It is because the key is not added into your device. Just add the number into your keyserver by 
```
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 'The key number'
```









