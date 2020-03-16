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

* Navigate to GroupD_TGOF\src
* run `python -m frupal`
* or run `python3 -m frupal`if you have python2 and python3 installed

## Compiling Into Program Executable
```bash
python3 -m venv venv
pip install pyinstaller
pyinstaller src/main.py -n Frupal -F --icon=src/frupal.ico
```

src/main.py is the script, "-n" names the resulting file(s) and -F sets it to package it in one exe, if you want the program in parts in a directory do -D