import os
import hievpy

# Set API/Auth token for all calls to the HIEvPy library
api_token = os.environ['HIEV_API_KEY']


# 1. Search API test
#-------------------------------------------------------
results = hievpy.search(api_token, experiments=['82'], upload_from_date="2018-05-01")


# 2. Download file(s) locally
#-------------------------------------------------------
for result in results:
    hievpy.download(api_token, result)


# 3. Load a TOA5 file into a pandas dataframe
#-------------------------------------------------------
df = hievpy.toa5_to_df(api_token, results[0])



# df = hievpy.toa5_info(os.environ['HIEV_API_KEY'], myfile[0])
#
# df.reset_index()
#
# # x = df['TIMESTAMP']
# y1 = df['RH_Avg']
#
# plt.style.use('presentation')
# plt.plot(y1,use_index=True)
#
print('bla')

# hp.reg_lin(x=df['VW_Avg(1)'], y=df['VW_Avg(2)'])

