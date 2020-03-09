##Set-ExecutionPolicy RemoteSigned (required to run bash scripts)
#to run - .\control2.ps1

#commands to execute YOLO




#commands to execute GeoDim
$test = unitTest.csv
$filname = YOLOv3 Output Files\Test_Image_Detection_Results\Detection_Results.csv
python GeoDim\GeoDim.py $filname
