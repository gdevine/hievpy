
#### Import hievpy library


```python
import hievpy as hp
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

#### Set the search parameters


```python
search_params = {"filename": "DRL_AUTO_450LO_SOIL_R",
                 "from_date": "2017-01-02",
                 "to_date": "2018-01-01"}
```

#### Run the hievpy search function using the search parameters


```python
records = hp.search(api_token, base_url, search_params)
```

#### Check the results


```python
for record in records: print(record['filename'])
```

    DRL_AUTO_450LO_SOIL_R_20171130.dat
    DRL_AUTO_450LO_SOIL_R_20170131.dat
    DRL_AUTO_450LO_SOIL_R_20170731.dat
    DRL_AUTO_450LO_SOIL_R_20170430.dat
    DRL_AUTO_450LO_SOIL_R_20171031.dat
    DRL_AUTO_450LO_SOIL_R_20170331.dat
    DRL_AUTO_450LO_SOIL_R_20170228.dat
    DRL_AUTO_450LO_SOIL_R_20170630.dat
    DRL_AUTO_450LO_SOIL_R_20180131.dat
    DRL_AUTO_450LO_SOIL_R_20170531.dat
    DRL_AUTO_450LO_SOIL_R_20170930.dat
    DRL_AUTO_450LO_SOIL_R_20170831.dat
    DRL_AUTO_450LO_SOIL_R_20171231.dat
`
