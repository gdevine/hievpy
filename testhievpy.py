import os
import hievpy


# Set the base URL of the HIEv instance being called against
# base_url = 'https://hiev.westernsydney.edu.au/'
# Set API/Auth token for all calls to the HIEvPy library
api_token = os.environ['HIEV_API_KEY']


# xx = hievpy.search_download(api_token, experiments=['82'], upload_from_date="2018-05-01")
df = hievpy.search_load_toa5df(api_token, filename="DRL_AUTO_450LO_SOIL_R", from_date="2017-01-02", to_date="2018-01-08")

print('bla')
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
hievpy.plot_toa5df_var(api_token, df, 'VW_Avg(1)')
#
#
# print('complete')
