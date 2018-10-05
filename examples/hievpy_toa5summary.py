import hievpy as hp

# Import the credentials file (to read HIEv API token)
import examples.credentials as c


# Set the base URL of the HIEv instance being called against
base_url = 'https://hiev.westernsydney.edu.au/'

# Set API/Auth token
api_token = c.hiev_api_key

# Set up search filters
search_params = {"filename": "DRL_AUTO_250HI_SOIL_R_20181031.dat"}

# Search for all records matching the filter
records = hp.search(api_token, base_url, search_params)

# Assuming one record returned, pass the first result to toa5_summary
record = records[0]
hp.toa5_summary(api_token, record)
