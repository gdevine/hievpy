import os
import hievpy


# Set the base URL of the HIEv instance being called against
# base_url = 'https://hiev.westernsydney.edu.au/'
# Set API/Auth token for all calls to the HIEvPy library
api_token = os.environ['HIEV_API_KEY']


# xx = hievpy.search_download(api_token, experiments=['82'], upload_from_date="2018-05-01")
# df = hievpy.search_load_toa5df(api_token, filename="DRL_AUTO_450LO_SOIL_R", from_date="2017-01-02", to_date="2018-01-08")

#
# # 1. Search API test
# # -------------------------------------------------------
# results = hievpy.search(api_token, experiments=['82'], upload_from_date="2018-05-01")
#
#
# # 2. Download file(s) locally
# #-------------------------------------------------------
# for result in results:
#     hievpy.download(api_token, result)
#
#
# # 4. Print summary information about a TOA5 file
# # -------------------------------------------------------
# hievpy.toa5_summary(api_token, results[1])
#
#
# # 5. Load a TOA5 file into a pandas dataframe
# # -------------------------------------------------------
# df = hievpy.toa5_to_df(api_token, results[1])
#
#
# # 6. Generate a simple plot of a single variable from a HIEv TOA5 file
# # -------------------------------------------------------
# hievpy.plot_toa5df_var(df, 'VW_Avg(1)')
#
#

## Set path of file to be uploaded
#upload_file = '/Users/gerarddevine/dev/python/hiev/hievpy/DanData.txt'
#
## -------------------------------------------------------------------------
## Set metadata variables for upload
#metadata = {"experiment_id":77,
#            "type":"RAW",
#            "description":"This is a dummy description for file upload testing",
#            "creator_email":"g.devine@westernsydney.edu.au",
#            "contributor_names":['Tom Smith, t.smith@google.com', 'Jane White, J.White@aol.com', 'Frank Blank, f.black@yahoo.com'],
#            "label_names":'"Rainfall","Environment","TOA5"',
#            "grant_numbers": '"ZXY7654","PRQ53422"',
#            "related_websites":'"http://www.bom.org.au","http://www.westernsydney.edu.au"',
#            "start_time":'2014-01-01 12:11:10',
#            "end_time":'2014-12-30 14:09:08'
#            }
## -------------------------------------------------------------------------
#
#hievpy.upload(api_token, upload_file, metadata)
#print('complete')

#df = hievpy.search_download(api_token=api_token, filename='EddyFlux_slow_rad_2018')


# -------------------------------------------------------------------------
## Set metadata variables for upload
#updates = {
#           # "experiment_id":77,
#           # "type":"RAW",
#           "description":"PAR data from understorey sensors at the TERN site.",
#           # "creator_email":"g.devine@westernsydney.edu.au",
#           # "contributor_names":['Tom Smith, t.smith@google.com', 'Jane White, J.White@aol.com', 'Frank Blank, f.black@yahoo.com'],
#           # "label_names":'"Rainfall","Environment","TOA5"',
#           # "grant_numbers": '"ZXY7654","PRQ53422"',
#           # "related_websites":'"http://www.bom.org.au","http://www.westernsydney.edu.au"',
#           # "start_time":'2014-01-01 12:11:10',
#           # "end_time":'2014-12-30 14:09:08'
#           }
## -------------------------------------------------------------------------
#
#results = hievpy.search(api_token, filename='TERNHECT_UNDERPAR', from_date='2018-01-25')
#
#hievpy.update(api_token, results, updates)
