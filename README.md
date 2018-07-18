
> Full documentation, with examples, can be found [here](https://gdevine.github.io/hievpy)

### HIEvPy
HIEvPy is a python wrapper around the API interface of the [HIEv](https://hiev.westernsydney.edu.au), a data capture 
application used by the [Hawkesbury Institute for the Environment](https://www.westernsydney.edu.au/hie) at [Western 
Sydney University](https://westernsydney.edu.au). 

**To use HIEvPY you must have an account on HIEv**

### Installation
HIEvPy can be installed via *pip*:

``` bash
$ pip install --index-url https://test.pypi.org/simple/ hievpy
```

> Note: HIEvPy is currently hosted on Test PyPi. This will soon be moved to the official PyPi repository


Once HIEvPy has been installed, you can import it into a python console or script using:

``` python
import hievpy as hp
```


### Instructions

*Docstrings, outlining the full functionality, have been provided against all primary functions and can be accessed using help(function), for example*
```sh
help(hievpy.search_hiev)
```


All commands available via HIEvPy will require passing in your HIEv API key. Please consider keeping your API key outside of your actual
code (particularly if you intend on sharing code). Instead, store your API key in a separate file or in a local environment variable.


#### Search
To search against the HIEv database, you can use
```sh
hievpy.search(api_key, <optional args>)
```

Use the help function on *hievpy.search* to see a full list of optional search arguments.

**It is highly recommended that you supply at least one search query to your search to limit returning the full database in one call**

As an example, to search for all records with data for February 2017 from the DriGrass facility and save to a variable called *dgFiles* use:
```sh
dgFiles = hievpy.search(<MY_API_KEY>, from_date="2017-02-01", to_date="2017-02-28", facilities=['10'])
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
