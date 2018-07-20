### HIEvPy Search


```python
import os
import hievpy as hp
```

Load in your API token
```python
api_token = os.environ['HIEV_API_KEY']
```

Use the hievpy search function to return a list of all files within HIEv that have been uploaded to HIEv since 
January 1st 2018 and that belong to the EucFACE experiment 31


```python
results = hp.search(api_token, experiments=['31'], upload_from_date="2018-01-01")
```

Check how many files have been returned


```python
len(results)
```




    84



Have a deeper look at the first record returned


```python
results[0]
```




    {'access_rights_type': None,
     'contributors': ['David Ellsworth', 'Teresa Gimeno', 'Vinod Kumar'],
     'created_at': '2018-03-14T00:03:49+11:00',
     'created_by_id': 26,
     'creator': 'Teresa Gimeno (t.gimeno@uws.edu.au)',
     'end_time': '2014-08-31T10:00:00+10:00',
     'experiment_id': 31,
     'facility_id': 7,
     'file_id': 225647,
     'file_processing_description': 'This file is associated with the following publication:\r\n\r\nTitle: \r\nElevated CO2 did not affect the hydrological balance of a mature native Eucalyptus woodland\r\n\r\nAuthors list: \r\nTeresa E. Gimeno, Tim R. McVicar, Anthony P. O’Grady, David T. Tissue and David S. Ellsworth\r\n\r\nAccepted for publication in Global Change Biology on the 12 March 2018\r\n\r\nCorresponding author: Teresa E. Gimeno (teresa.gimeno@inra.fr, tegimeno@gmail.com).\r\n\r\nEven if these data are public, please consider contacting the corresponding author if you are planning to work with them.\r\n\r\nThis file contains mean (of the six rings, unless stated otherwise) daily meteorological measurements from the EucFACE experimental site from 1 September 2012 to 1 September 2014. This file contains the following variables: \r\n\r\nDate: date variable (format yyyy-mm-dd)\r\nTmean_C: numerical variable, mean daily temperature in °C\r\nTmax_C: numerical variable, maximum daily temperature in °C\r\nTmin_C: numerical variable, minimum daily temperature in °C\r\nRH_percent: numerical variable, mean daily relative humidity in %\r\nPAR_mol_day.1:  numerical variable, total daily incoming photosynthetic photon flux density in mol/day\r\nNetRad_mm_day.1:  numerical variable, total net radiation in mm/day\r\nVPD_kPa: numerical variable, mean daily vapour pressure deficit in kPa (see equations 14-24, 7-2 and 7-1 in the LICOR 6400 manual)\r\nVPDz_kPa: numerical variable, day-length normalized mean vapour pressure deficit in kPa (see Tor-ngren et al. 2015 New Phytologist 205:518)\r\nP_kPa: numerical variable,  mean daily atmospheric pressure in kPa (only one sensor for the whole EucFACE site)\r\nrain_mm_day.1: numerical variable,  numerical variable,  total daily incoming precipitation (mean of gauges on top of the towers of rings 1, 3 and 4) in mm/day\r\nWS_m_s.1: numerical variable,  mean (anemometers only on rings 1, 4 and 5) daily wind speed in m/s\r\nGust_m_s.1: numerical variable,  daily maximum (anemometers only on rings 1, 4 and 5) gust speed in m/s\r\nEp_mm_s.1: numerical variable, total daily potential evapotranspiration (see Eq. 1 in associated paper: Gimeno et al. 2018, GCB) \r\n',
     'file_processing_status': 'PROCESSED',
     'file_size': 147538.0,
     'filename': 'Gimeno_wb_EucFACE_meteo.csv',
     'format': 'text/plain',
     'grant_numbers': [],
     'id': '',
     'interval': None,
     'labels': ['Air Temperature',
      'General Radiation',
      'PAR',
      'Relative Humidity'],
     'path': '/data/dc21-data/Gimeno_wb_EucFACE_meteo.csv',
     'published': False,
     'published_by_id': None,
     'published_date': None,
     'related_websites': [],
     'start_time': '2012-09-01T10:00:00+10:00',
     'updated_at': '2018-03-14T00:47:35+11:00',
     'url': 'https://hiev.westernsydney.edu.au/data_files/225647/download.json'}



Read the _start time_ of this first record


```python
results[0]['start_time']
```




    '2012-09-01T10:00:00+10:00'