@echo off
title Starting clam
echo y|rmdir /s ..\temp\temp
mkdir ..\temp\temp
waitfor SomethingThatIsNeverHappening /t 5
rem timeout /T 5 /nobreak > nul
exit