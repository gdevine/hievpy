## Search and Download
The _search_download_ function extends the __HievPy__ _search_ function by downloading found records to your 
local computer. It is structured in a similar manner to the _search_ function with the addition of an optional 
local path where records will be downloaded to.
  
```sh
import hievpy as hp
hp.search_download(api_token, base_url, search_params, path=None)
```

where
1. api_token: HIEv API token string
2. base_url: the base url string of the HIEv instance
3. search_params: Object containing metadata key-value pairs for searching
4. path: Optional full path of download directory (if path not provided, file will be downloaded to current 
directory)

**As with the _search_ function, it is highly recommended that you supply at least one search query to your 
search to limit returning the full database in one call**


## Example

> You can download a Jupyter notebook version of this example from the __/examples__ folder on the github 
project page.

As an example, to search for all records associated with experiment 82 dating back to 2nd January 2018 and 
download them to a subfolder called Downloads within the current location

## Example


```python
import hievpy as hp
from pathlib import Path
```

#### Import the credentials file and set the API token


```python
import credentials as c
api_token = c.hiev_api_key
```

#### Set the base URL of the HIEv instance being called against


```python
base_url = 'https://hiev.westernsydney.edu.au/'
```

#### Set the search filters


```python
search_params = {"experiments": ['82'],
                 "from_date": "2018-01-02"}
```

#### Set (or create if necessary) the folder to store the downloaded files


```python
downloads = Path.cwd() / 'Downloads'
downloads.mkdir(exist_ok=True)
```

#### Run the search and download the matching files to the specified path


```python
hp.search_download(api_token, base_url, search_params, path=downloads)
```
