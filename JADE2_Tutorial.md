# <span style="color:#2E86C1 ">*JADE2 Usage Tutorial*</span>

## <span style="color:#2E86C1 ">*JUST follow this tutorial step by step !*</span>

<br>


1. ### If you have any questions, please check the [official docs](https://docs.jade.ac.uk/en/latest/index.html) first 

2. ### if you can not handle the problem, then raise an issue at [this link](https://github.com/XiaodanXing/Guide4Yanglab/issues)

3. ### If there still exists any knotty problems, please raise an issue at [this link](https://github.com/jade-hpc-gpu/jade-hpc-gpu.github.io/issues) 

---
<br>
<br>
<br>



# <span style="color:#2E86C1 ">*Introduction*</span>

## <span style="color:#2E86C1 ">*Computational resources*</span>

*We have four accounts on JADE2, namely*

|Name|Status|Administrator|Email|
| :--- | :---: | :---: | ---: |
|user_1|ready|Ming Li|ming.li@imperial.ac.uk|
|user_2|ready|Xiaodan Xing|x.xing@imperial.ac.uk|
|user_3|ready|Jiahao Huang|j.huang21@imperial.ac.uk|
|user_4|on the way|Yang Nan|y.nan20@imperial.ac.uk|

<br>

## <span style="color:#2E86C1 ">*Running Capacity (<u>for one single account</u>)*</span>

<u>*we strongly recommend that you opt for `small`, given the queuing time*</u>


|Partition|Description|Job Walltime limit|Running Job limit|
| :--- | :---: | :---: | ---: |
|`small`|Partition dedicated to jobs that utilise a single GPUs each|6 days|5 Jobs|
|`big`|Partition dedicated to jobs that occupy an entire node, i.e., 8 or 4 GPUs|24 hours|8 Jobs|
|`devel`|Partition dedicated to testing <br> <span style="color:#2E86C1 ">*should be used to check your submission script works correctly and that your application starts to execute without errors*</span>|1 hour|1 Job|

<br>

## <span style="color:#2E86C1 ">*Login JADE2*</span>

1. ask Dr Guang Yang for oral `zerotier & JADE2` access permission
2. email Ming Li (CC Dr Guang Yang) to authorize your `zerotier & JADE2` connection
   (provide your zerotier address e.g., 530c509607)
3. login yanglab6 using a specific ID
    ``` python
    ssh specific_ID@yanglab6_zerotier_ip
    ```
    * `Attention:`
        * yanglab6 serves as a jump server, everyone needs to access JADE2 via yanglab6
4.  connect JADE2 
    ``` python
    ssh jade_user_name@JADE_address
    ```

---
<br>
<br>
<br>



# <span style="color:#2E86C1 ">*Create Environment*</span>

## <span style="color:#2E86C1 ">*0 - Prerequisites*</span>

### <span style="color:#2E86C1 ">*create your own folder*</span>
``` python
mkdir [your_name]
```

### <span style="color:#2E86C1 ">*load modules*</span>
``` python
module load python/anaconda3

# abbreviation
ml python/anaconda3
```

<br>

## <span style="color:#2E86C1 ">*1 - Clone Official Build Envs*</span>

### <span style="color:#2E86C1 ">*clone env using this command*</span>
``` python
# be patient. This procedure will take a long time
conda create --clone /jmain02/apps/python3/anaconda3/envs/pytorch-1.12.1 -n [your_env_name]
```

### <span style="color:#2E86C1 ">*your_env_name naming convention (recommend)*</span>
``` python
[your_name]_[cuda_version]_[torch_version]
# e.g., ming_cu111_torch112
```


### <span style="color:#2E86C1 ">*you can choose the following options to clone:*</span>

> /jmain02/apps/python3/anaconda3/envs/pytorch-1.12.1 <br>
> /jmain02/apps/python3/anaconda3/envs/pyTorch-1.9.0 <br>
> ~~/jmain02/apps/python3/anaconda3/envs/pyTorch-1.8.1~~ <br>

