# Manim animations, showing how different Page Replacement Algorithms work

This project is still in the works.

The plan is to animate more PRAs. Final goal is a program that can generate tasks for practicing PRAs, and the accompanying animations for clarification.

# Dependencies

* __git__ - version control system
* __Python__ - programming language
* __venv__ - virtual environment utility for python
* __pip__ - package manager for python
* __gcc__ or other C compiler
* __cmake__ - build system for C and C++
* __Cairo__ - renderer
* __pkg-config__
* __Manim__ - animation library for Python

### Installing dependencies on Linux
Redhat/Fedora:

```
dnf upgrade
dnf install git python3 python3-virtualenv python3-pip gcc cmake cairo cairo-devel pkg-config
```

Debian/Ubuntu

```
apt update
apt upgrade
apt install git python3 python3.14-venv python3-pip gcc cmake libcairo2 libcairo2-dev libpangocairo-1.0-0 pkg-config
```

Arch

```
pacman -Syu
pacman -S git python python-pip gcc cmake cairo pkgconf
```

### Installing dependencies on Windows
Get the official git Windows installer [here](https://git-scm.com/install/windows).

Go to the official Python website [python.org](https://www.python.org/downloads/windows) and choose an appropriate Python installer. When prompted, tick the box next to "Add 
python.exe to PATH". Install it however you like, but be sure to include __pip__.

In my testing, other dependencies don't have to be installed explicitly.

# Setup and rendering

Clone this repository with git:

```
git clone https://github.com/duletils/PRAs-animated.git
```

## Installing Manim
### Linux
Before installing Manim, some distros might ask you to create a Python virtual environment. You can do it in the repo root:

```
cd PRAs-animated
python3 -m venv .
```
To activate the virtual environment, run the following in the folder where you made it:

```
source bin/activate
```

Then use __pip__ to install __Manim__:

```
pip install manim
```

### Windows
The process is the same as in Linux. In my testing, I used the __git__ cmd with bash, and didn't test PowerShell.

```
cd PRAs-animated
python -m venv .
pip install manim
```

### Rendering the animations
To render an animation explaining a PRA, run the following command in the root directory of the repo:

```
manim -pqh explanations/<choosen PRA>.py
```

This will play the animation immediately after rendering. If you don't want this, omit the __p__ flag in __-pqh__. This will also render the animation in high quality (1080p 60fps). 
If you want medium (720p 30fps) or low quality (480p 15fps), use __qm__ and __ql__ flags respectively.

The rendered animations will be in the _media_ directory.
