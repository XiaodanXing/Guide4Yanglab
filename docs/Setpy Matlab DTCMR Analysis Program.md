# Setup and Bug Report Matlab DTCMR Analysis Program

Note:
first version: 06/02/2023
lastest version: 06/02/2023


## Basic Information:

Github: https://github.com/ImperialCollegeLondon/DT_CMR_analysis

Platform:
- MacOS M2 success
- Linux Ubuntu 18.04 VM success

### Installation

#### Follow the tutorial of Github

   Please follow https://github.com/ImperialCollegeLondon/DT_CMR_analysis

#### Installation of SimpleElastix:
   
- Linux:
  - (Tried, success.)
  - Just follow the tutorial.

- MacOS M1: 
  - (Never tried, unknown.)
  - Reference: https://github.com/SuperElastix/SimpleElastix/issues/413

- MacOS M2
  - (Tried, success)
  - Reference: https://github.com/SuperElastix/SimpleElastix/issues/413
  

  - Q1: Compile fail when `sudo make`?
  - A1: Use **develop** branch for MacOS Mx. if use **main** branch, the compile may fail.
  

  - Q2: Can't find `setpy.py`, only `setup.py.in`?
  - A2: This is because the use of **develop** branch, it also happen in Linux when using **develop** branch. We can directly change `setup.py.in` to `setup.py` for next step.


  - Q3: Error `ModuleNotFoundError: No module named 'SimpleITK` when `sudo python Packaging/setup.py install` ?
    ```
    (test1) jiahao@lapc-br1-339 Python % sudo python Packaging/setup.py install
    Password:
    Traceback (most recent call last):
    File "Packaging/setup.py", line 14, in <module>
        from SimpleITK._version import __version__
    ModuleNotFoundError: No module named 'SimpleITK'
    ```
  - A3: I don't know why (maybe the reason of **develop branch**). Just `pip install SimpleITK`


#### Tensorflow

For MacOS M2, please follow this to install tensorflow:

`SYSTEM_VERSION_COMPAT=0 pip install tensorflow-macos tensorflow-metal`

### Error and Bug

1. Run and error with `log.txt File not found`
   
    This may because you don't have the write permission in [DICOM_FOLDER]. You may use `sudo chmod -R 777 [DICOM_FOLDER]`

2. Run V3.0, keep `matlab_data` but without `input_data.txt`, error.
- If you want to keep `matlab_data` for V3, you must keep `input_data.txt`.

3. Run V2.9 and turn on AI, error with:

    ```
    ---------------------------------------------
    ---------------------------------------------
    ---------------------------------------------
    DTI output:
    ---------------------------------------------
    Text file with variables found
    ----------------------------
    LV SHORT-AXIS
    ----------------------------
    ---------------------------------------------
    Patient ID: results_dicom_workspace_V2_SOFTWARE_TEST_v2_ai_DCM_systole_20150727_144756_001
    ---------------------------------------------
    Number of myocardial segments: 4
    Number of through-wall segments: 3
    ECG phase: SYSTOLE
    Short-axis plane
    ---------------------------------------------
    Organising Diffusion data...
        Using diff_param.b_value_ref found in header : 11.41
    msgString =
        'Error using <a href="matlab:matlab.internal.language.introspective.errorDocCallback('load')" style="font-weight:bold">load</a>
        Unable to find file or directory '/home/lichao/DT_CMR_analysis_collection/DT_CMR_analysis_2.9/deep_learning/prediction.mat'.
        Error in <a href="matlab:matlab.internal.language.introspective.errorDocCallback('unet_heart_segmentation_3c', '/home/lichao/DT_CMR_analysis_collection/DT_CMR_analysis_2.9/matlab_files/unet_heart_segmentation_3c.m', 60)" style="font-weight:bold">unet_heart_segmentation_3c</a> (<a href="matlab: opentoline('/home/lichao/DT_CMR_analysis_collection/DT_CMR_analysis_2.9/matlab_files/unet_heart_segmentation_3c.m',60,0)">line 60</a>)
        load([code_filepath '/deep_learning/prediction.mat']);
        Error in <a href="matlab:matlab.internal.language.introspective.errorDocCallback('organise_diff_dicoms', '/home/lichao/DT_CMR_analysis_collection/DT_CMR_analysis_2.9/matlab_files/organise_diff_dicoms.m', 569)" style="font-weight:bold">organise_diff_dicoms</a> (<a href="matlab: opentoline('/home/lichao/DT_CMR_analysis_collection/DT_CMR_analysis_2.9/matlab_files/organise_diff_dicoms.m',569,0)">line 569</a>)
                    [unet_masks] = unet_heart_segmentation_3c(code_filepath,imgs,info);
        Error in <a href="matlab:matlab.internal.language.introspective.errorDocCallback('DT_CMR_analysis', '/home/lichao/DT_CMR_analysis_collection/DT_CMR_analysis_2.9/DT_CMR_analysis.m', 814)" style="font-weight:bold">DT_CMR_analysis</a> (<a href="matlab: opentoline('/home/lichao/DT_CMR_analysis_collection/DT_CMR_analysis_2.9/DT_CMR_analysis.m',814,0)">line 814</a>)
                                =organise_diff_dicoms...
        Error in <a href="matlab:matlab.internal.language.introspective.errorDocCallback('run', '/usr/local/MATLAB/R2022b/toolbox/matlab/lang/run.m', 91)" style="font-weight:bold">run</a> (<a href="matlab: opentoline('/usr/local/MATLAB/R2022b/toolbox/matlab/lang/run.m',91,0)">line 91</a>)
        evalin('caller', strcat(script, ';'));'
    ```

   1. Missing `[Program v2.9 Source]/deep_learning` folder in the program v2.9 source. 
   - The Program v2.9 in the MacMini in CMR Office B misses the folder. This folder is for the AI module. 
   - Usually crash when the windows shows "denoising dicom..." 
   - Make sure you have write permission of this folder by `sudo chmod -R 777 [xx]/deep_learning`, because temp_file will written in this folder

   2. Tersorflow Version (happend on MacOS M2). 
   - Loading tensroflow module failed. Reinstall tensorflow using `SYSTEM_VERSION_COMPAT=0 pip install tensorflow-macos tensorflow-metal`. Usually crash when the windows shows "segmentation..." after "denoising dicom..."

   3. Unknown Error happened on Yanglab (The example). This error occurs when turn on AI. 

   4. A useful way to check the error is to add a break point on `matlab_files/unet_heart_segmentation_3c.m` in line 60: “load([code_filepath '/deep_learning/prediction.mat']);”. Then check variables `r` and `s`. This may record the reason.







