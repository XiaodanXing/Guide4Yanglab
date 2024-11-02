# <span id="top" style="color:#2E86C1 ">*A manual for new starters in our group [`ayanglab`](https://www.yanglab.fyi/)*</span>

* `NOTE`
  * this repo will be transferred to https://github.com/ayanglab in a near future

<br>

## <span style="color:#2E86C1 ">*Table of Contents*</span>
* [*FAQ*](#faq) 
* [*Computational Resources in `ayanglab`*](#cria)
* [*JADE2*](#jade2)
* [*NAS*](#nas)
* [*Datasets overview*](#data)
* [*SSH Connection*](#ssh)
* [*Trello*](#trello)
* [*Build Environment*](#env)
* [*Remote Desktop*](#rm)
* [*Matlab*](#rm)
* [*Office Key*](#key)
* [*Office AC*](#ac)
* [*Journal Club*](#journalclub)


<br>
<br>
<br>


## <span id="faq" style="color:#2E86C1 ">*FAQ*</span>
If you have any questions, <span style="color:red; font-size:1em">*please post it on issues*</span>, or find answers in  [FAQ](FAQ/FAQ.md).

### <span style="color:#2E86C1 ">*How to raise questions?*</span>
1. raise an issue in this [repository](https://github.com/XiaodanXing/Guide4Yanglab/issues)
2. email anyone you think can help with this issue and CC Dr Guang Yang

### <span style="color:#2E86C1 ">*How to propose suggestions?*</span>
1. raise an issue in this [repository](https://github.com/XiaodanXing/Guide4Yanglab/issues)
2. provide your suggestions and solutions in the issue
3. email anyone you think can help with this issue and CC Dr Guang Yang

---
<br>
<br>


## <span id="cria" style="color:#2E86C1 ">*Computational Resources in `ayanglab`*</span>

### <span style="color:#2E86C1 ">*Local Workstations*</span>

|Name|Administrator|Email|
| :--- | :---: | ---: |
|yanglab0|Shiyi Wang <br> Zeyu Tang| s.wang22@imperial.ac.uk <br> zeyu.tang19@imperial.ac.uk |
|yanglab |Jiahao Huang| j.huang21@imperial.ac.uk |
|yanglab1|Ming Li| ming.li@imperial.ac.uk |
|yanglab2|Yang Nan| y.nan20@imperial.ac.uk |
|yanglab3|Xiaodan Xing| x.xing@imperial.ac.uk |
|yanglab4|Yingying Fang| y.fang@imperial.ac.uk |
|yanglab5|-| - |
|yanglab6|-| - |
|yanglab7|Yinzhe Wu| yinzhe.wu18@imperial.ac.uk |
|yanglab8|Fanwen Wang| fanwen.wang@imperial.ac.uk |
|yanglab9|-| - |
|yanglab10|-| - |
|yanglab11|-| - |
|yanglab12|-| - |
|yanglab13|-| - |
|yanglab14|-| - |
|yanglab15|-| - |
|DistriM|Ming Li|ming.li@imperial.ac.uk|

* check workstation IP in `Teams` [*Path: Files/Workstation Information*](https://teams.microsoft.com/_?culture=en-us&country=ww#/one/viewer/teamsSdk/https:~2F~2Fimperiallondon.sharepoint.com~2Fsites~2FAYangLab-WH~2FShared%20Documents~2FGeneral~2FWorkstation%20Information~2FWorkstations%20IP?threadId=19:f49b4c67b1894aff9ea2738829473de3@thread.tacv2&subEntityId=%257B%2522viewParams%2522%253A%2522id%253D%25252Fsites%25252FAYangLab%25252DWH%25252FShared%252520Documents%25252FGeneral%25252FWorkstation%252520Information%2526viewid%253D4a7c2a42%25252Da573%25252D433d%25252Da1ef%25252D21960f1d0619%2522%257D&baseUrl=https:~2F~2Fimperiallondon.sharepoint.com~2Fsites~2FAYangLab-WH&fileId=5bb99d8c-2ed8-4f5d-b941-abc50894f628&ctx=openFilePreview&viewerAction=view)
* ask Dr Guang Yang for `Teams` permission
---
<br>

### <span id="jade2" style="color:#2E86C1 ">*JADE2*</span>
* For more instructions on how to use JADE2, please check [JADE tutorial](docs/JADE2_Tutorial.md).
---
<br>

### <span id="nas" style="color:#2E86C1 ">*Colab*</span>
* For more instructions on how to set up on Google Colab, please check [Set up Google Colab](boilerplate_code/Colab.md).
---
<br>

### <span style="color:#2E86C1 ">*Dataset storage - NAS*</span>

|Name|NAS mount path on local workstation|Administrator|Email|
| :--- | :---: | :---: | ---: |
|NAS1| /media/NAS00 |-| - |
|NAS2| /media/NAS01 <br> /media/NAS02 |-| - |
|NAS3| /media/NAS03 |-| - |
|NAS4| /media/NAS04 |-| - |
|NAS5| /media/NAS05 |-| - |
|NAS6| /media/NAS06 |-| - |
|NAS_CMR| /media/NAS_CMR |-| - |
|NAS_CMR2| /media/NAS_CMR2 |-| - |


* `Attention`: 
  * we are not running a company, we are just a research lab, we do not have any IT or Operation & Maintenance engineers
  * our NASs are not Enterprise Data Warehouse and we do not have disaster recovery backup
  * <span style="color:red; font-size:1em">*please do not load data to gpus from /media/NAS\* directly*</span>
  * when you train models, please transfer data to corresponding workstations, every workstation has large local HDD or SSD (path: /media/hdd or /media/ssd, use command `"df -h"` to check the path)
  * <span style="color:red; font-size:1em">*only use NAS for dataset/models/projects backup*</span>

### <span style="color:#2E86C1 ">*How to set up NAS?*</span>
* please refer to `Teams` [*Path: Team notes*](https://teams.microsoft.com/_?culture=en-us&country=ww#/school/tab::10b584f9-7333-490e-9e55-86198110e8d7/General?threadId=19:f49b4c67b1894aff9ea2738829473de3@thread.tacv2&ctx=channel)

### <span id="data" style="color:#2E86C1 ">*Datasets overview*</span>
* please refer to `Teams` [*Path: Team notes*](https://teams.microsoft.com/_?culture=en-us&country=ww#/school/tab::10b584f9-7333-490e-9e55-86198110e8d7/General?threadId=19:f49b4c67b1894aff9ea2738829473de3@thread.tacv2&ctx=channel)
	* before you download any dataset from the internet, check `Teams notes` in case repeated storage (save NAS space)
	* once you save any new dataset on NAS, please remember to update the `Teams notes`

---
<br>

### <span id="ssh" style="color:#2E86C1 ">*SSH access to local workstations*</span>

Zescaler:
1. install [zescaler](https://uafiles.cc.ic.ac.uk/)
2. find the Zscaler client connector icon and selecting ‘Open Zscaler’
3. log in as username@ic.ac.uk with your standard Imperial password
4. Use ssh to connect to the workstation, please refer to `Teams` [*Path: Team notes*](https://imperiallondon.sharepoint.com/:o:/r/sites/AYangLab-WH/Shared%20Documents/General/Workstation%20Information/Workstations%20IP?d=w5bb99d8c2ed84f5db941abc50894f628&csf=1&web=1&e=zcrDjP)
5. For other questions, please refer to `Unified Access in Imperial` [*Path: Unified Access*](https://www.imperial.ac.uk/admin-services/ict/self-service/connect-communicate/remote-access/unified-access/)

Zerotier:
1. install [zerotier](https://www.zerotier.com/download/)
2. ask Dr Guang Yang for oral zerotier access permission
3. email Ming Li (CC Dr Guang Yang) to authorize your zerotier connection
   (provide your zerotier address e.g., 530c509607)
4. login workstation (ask corresponding administrator	to help you set up new account)

---
<br>
<br>

## <span id="trello" style="color:#2E86C1 ">*Share the trello board*</span>

1. Register a Trello account using imperial email in [Trello](https://trello.com/)
2. Find project management in the template and create a workspace and board from this templete
3. Change the workspace and board name to PhD students (Your Name)
4. Share this workspace to Dr Guang Yang's email

---
<br>
<br>

## <span id="env" style="color:#2E86C1 ">*Building local environments*</span>
* please refer to [building local environments](docs/hands_on_tutorial.md) and [reinstallation of CUDA](docs/cuda-installation.md)


---
<br>
<br>


## <span id="rm" style="color:#2E86C1 ">*GUI - `remote desktop` and `MATLAB`*</span>
* please refer to [remote_desktop_and_matlab](docs/remote_desktop_and_matlab.md)


---
<br>
<br>


## <span id="key" style="color:#2E86C1 ">*Office key holders*</span>

|Name|key number|
| :--- | :---: |
|Ming Li|1|
|Xiaodan Xing|1|
|Yang Nan|1|
|Jiahao Huang|1|
|Yingying Fang|1|
|Shiyi Wang|1|
|Fanwen Wang|1|
|Sheng Zhang|1|
||8 keys in total|


---
<br>
<br>


## <span id="ac" style="color:#2E86C1 ">*AC setting in our office*</span>
* please refer to [TOSHIBA_AC_setting_manual](docs/TOSHIBA_AC_setting_manual.pdf)


---
<br>
<br>


## <span id="journalclub" style="color:#2E86C1 ">*Journal Club*</span>

|time|speaker|topic|readings <br> slides|
| :--- | :---: | :---: | :---: |
|2023-01-27|Ming Li|Learning in the Frequency Domain|[link](journal_club/2023-01-27-Ming_Li-frequency/)|
|?|?|?|?|


<br>
<br>


:point_up_2: <span style="color:#2E86C1 ">*[Back to Top](#top)*</span>
