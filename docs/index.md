## Overview
The [HIEv](https://hiev.westernsydney.edu.au) data capture system, hosted at the Hawkesbury Institute for the 
Environment (HIE) at Western Sydney University, is an application allowing both automated (e.g via sensor-based 
networks) and manual upload of data into a secure and centralised data server. Registered users have the ability 
to explore and download hosted data for further scientific analysis and exploration. At its core the HIEv is designed 
to facilitate and encourage the sharing of, reuse of, and collaboration around data, thus maximising scientific 
advancement. The HIEvPy library facilitates interaction with the HIEv application using the Python programming language.


## HIEv Use
To use HIEvPY you must have an active account (and subsequently a HIEv API token) on the 
[**HIEv**](https://hiev.westernsydney.edu.au) application. To discuss registration please contact HIE's data manager, 
[Gerry Devine](mailto:g.devine@westernsydney.edu.au)


## Prerequisites
- pandas


## Installation
HIEvPy can be installed via *pip*:

``` bash
$ pip install hievpy
```

Once HIEvPy has been installed, you can import it into a python console or script using:

``` python
import hievpy as hp
```
(using the optional *as hp* as a shortcut)


## HIEv API token 
The majority of HIEvPy functions will require passing in your HIEv API key/token for authentication purposes. 
It is important that you keep your API token outside of your actual code (particularly if you intend on sharing 
code). Instead, either: 

- **(Preferred)** Store your API token in a local environment variable and load it into your code, e.g:

```python
api_token = os.environ['HIEV_API_KEY']
```

or

- Store your token in a separate file, e.g. create a file called _credentials.py_ and populate it with:

```python
hiev_api_token = 'MY_API_KEY'
```   

and then call it in your code with someting like:
```python
import credentials as c
api_token = c.hiev_api_token 
```   

If choosing the latter, ensure that you do not share this credentials file directly with others.

> Your HIEv API key/token can be found by logging into the HIEv website and clicking on "settings" in the top right and 
clicking on your account name. 


## HIEv Base URL
Whilst the __HIEvPy__ library was originally written for the HIEv application hosted at HIE, additional 
instances of the HIEv are now in place at different locations, each with their own web url. It is therefore required to
pass the 'base url' of the HIEv that you are working with to each of the different __HIEvPy__ functions, e.g.:

```python
# Set the base URL of the HIEv instance being called against
base_url = 'https://hiev.westernsydney.edu.au/'
```   
    

## HIEvPy Functions

##### Generic functions
- **search**: Return a list of HIEv records matching a set of input search parameters  [read more...](notebooks/hievpy_search.md)
- **search_download**: Perform a hievpy search and automatically download the matching files [read more...](notebooks/hievpy_search_download.md)
- **upload**: Upload a file to HIEv with associated metadata
- **update_metadata**: Update metadata on a list of records returned by hievpy search

##### TOA5 functions
- **toa5_summary**: Returns toa5 summary information (variable names, units and measurement types) for a given
    individual search-returned record.
- **search_loaf_toa5df**: Performs a hievpy search and loads results into a pandas dataframe given the file records


