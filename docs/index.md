### Overview
HIEvPy is a python 3 wrapper around the API interface of the [HIEv](https://hiev.westernsydney.edu.au), a data capture 
application used by the [Hawkesbury Institute for the Environment](https://www.westernsydney.edu.au/hie) at [Western 
Sydney University](https://westernsydney.edu.au). 


### Pre-requisites
To use HIEvPY you must have an active account (and subsequently a HIEv API token) on the 
[**HIEv**](https://hiev.westernsydney.edu.au) application. To discuss registration please contact HIE's data manager, 
[Gerry Devine](mailto:g.devine@westernsydney.edu.au)


### Installation
HIEvPy can be installed via *pip*:

``` bash
$ pip install --index-url https://test.pypi.org/simple/ hievpy
```

> Note: HIEvPy is currently hosted on Test PyPi. This will soon be moved to the official PyPi repository

Once HIEvPy has been installed, you can import it into a python console or script using:

``` python
import hievpy
```
(or optionally *import hievpy as hp* as a shortcut)


### HIEv API key 
The majority of commands available via HIEvPy will require passing in your HIEv API key for authentication purposes. 
It is highly reccomended that you keep your API key outside of your actual code (particularly if you intend on sharing 
code). Instead, store your API key in a private file or in a local environment variable.


### HIEvPy Functions

#### Search
To search for records within HIEv database, you can use the hievpy _search_ function:
```sh
hievpy.search(api_key, <optional args>)
```

Use the help function on *hievpy.search* to see a full list of optional search arguments.

**It is highly recommended that you supply at least one search query to your search to limit returning the full database in one call**

As an example, to search for all records with data for February 2017 from the DriGrass facility and save to a variable called *dgFiles* use:
```sh
dgFiles = hievpy.search(<MY_API_KEY>, from_date="2017-02-01", to_date="2017-02-28", facilities=['10'])
```

A more thorough walkthrough of the HIEvPy search fuction can be found here:\
[HIEvPy Search Example](notebooks/hievpy-search.md)

Or, alternatively, download a working jupyter notebook of this example:\
[HIEvPy Search Jupyter Notebook](notebooks/hievpy-search.ipynb)

 
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
