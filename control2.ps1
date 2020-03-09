#! python3
##Set-ExecutionPolicy RemoteSigned (required to run bash scripts)
#to run - .\control2.ps1

#commands to execute YOLO
cd C:\Users\caile\Documents\GitHub\TrainYourOwnYOLO\
py -m venv env
.\env\Scripts\activate
cd .\3_Inference\
py .\Detector.py
deactivate
cd C:\Users\caile\Documents\GitHub\survey_drone\

#commands to execute GeoDim
$test = unitTest.csv
$filname = YOLOv3 Output Files\Test_Image_Detection_Results\Detection_Results.csv
python GeoDim\GeoDim.py $test
#python GeoDim\GeoDim.py $filname
