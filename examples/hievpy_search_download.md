

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

    100%|██████████| 30/30 [00:04<00:00,  7.36it/s]



```python

```