### <span style="color:#2E86C1 ">*or using your sweet old environment that is set up in your local device:*</span>
1. first upload your environment to NAS* and then download the env folder to JADE2:
    ``` python
    # via any servers (yanglab*) that can access NAS*
    cp -r /home/[your_name]/anaconda3/envs/[your_env_name] /media/NAS*/JADE_envs/[your_env_name] 

    # via yanglab6 (jade account)
    scp -r /media/NAS03/JADE_envs/[your_env_name] [user_name]@[JADE_address]:/[home]/[your_name]/[your_env_name] 
    ```

    * `Attention:`
        * Please use `pwd` to check [home] when you first login JADE, especially when 'Permission Denied' happens


2. You are free to clone your environment by
    ``` python
    conda create --clone /[home]/[your_name]/[your_env_name] -n [your_env_name]
    ```

### <span style="color:#2E86C1 ">*test your envs*</span>

``` python
# activate (please use source activate, conda activate sometimes does not work.)
source activate [your_env_name]

# check package already installed
conda list

# customize your envs
conda install packages_you_need

# deactivate (this can be important. If the conda virtual environment is not deactivated, you might not be able to activate the virtual environment in your job submissions)
conda deactivate
```

* Q: Why we use `source activate` instead of `conda activate` here?
* A: If we directly use `conda activate`, it requires `conda init` and restart the shell. Please use `source activate` at the first time (after `module load`), and free to use both of them later.


### <span style="color:#2E86C1 ">*test your envs interactively with GPU*</span>
* To validate the environment installation with GPU resources, you need to apply for GPU with
    ``` 
    srun --gres=gpu:1 --partition=small --pty /bin/bash
    ```

* If success:
    ``` 
    srun: job xxxxxx queued and waiting for resources
    srun: job xxxxxx has been allocated resources
    ```

---
<br><br><br>



# <span style="color:#2E86C1 ">*Data&Code Transfer Between Our Local Workstation and JADE2*</span>

* after you login in yanglab6, use this command to transfer data&code between our local workstation and JADE2

    ``` python
    '''use command `pwd` to get the path
    '''
    rsync -rz --info=progress2 --partial SOURCE_PATH TARGET_PATH

    '''examples
    '''
    # transfer data from our local machine to JADE2
    rsync -rz --info=progress2 --partial /media/[nas_id]/model_weights.pth user_name@JADE_address:/[home]/.../

    # transfer data from JADE2 to our local machine
    rsync -rz --info=progress2 --partial user_name@JADE_address:/[home]/.../model_weights.pth /media/[nas_id]/
    ```

### `Attention:`
> if your data is too large or contains too many files (i.e., thousands and hundreds of images), remember to compress your files before transfer

---
<br>
<br>
<br>



# <span style="color:#2E86C1 ">*Run Your Code*</span>

## <span style="color:#2E86C1 ">*Preparing a submission script*</span>

### <span style="color:#2E86C1 ">*job_test.sh*</span>

``` bash
#!/bin/bash

# set the number of nodes
#SBATCH --nodes=1

# set max wallclock time
#SBATCH --time=10:00:00

# set name of job
#SBATCH --job-name=yourname_jobname

# set partitions: small or big or devel
#SBATCH --partition=small

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
# if you choose Pytorch 1.12.1
module load cuda/11.1-gcc-9.1.0
# if you choose Pytorch 1.9.0
# module load cuda/10.2
# we do not recommend you to use other PyTorch versions


# use absolute path (recommend)
# cd ~/.conda/envs 
# use pwd to get the path
source activate /.../your_env_name


# run python files
# use absolute path (recommend)
python /.../gpu_test.py
```
* `ATTENTION`
    * do not delete `#` in `#SBATCH`

<br>

## <span style="color:#2E86C1 ">*Submit Jobs*</span>

``` bash
sbatch job_test.sh
```
then you will get your job id in the terminal

<br>

## <span style="color:#2E86C1 ">*Check Running Status & Organize your jobs*</span>

``` bash
# running status
squeue -u user_name

# cancel your jobs
scancel job_id
```

<br>

## <span style="color:#2E86C1 ">*Check Running Output*</span>

you will see "slurm-job_id.out" in the folder where your submission script exists
``` bash
cat slurm-job_id.out
```

<br>

## <span style="color:#2E86C1 ">*Check GPU Status*</span>

``` bash
srun --jobid=your_job_id nvidia-smi
```

<br>

## More details, please check [Slurm docs](https://docs.jade.ac.uk/en/latest/jade/scheduler/index.html#)


