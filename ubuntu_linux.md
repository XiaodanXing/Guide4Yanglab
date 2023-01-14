## INSTALL RDP ON LINUX

>Require sudo authority

>Reproduced from https://www.80sy.com/715/html

```
http://www.c-nergy.be/downloads/install-xrdp-3.0.zip
unzip install-xrdp-3.0.zip
chmod 777 Install-xrdp-3.0.sh
./Install-xrdp-3.0.sh
```

Restart the machine by shutdown -r now

### To access RDP from a remote computer with Zerotier access
For Windows
1. Open “remote desktop connection” by searching “RDP”
2. Key in Zerotier IP address for connection
3. Follow on-screen protocol to login into your server account

## To disable animation on Ubuntu
1.	Launch software (From Applications)
2.	Search GNOME Tweaks and install it
3.	Launch GNOME Tweaks
4.	Appearance  Animation  OFF

## To install Teamviewer on Ubuntu
1.	Launch software (From Applications)
2.	Search Teamviewer and install it
3.	Launch Teamviewer
>Below recommended
4.	Set up a free Teamviewer account and login into it on the desktop software
5.	To set up a personal password for access: 
`Teamviewer --> Extras --> options --> Advanced --> Personal password`

## INSTALL MATLAB ON UBUNTU
###Require sudo authority###
1.	Follow standard protocol to register and set up an account with `MATLAB` on `mathworks.com`
2.	Download MATLAB installer (e.g., `matlab_R2022b_glnxa64.zip`)
3.	Open `terminal` in the directory where the installer is located
```
sudo unzip -X -K <installer zip file name> -d matlab_installer
cd matlab_installer
sudo ./install
```
4.	A GUI window will pop up
5.	Follow on-screen instructions to finish the MATLAB set up
6.	Launch `software` (From `Applications`)
7.	Search `MATLAB` and install it
8.	Follow on-screen instructions to finish setting up `MATLAB` as a stand-alone Application
9.	Launch `MATLAB` (From `Applications`)
