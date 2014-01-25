@echo off
color FC
TITLE [ GEN - Josh Bosley ]
mode con:cols=25 lines=10
echo Deleting old files.  .  .
del xFileGen\shop\*.* /Q
del xFileGen\config\*.* /Q
echo Initiating Gen.  .  .
cd xFileGen\
C:\Python27\python.exe xGenFiles.py
echo .
echo Completed!
pause
