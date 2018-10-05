import hievpy as hp
from pathlib import Path

# Import the credentials file (to read HIEv API token)
import examples.credentials as c


# Set the base URL of the HIEv instance being called against
base_url = 'https://hiev.westernsydney.edu.au/'

# Set API/Auth token
api_token = c.hiev_api_key


# Set path of file to be uploaded
upload_file = Path.cwd() / 'Uploads' / 'hievpy_test_upload_file'

# Set metadata variables for upload
metadata = {'creator_email': 'g.devine@westernsydney.edu.au',
            'description': 'Testing hievpy upload',
            'start_time': '2018-03-01 00:00:00',
            'end_time': '2018-03-01 23:59:59',
            'experiment_id': 31,
            'label_names': '"Neutron Probe","Soil Moisture"',
            'related_websites': '"https://www.westernsydney.edu.au/hie"',
            'contributor_names[]': ['Tom Smith, t.smith@google.com',
                                    'Jane White, J.White@aol.com',
                                    'Frank Blank, f.black@yahoo.com'],
            'type': 'PROCESSED'}

hp.upload(api_token, base_url, upload_file, metadata)
