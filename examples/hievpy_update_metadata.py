import hievpy as hp

# Import the credentials file (to read HIEv API token)
import examples.credentials as c


# Set the base URL of the HIEv instance being called against
base_url = 'https://hiev.westernsydney.edu.au/'

# Set API/Auth token
api_token = c.hiev_api_key

# Search for, and update, the Creator and Description field of the 'hievpy_test_upload_file' (that can be uploaded to
# hiev via the example hiev_upload routine)
search_params = {"filename": "hievpy_test_upload_file"}

records = hp.search(api_token, base_url, search_params)

updates = {'creator_email': 'g.devine@uws.edu.au',
           'file_processing_description': 'Testing hievpy update function'}

hp.update_metadata(api_token, base_url, records, updates)
