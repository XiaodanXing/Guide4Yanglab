# Frequently Asked Questions

#### 1. Cannot start pycharm: No JRE found Error (Weixun Luo, 2021.12.1)

![avatar](images/Q1.jpg)



A: The version of pycharm does not match with the version of JAVA. Please use pycharm-2021.1.2, which works on our servers.



#### 2. Could not load dynamic library 'libcupti.so.11.1' (Jiahao Huang, 2021.12.1) 

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





