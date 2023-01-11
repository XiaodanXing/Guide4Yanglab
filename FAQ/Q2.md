## Miniconda

1. Download miniconda here:

https://docs.conda.io/en/latest/miniconda.html

2. Copy the `Miniconda3-latest-Linux-x86_64.sh` to user path
   
3. Run
   
`bash Miniconda3-latest-Linux-x86_64.sh`

`conda update conda`


4. Useful Command: 
   
`conda create -n env_name python==3.x.xx`

`conda create -n env_name --clone env_name2`

`conda env list`

`conda activate env_name`

`conda remove -n env_name --all`




## CUDA & cuDNN

conda:
- cudatoolkit==11.3.1
- cudnn==8.2.1

`conda install cudatoolkit==11.3.1`

`conda install cudnn==8.2.1`




## Torch 1.9.0

Find the version you want:

https://download.pytorch.org/whl/torch_stable.html


`wget https://download.pytorch.org/whl/cu111/torch-1.9.0%2Bcu111-cp36-cp36m-linux_x86_64.whl`

`wget https://download.pytorch.org/whl/cu111/torchvision-0.10.0%2Bcu111-cp36-cp36m-linux_x86_64.whl`

`wget https://download.pytorch.org/whl/torchaudio-0.9.0-cp36-cp36m-linux_x86_64.whl`

`pip install + xxx`


## Tensorflow 1.15.5+nv21.11

Requirement:
- python>3.8
- tf>1.15

`pip install --upgrade pip`

`pip install nvidia-pyindex`

`pip install nvidia-tensorflow[horovod]`

`pip install nvidia-tensorboard==1.15`


### Could not load dynamic library 'libcupti.so.11.1'?

1. FIND IT:
    Input:
    `find ./ -name 'libcupti.so.11.1'`

    Get:
    `./miniconda3/envs/brats19/lib/python3.6/site-packages/nvidia/cuda_cupti/lib/libcupti.so.11.1`

2. ADD IT:
    Input:
    `vim ~/.bashrc`

    Add to the final line:
    `export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/jh/miniconda3/envs/test_env/lib/python3.8/site-packages/nvidia/cuda_cupti/lib/`

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
