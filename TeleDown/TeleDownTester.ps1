$time = get-date
$mon = $time.Month
$day = $time.Day
$yr = $time.Year
$h = $time.Hour
$m = $time.Minute
$s = $time.Second
$VAR1 = "."
$VAR2 = "-"
$fileName = "$mon$VAR1$day$VAR1$yr$VAR2$h$VAR1$m$VAR1$s"
python TeleDown\teleDown.py $fileName
# python C:\Users\micel\Documents\Spring 2020\Capstone\survey_drone\TeleDown\TeleDown.py $fileName