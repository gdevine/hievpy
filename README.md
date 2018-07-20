
# HievPy

A short overview of the HIEvPy library, including installation instructions, is given below. Full 
documentation, with examples, can be found on the project's [documentation pages](https://gdevine.github.io/hievpy).


#### Overview
HIEvPy is a python wrapper around the API interface of the [HIEv](https://hiev.westernsydney.edu.au), a data capture 
application used by the [Hawkesbury Institute for the Environment](https://www.westernsydney.edu.au/hie) at [Western 
Sydney University](https://westernsydney.edu.au). 


#### Pre-requisites
To use HIEvPY you must have an active account (and subsequently a HIEv API token) on the 
[**HIEv**](https://hiev.westernsydney.edu.au) application. To discuss registration please contact HIE's data manager, 
[Gerry Devine](mailto:g.devine@westernsydney.edu.au)


#### Installation
HIEvPy can be installed via *pip*:

``` bash
$ pip install --index-url https://test.pypi.org/simple/ hievpy
```

> Note: HIEvPy is currently hosted on Test PyPi. This will soon be moved to the official PyPi repository

Once HIEvPy has been installed, you can import it into a python console or script using:

``` python
import hievpy as hp
```
(using the optional *as hp* as a shortcut)


### Instructions

*Docstrings, outlining the full functionality, have been provided against all primary functions and can be accessed using help(function), for example*
```sh
help(hievpy.search_hiev)
```



#### Download
The HIEvPy.download function can be used in conjunction with the search function to download a file from HIEv (with option to specify download location)
```sh
hievpy.download(api_key, search_record, <optional path>)
```

Use the help function on *hievpy.download* to see a full list of optional search arguments.

As an example, the following code is used to search for all files with data for March 15th 2017 from the Mini-ROS/DriGrass facility and to download the results to a directory called DG_DATA (directory must exist)
```sh
dg_files = hievpy.search(MY_API_KEY, from_date="2017-03-15", to_date="2017-03-16", facilities=['10'])
for dg_file in dg_files:
    hievpy.download(<MY_API_KEY>, dg_file, path='/Users/<USERNAME>/DG_DATA/')
```


#### Load
The HIEvPy.load function can be used in conjunction with the search function to load a file from HIEv into memory
```sh
hievpy.load(api_key, search_record)
```

As an example, the following code is used to locate the file called 'FACE_R3_B1_SoilVars_20161130.dat' and load it into memory.
*(Note that face_file[0] is passed to hievpy_load given that the single result from the search is still part of a list.)*
```sh
face_file = hievpy.search(MY_API_KEY, filename="FACE_R3_B1_SoilVars_20161130.dat")
im_file = hievpy.load(<MY_API_KEY>, face_file[0])
```
