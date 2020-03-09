##Set-ExecutionPolicy RemoteSigned (required to run bash scripts)
#to run - .\control1.ps1

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