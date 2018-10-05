
# HIEvPy
HIEvPy is a python 3 wrapper around the API interface of the [HIEv](https://hiev.westernsydney.edu.au), a data capture 
application used by the [Hawkesbury Institute for the Environment](https://www.westernsydney.edu.au/hie) at [Western 
Sydney University](https://westernsydney.edu.au). 

A short overview of the HIEvPy library, including installation instructions, is given below. Full 
documentation, with examples, can be found on the project's [documentation pages](https://gdevine.github.io/hievpy).



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

Once **HIEvPy** has been installed, you can import it into a python console or script using:

``` python
import hievpy as hp
```
(using the optional *as hp* as a shortcut)

### HIEvPy functions

##### Generic functions
- search
- search_download
- upload
- update_metadata

##### TOA5 functions
- toa5_summary
- search_loaf_toa5df

See the project's [documentation pages](https://gdevine.github.io/hievpy) for a full explanation of all **HIEvPy** functions

### Examples
The __examples__ folder contains a number of example scripts outlining usage of the different **HIEvPy** functions. 

To run any of the example scripts you need to create a file called *credentials.py* and populate it with your HIEv 
API token, e.g:
  
    hiev_api_key = 'my_hiev_api_token'


### License

