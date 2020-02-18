# survey_drone
Designed to be run in windows powershell

To activate windows powershell for unsigned scripts
    Run powershell as administrator
    Enter: set-executionpolicy remotesigned

Download Mission Planner
    https://ardupilot.org/planner/docs/mission-planner-installation.html

Python Packages - https://www.python.org/downloads/
    Python 2 required for Dronekit  (Python 2.7.17)
    Python 3 required for YOLOv3    (Python 3.8.1)
    Make sure to add to path variables: C:\Python27 and C:\Python27\scripts

verify pip was installed with python3: pip -v
If not - to download pip, enter:
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py

Python Supplemental Packages:
    pip install dronekit
    pip install pymavlink
    pip install numpy

STMicroelectonrics download to recognize COM ports
DFU bootloader required
download ardupilot hex to bootload onto FC:
    https://firmware.ardupilot.org/Copter/latest/
        select based on specific flight controller
        for Kakute F7: https://firmware.ardupilot.org/Copter/latest/KakuteF7/



.\control1.ps1 - runs TeleDown and Screenshotter - Designed for live use
.\control2.ps1 - runs YOLOv3 and GeoDim - Designed for post flight analysis
.\contorl3.ps1 - runs KeyControl - Designed for live use