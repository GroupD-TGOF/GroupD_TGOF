# GroupD_TGOF

Github for CS300: Group D's version of The Game Of Frugal

Group D's Members:
- Adam LaFleur
- Silas Marvin
- Jonathan Sabini
- Nicholas Grout 
- Matthew Cole

## Branching (do before working!)

> [Download github desktop](https://desktop.github.com/)
* Switch to `inprogress` branch
* Branch off this branch
* Push while on your branch
* Open a pull request, ask others to review

```bash
git checkout -b [myname]-[mycomponent]
```

## Setup

```bash
python3 -m venv venv
pip3 install -r requirements.txt
```

## Running

* Navigate to root directory
* run `python3 main.py`

## Compiling Into Program Executable
```bash
python3 -m venv venv
pip install pyinstaller
pyinstaller --onefile pythonScriptName.py
```
pythonScriptName is the name of the main file of the python program being created. Pyinstaller should be able to detect the current operating system and create an executable accordingly.
