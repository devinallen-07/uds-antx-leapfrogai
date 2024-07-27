from typing import Any
import pandas as pd


def wrangle_initial_df(data_path: str, 
                       group_column: str='start', 
                       fill_state: bool=True
                       ) -> pd.DataFrame:
    '''
    Wrangles data into initial DF. Defaults to using the 
    "start" column as the grouping key. Fill_state option
    will by default fill foward all of the blank states with 
    the previous state. 
    '''
    df = pd.read_csv(data_path)
    
    #drop track2 which is blank
    df.drop('track2', axis=1, inplace=True)
    
    #replace NaNs with empty string value
    if fill_state:
        df['state'] = df['state'].ffill()
    df.fillna(value='', inplace=True)

    #create minute column for grouping data
    df['minute'] = pd.to_datetime(df[group_column]).dt.time
    df['minute'] = df['minute'].apply(lambda x: x.strftime('%H:%M'))
                       
    #remove uneeded columns
    df.drop(['start', 'end'], axis=1, inplace=True)
    return df
                       

def _fill_entry(grouped_minute: dict, row: list[Any]):
    '''
    Fills a grouped minute dictionary with data from 
    a data row.
    '''
    for i, key in enumerate(grouped_minute):
        grouped_minute[key].append(row[i])

def group_data_by_minute(df: pd.DataFrame, 
                         merge_tracks: bool=False
                        ) -> dict:
    '''
    Given a DF from the wrangle_initial_df fx, groups
    data by minute.  Merge tracks option allows all 
    text from each track to be joined as a single string.
    '''
    grouped_data = {}
    list_of_data = df.values.tolist()
    for row in list_of_data:
        time = row[-1]
        if time not in grouped_data:
            grouped_data[time] = {column:[] for column in df.columns[:-1]}
            _fill_entry(grouped_data[time], row)
        else:
            _fill_entry(grouped_data[time], row)
    if merge_tracks:
        for time in grouped_data:
            for num in [1,3,4]:
                grouped_data[time][f'track{num}'] = ' '.join([s for s in grouped_data[time][f'track{num}'] if s])
    return grouped_data

def df_pipe(data_path: str, 
            group_column: str='start', 
            fill_state: bool=True, 
            merge_tracks: bool=False
            ) -> dict:
    '''
    Primary entrypoint for data grouping by minute.
    '''
    df = wrangle_initial_df(data_path, group_column, fill_state)
    grouped_data = group_data_by_minute(df, merge_tracks)
    return grouped_data