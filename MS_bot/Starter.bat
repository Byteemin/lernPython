@echo off
chcp 65001
cls
call %~dp0\venv\Scripts\activate
cd %~dp0

set TOKEN=""

rem python inline_example.py
rem python inline_mode_example.py
python bot.py

pause