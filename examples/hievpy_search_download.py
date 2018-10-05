import hievpy as hp
from pathlib import Path

# Import the credentials file (to read HIEv API token)
import examples.credentials as c


# Set the base URL of the HIEv instance being called against
base_url = 'https://hiev.westernsydney.edu.au/'

# Set API/Auth token
api_token = c.hiev_api_key


# Set the search filters
search_params = {"experiments": ['82'],
                 "from_date": "2018-01-02"}

# Set (or create if necessary) the folder to store the downloaded files
downloads = Path.cwd() / 'Downloads'
downloads.mkdir(exist_ok=True)

# Run the search and download the matching files to the specified path
hp.search_download(api_token, base_url, search_params, path=downloads)
