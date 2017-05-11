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

Once HIEvPy has been installed, you can import it into a python console or script using:
```sh
from hievpy import hievpy
```


### Instructions

*Docstrings, outlining the full functionality, have been provided against all primary functions and can be accessed using help(function), for example*
```sh
help(hievpy.search_hiev)
```


All commands available via HIEvPy will require passing in your HIEv API key. Please consider keeping your API key outside of your actual
code (particularly if you intend in uploading to code repositories). Instead, store your API key in a separate file or in a local environment variable.


#### Search
To search against the HIEv database, you can use
```sh
hievpy.search_hiev(api_key, <optional args>)
```

Use the help function on *hievpy.search_hiev* to see a full list of optional search arguments.

**It is highly recommended that you supply at least one search query to your search to limit returning the full database in one call**

As an example, to search for all records with data for February 2017 from the DriGrass facility and save to a variable called *dgFiles* use:
```sh
dgFiles = hievpy.search_hiev(MY_API_KEY, from_date="2017-02-01", to_date="2017-02-28", facilities = ['14'])
```
