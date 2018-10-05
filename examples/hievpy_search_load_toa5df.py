import hievpy as hp

# Import the credentials file (to read HIEv API token)
import examples.credentials as c


# Set the base URL of the HIEv instance being called against
base_url = 'https://hiev.westernsydney.edu.au/'

# Set API/Auth token
api_token = c.hiev_api_key

# Set up search filter
search_params = {"filename": "DRL_AUTO_450LO_SOIL_R",
                 "from_date": "2017-01-02",
                 "to_date": "2018-01-01"}

# Search for all records matching filter and load into a single, sorted dataframe
my_df = hp.search_load_toa5df(api_token, base_url, search_params)
