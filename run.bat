@echo off


set USER_PORT=4585


if not defined PYTHON (set PYTHON=python)
if not defined VENV_DIR (set "VENV_DIR=%~dp0%venv")

if not exist "%VENV_DIR%" python\python.exe -m venv venv
set PYTHON="%VENV_DIR%\Scripts\python.exe"

%PYTHON% -m pip install --upgrade pip
%PYTHON% -m pip install -r requirements.txt

%PYTHON% %~dp0%main.py