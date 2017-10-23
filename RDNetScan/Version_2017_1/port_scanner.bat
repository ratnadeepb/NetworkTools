@echo off
set host=%1
set port=%2
nc.exe -zv %host% %port% > NUL 2>&1
if not errorlevel 1 echo %port%