# JADE2 Usage Tutorial

**JUST follow this tutorial step by step**

<!-- **DO NOT ask Why, no time to answer** -->

**Any question, check the [official docs](https://docs.jade.ac.uk/en/latest/index.html) first, if you can not handle the problem in 6 hours, then consider to contact Ming Li / Xiaodan Xing / Jiahao Huang via email, you will get response in 1-2 working day**

---

## 0 - Introduction

We have three account on JADE2, namely

> user_1 (ready, managed by Ming Li - <ming.li@imperial.ac.uk>) <br>
> user_2 (on the way, managed by Xiaodan Xing - <x.xing@imperial.ac.uk>) <br>
> user_3 (on the way, managed by Jiahao Huang - <j.huang21@imperial.ac.uk>) <br>


---

## 1 - Login yanglab6

1. Ask Dr Guang Yang for Zerotier access permission
2. Email Ming Li / Xiaodan Xing / Jiahao Huang for ID and passwd (attach the email or wechat screenshot that shows your have got permission)
3. Login yanglab6 using specific ID
``` python
ssh specific_ID@yanglab6_zerotier_ip
```

## 2 - Login JADE2

1. Ask Dr Guang Yang for JADE2 access permission
2. Email Ming Li / Xiaodan Xing / Jiahao Huang for ssh connection detail (attach the email or wechat screenshot that shows your have got permission)
3. Connect JADE2 
``` python
ssh user_name@JADE_address
```

---

# Create Environment

## 0 - Prerequisites

### create your own folder
``` python
mkdir yourName
```

### load modules
``` python
module load python/anaconda3
```

## 1 - Clone Official Build Envs

### clone env using this command
``` python
# be patient, this procedure will take a long time
conda create --clone /jmain02/apps/python3/anaconda3/envs/pytorch-1.12.1 -n your_env_name
```

### your_env_name naming method (recommend)

> yourName_version_torch <br>
> (e.g., ming_112_torch)

### you can choose the following options to clone:

> /jmain02/apps/python3/anaconda3/envs/pytorch-1.12.1 <br>
> /jmain02/apps/python3/anaconda3/envs/pytorch-1.9.0 <br>
> /jmain02/apps/python3/anaconda3/envs/pytorch-1.8.1 <br>

### test your envs

``` python
# activate
source activate your_env_name

# check package already installed
conda list

# customize your envs
conda install package_you_need

# deactivate
conda deactivate
```

---

# Data&Code Transfer Between Our Local Workstation and JADE2

after you login in yanglab6, use this command to transfer data&code between our local workstation and JADE2

``` python
rsync -rz --info=progress2 --partial SOURCE_PATH TARGET_PATH

# example
rsync -rz --info=progress2 --partial /media/nas/model_weights.pth user_name@JADE_address:/home

# use command `pwd` to get the path
```

### Attention: 
> if your data is too large or contains too many files (i.e., thousands and hundreds of images), remember to compress your files before transfer

---


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



# load modules
module load python/anaconda3
# if you choose pytorch 1.12.1
module load cuda/11.1-gcc-9.1.0
# if you choose pytorch 1.9.0
# module load cuda/10.2
# we do not recommend you to use other pytorch versions


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

---

## More details, please check [Slurm docs](https://docs.jade.ac.uk/en/latest/jade/scheduler/index.html#)
