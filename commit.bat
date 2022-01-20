@echo on
git add .
pause
git commit -m %date%::%time%
pause
git push -u origin main
pause