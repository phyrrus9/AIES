@echo off
:loop
color F9
mode con:cols=35 lines=20
TITLE [ Expert System - Josh Bosley ]
echo   .                             .
echo  [Technical Expert Support System]
echo   `			     `
echo               _.---._    /\\
echo            _/`       "--`\//
echo          _/      !       x \
echo         /_/\  )______   \__ \
echo        //  / /\ \    /\ \  \ \
echo        `  / /  \ \  / /\ \  ``
echo            "     "   "   " 
echo             _________ 
echo            [ T.E.S.S ]   J.B
echo 	   [    A    ]  2013
echo        ____[  Python ]______
echo       [ based expert system ]
echo      /_______________________\  
set /P wait=.

mode con:cols=80 lines=42

cd bin\
C:\Python27\python.exe Main.py

goto loop