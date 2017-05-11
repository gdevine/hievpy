# HIEvPy
HIEvPy is a python package for interfacing with the [HIEv](https://hiev.westernsydney.edu.au), a data capture application used by the [Hawkesbury Institute for the Environment](https://www.westernsydney.edu.au/hie) at Western Sydney University. HIEvPy provides programmatic shortcuts for the following operations in HIEv:
- Search


**To use HIEVPY you must have an account on HIEv.**
### Installation
Pre-requisites required on local machine
- Python (python2.7)
- Pip
- Git

You can install HIEvPy directly from the main GitHub repository using:
```sh
$ pip install git+git://github.com/gdevine/hievpy.git
```
Note: the 'sudo' command should only be used if you are installing HIEvPy system-wide. Otherwise, you may want to use the “--user” flag for a local user install, e.g.:
```sh
$ pip install --user git+git://github.com/gdevine/hievpy.git
```
Make sure your user install executable directory is on your PATH. For example consider adding this at the end of your ~/.bash_profile file
```sh
export PATH="$PATH:/Users/Username/Library/Python/2.7/bin"
```
Once HIEvPy has been installed, you can import it into a python console or script using:
```sh
from hievpy import hievpy
```
