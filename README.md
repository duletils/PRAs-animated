# PRAs-animated
Manim animations, showing how different Page Replacement Algorithms work

This project is still in the works.

The plan is to animate more PRAs. Final goal is a program that can generate a task for practicing PRAs, and the accompanying animation for clarification.

# Dependencies
## Linux
### git
It usually comes preinstalled with many Linux distros. To check if it is installed, run

```
git --version
```

If you get the version number, it is installed. Otherwise, use your package manager to install it.

Redhat/Fedora:

```dnf install git```

Debian/Ubuntu (not tested):

```apt install git```

Arch (not tested):

```pacman -S git```

### Python
It usually comes preinstalled with many Linux distros. To check if it is installed, run

```python --version```

If you get the version number, it is installed. Otherwise, use your package manager to install it.

Redhat/Fedora:

```dnf install python3```

Debian/Ubuntu (not tested):

```apt install python3```

Arch (not tested):

```pacman -S python```

### pip
__pip__ is a package manager for Python.

Redhat/Fedora:

```dnf install python3-pip```

Debian/Ubuntu (not tested):

```apt install python3-pip```

Arch (not tested):

```pacman -S python-pip```

### Manim
__Manim__ is the animation library for Python:

```pip install manim```

## Windows (not tested)
### git
Get the official windows installer [here](https://git-scm.com/install/windows).

### Python
Go to the official Python website [python.org](https://www.python.org) and choose an appropriate installer. When prompted, select the "Add to system PATH" option.
The installer should also automatically install __pip__.

### Manim
```pip install manim```

# Rendering the animations

Clone this repository with git:

```git clone https://github.com/duletils/PRAs-animated.git```

To render an animation explaining a PRA, run the following command in the root directory of the repo:

```manim -pqh explanations/<choosen PRA>.py```

This will play the animation immediately after rendering. If you don't want this, omit the __p__ flag in __-pqh__. This will also render the animation in high quality (1080p 60fps). 
If you want medium (720p 30fps) or low quality (480p 15fps), use __qm__ and __ql__ flags respectively.

The rendered animations will be in the _media_ directory.
