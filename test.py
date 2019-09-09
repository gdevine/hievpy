import hievpy as hp
import pandas as pd
import os


def get_data_columns(hiev_filename, data_column, start_date, end_date,
                     output_freq='30min', token=os.environ['HIEV_API_KEY']):
    # pull data from hiev
    df = hp.search_load_toa5df(
        api_token=token,
        base_url='https://hiev.uws.edu.au/',
        search_params={
            'filename': hiev_filename,
            'from_date': start_date,
            'to_date': end_date
        },
        biggish_data=True,
        keep_files=True,

    )
    # grab column and for to output frequency
    selection = df[data_column].resample(output_freq).mean()
    return selection




import pandas as pd
import matplotlib.pyplot as plt
import hievpy as hp
import os


token=os.environ['HIEV_API_KEY']
base_url='https://hiev.uws.edu.au/'

lat_cup = -33.615174
lon_cup = 150.72366
lat_tern = -33.615271
lon_tern = 150.722488
lat_mofo = -33.614154
lon_mofo = 150.726238


def build_df(months_back=6, output_freq='30min'):
    # generate start and end date
    start_date = (
        pd.to_datetime('today') -
        pd.Timedelta(value=months_back, unit='M')
    ).strftime('%Y-%m-%d')
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')
    # build index and empty dataframe
    idx = pd.date_range(
        start=start_date,
        end=end_date,
        freq='30min'
    )
    data = pd.DataFrame(index=idx)
    # add data
    data[[
        'CUP_08cm_1',
        'CUP_08cm_2',
        'CUP_30cm_1',
        'CUP_30cm_2'
    ]] = get_data_columns(
        hiev_filename='CUP_AUTO_soil',
        data_column=[
            'VW_01_Avg',
            'VW_02_Avg',
            'VW_03_Avg',
            'VW_04_Avg'
        ],
        start_date=start_date,
        end_date=end_date,
        output_freq=output_freq
    )
    data[['MOFO_10cm_1',
          'MOFO_10cm_2',
          'MOFO_0-20cm_1',
          'MOFO_0-20cm_2',
          'MOFO_30-60cm_1',
          'MOFO_30-60cm_2'
        ]]= get_data_columns(
            hiev_filename='CUP_AUTO_MEL_SOILVARS',
            data_column=[
                'Theta_Avg(1)',
                'Theta_Avg(2)',
                'VW_Avg(1)',
                'VW_Avg(4)',
                'VW_Avg(2)',
                'VW_Avg(3)'
            ],
            start_date=start_date,
            end_date=end_date,
            output_freq=output_freq
    )

    for ring in range(6):
        data[[
            f'FACE_R{ring+1}_5cm_1',
            f'FACE_R{ring+1}_5cm_2',
            f'FACE_R{ring+1}_30cm_1',
            f'FACE_R{ring+1}_30cm_2',
            f'FACE_R{ring+1}_75cm_1',
            f'FACE_R{ring+1}_75cm_2',
            f'FACE_R{ring+1}_0-30cm_1',
            f'FACE_R{ring+1}_0-30cm_2',
            f'FACE_R{ring+1}_0-30cm_3',
            f'FACE_R{ring+1}_0-30cm_4',
            f'FACE_R{ring+1}_0-30cm_5',
            f'FACE_R{ring+1}_0-30cm_6',
            f'FACE_R{ring+1}_0-30cm_7',
            f'FACE_R{ring+1}_0-30cm_8'
        ]] = get_data_columns(
            hiev_filename=f'FACE_R{ring+1}_B1_SoilVars',
            data_column=[
                'Theta5_1_Avg',
                'Theta5_2_Avg',
                'Theta30_1_Avg',
                'Theta30_2_Avg',
                'Theta75_1_Avg',
                'Theta75_2_Avg',
                'VWC_1_Avg',
                'VWC_2_Avg',
                'VWC_3_Avg',
                'VWC_4_Avg',
                'VWC_5_Avg',
                'VWC_6_Avg',
                'VWC_7_Avg',
                'VWC_8_Avg'
            ],
            start_date=start_date,
            end_date=end_date,
            output_freq=output_freq
        )

    return data


df = build_df()
df.filter(like='0-30cm_1').plot(figsize=(20,10))
plt.show()
