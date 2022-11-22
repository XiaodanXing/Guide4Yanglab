# JADE2 Usage Tutorial

### **JUST follow this tutorial step by step !**

<br>

<!-- **DO NOT ask Why, no time to answer** -->

### **If you have any questions, please check the [official docs](https://docs.jade.ac.uk/en/latest/index.html) first; if you can not handle the problem in 6 hours, then consider to contact Ming Li / Xiaodan Xing / Jiahao Huang via email, you will get a response in 1-2 working day**

<br>

### If there still exists any knotty problems, please raise an issue at [this link](https://github.com/jade-hpc-gpu/jade-hpc-gpu.github.io/issues) 

---
<br><br><br>

# Introduction

*We have three accounts on JADE2, namely*

> user_1 (ready, managed by Ming Li - <ming.li@imperial.ac.uk>) <br>
> user_2 (ready, managed by Xiaodan Xing - <x.xing@imperial.ac.uk>) <br>
> user_3 (ready, managed by Jiahao Huang - <j.huang21@imperial.ac.uk>) 

## Running Capacity (<u>for one single account</u>)

<u>**we strongly recommend that you opt for ''small'', given the queuing time**</u>

* every account can
    > run 8 small jobs at most <br>
    > run 5 big jobs at most <br>
    > ~~run 1 devel job at most~~ <br>

* partition description
    > small - 1 GPU <br>
    > big - 4 or 8 GPUs <br>
    > ~~devel - 1 GPU~~ <br>

* time limitation
    > small - 6 days <br>
    > big - 24 hours <br>
    > ~~devel - 1 hour~~ <br>


## 1 - Login yanglab6

1. Ask Dr Guang Yang for Zerotier access permission
2. Email Ming Li / Xiaodan Xing / Jiahao Huang for ID and password (attach the email or WeChat screenshot that shows your have got permission)
3. Login yanglab6 using a specific ID
``` python
ssh specific_ID@yanglab6_zerotier_ip
```

## 2 - Login JADE2

1. Ask Dr. Guang Yang for JADE2 access permission
2. Email Ming Li / Xiaodan Xing / Jiahao Huang for ssh connection detail (attach the emails or WeChat screenshots that shows you have got permission)
3. Connect JADE2 
``` python
ssh user_name@JADE_address
```

---
<br><br><br>

# Create Environment

## 0 - Prerequisites

### create your own folder
``` python
mkdir [your_name]
```

### load modules
``` python
module load python/anaconda3
```

## 1 - Clone Official Build Envs

### clone env using this command
``` python
# be patient. This procedure will take a long time
conda create --clone /jmain02/apps/python3/anaconda3/envs/pytorch-1.12.1 -n [your_env_name]
```

### your_env_name naming convention (recommend)

> [your_name]\_[cuda_version]\_[torch_version] <br>
> (e.g., ming_112_torch)

### you can choose the following options to clone:

> /jmain02/apps/python3/anaconda3/envs/pytorch-1.12.1 <br>
> /jmain02/apps/python3/anaconda3/envs/pyTorch-1.9.0 <br>
> ~~/jmain02/apps/python3/anaconda3/envs/pyTorch-1.8.1~~ <br>

### or using your sweet old environment that is set up in your local device:
1. First upload your environment to NAS03 and then download the env folder in JADE2:
```
cp -r /home/[your_name]/anaconda3/envs/[your_env_name] /media/NAS03/JADE_envs/[your_env_name] 
scp -r /media/NAS03/JADE_envs/[your_env_name] [user_name]@[JADE_address]:/home/[your_name]/[your_env_name] 
```
2. You are free to clone your environment by
```
conda create --clone /home/[your_name]/[your_env_name]  -n [your_env_name]
```


### test your envs

``` python
# activate
source activate [your_env_name]

# check package already installed
conda list

# customize your envs
conda install packages_you_need

# deactivate (this can be important. If the conda virtual environment is not deactivated, you might not be able to activate the virtual environment in your job submissions)
conda deactivate
```

---
<br><br><br>

### test your environment interactively with GPU resources
To validate the environment installation with GPU resources, you need to apply for GPU with:
```
srun --gres=gpu:8 --pty /bin/bash
```


# Data&Code Transfer Between Our Local Workstation and JADE2

after you login in yanglab6, use this command to transfer data&code between our local workstation and JADE2

``` python
rsync -rz --info=progress2 --partial SOURCE_PATH TARGET_PATH

'''examples
'''
# transfer data from our local machine to JADE2
rsync -rz --info=progress2 --partial /media/[nas_id]/model_weights.pth user_name@JADE_address:/home

# transfer data from JADE2 to our local machine
rsync -rz --info=progress2 --partial user_name@JADE_address:/home/.../model_weights.pth /media/[nas_id]/


# use command `pwd` to get the path
```

### Attention: 
> if your data is too large or contains too many files (i.e., thousands and hundreds of images), remember to compress your files before transfer

---
<br><br><br>

# Run Your Code

## Preparing a submission script

### job_test.sh

``` bash
#!/bin/bash

# set the number of nodes
#SBATCH --nodes=1

# set max wallclock time
#SBATCH --time=10:00:00

# set name of job
#SBATCH --job-name=ming_job_test

# set partitions: small or big or devel
#SBATCH --partition=devel

# set number of GPUs
#SBATCH --gres=gpu:1

# set number of CPUs
#SBATCH -c 4

# set size of Memory/RAM
#SBATCH --mem=16G

# mail alert at start, end and abortion of execution
#SBATCH --mail-type=ALL

# send mail to this address
#SBATCH --mail-user=your_email_address

# job partition size
#SBATCH --partition=small


# load modules
module load python/anaconda3
# if you choose Pytorch 1.12.1
module load cuda/11.1-gcc-9.1.0
# if you choose Pytorch 1.9.0
# module load cuda/10.2
# we do not recommend you to use other PyTorch versions


# use absolute path (recommend)
# cd ~/.conda/envs 
# pwd
source activate /.../your_env_name


# run python files
# use absolute path (recommend)
python /.../gpu_test.py
```

## Submit Jobs

``` bash
sbatch job_test.sh
```
then you will get your job id in the terminal

## Check Running Status & Organize your jobs

``` bash
# running status
squeue -u user_name

# cancel your jobs
scancel job_id
```

## Check Running Output

you will see "slurm-job_id.out" in the folder where your submission script exists
``` bash
cat slurm-job_id.out
```

## Check GPU Status

``` bash
srun --jobid=your_job_id nvidia-smi
```

## More details, please check [Slurm docs](https://docs.jade.ac.uk/en/latest/jade/scheduler/index.html#)


