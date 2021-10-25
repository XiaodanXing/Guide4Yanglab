# PytorchGuide
A manual for new starters in our group

## Introduction

After learning some thrilling theoretical knowledge about deep learning and medical image analysis, it is time to start a hands-on project! This note will cover all the tips you will need to start a toy project on your own. We will learn to set up a new enviroment using anaconda, debug python project using Pycharm (it is okay to use other IDLE), and build a sample segmentation project, segmenting LV from cardiac MR images. 

 
Before we start, it is highly recommended that you use a Linux op system. In our group, we assigned yanglab@172.26.136.118 to undergraduate students. Here are several tips for new linux users: 

1. Download MobaXtern (for commanding) and WinSCP (for file transfer). 

2. Open MobaXtern 

3. Click session->ssh; remote host is  172.26.136.118, username is your name. Then you shall be connected. See picture below.
[pic]{./images/moba.png} 


5. In the command line, input 

    `ls `

This will show all the files under your private folder.  

 
## Setting up an enviroment in python: 

1. Download anaconda3 from here.  

2. Copy the sh file to your private folder '/home/yourname/' and run it with 
 ```
sh Anaconda3-2021.05-Linux-x86_64.sh 
```

3. After sucessful installation, input 
```
conda activate 
```

to activate your base enviroment. At most of the time, it is okay to use base enviroment directly. If you are still interested in creating independent virtual enviroment for each of your projects, you can search 'conda virtual env creation' with google.  

4. Input  

```
conda install python==3.7 
```
to install python for your base enviroment; and 
```
which python 

which pip 
```
to check if your python is installed sucessfully. The output of 'which python' should be your anaconda directory. 

5.  We recommend pytorch for starters as the toolkit for deep learning. It is easier to compile and debug (than Tensorflow/Keras/Caffee).  

```
Pip install torch 

Pip install torchvision 
```

 

 

Starting an simple pytorch project: 

    Download anaconda3 from here.  
