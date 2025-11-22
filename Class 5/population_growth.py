''' 
    This script provides an example of how to consolidate multiple csv files into w DataFrame panel
    This is a pretty dynamic script for reading in data files, metadata, and looking up the corresponding year.
    
    data downloaded from https://data.census.gov/cedsci/table?q=Population%20Total&tid=PEPPOP2019.PEPANNRES
'''

import pandas as pd
import glob
import re

def get_year(path):
    pattern = re.compile('Y([0-9]{4})')
    year = re.search(pattern, path)
    if year:
        year = year[1]
    return year

def get_type(path):
    meta = re.search('metadata', path)
    if meta:
        return 'meta'
    else:
        return 'data'

def get_year_type(path):
    return get_year(path),get_type(path)

def fix_meta(df):
    df.columns = ['id', 'name']
    
    # expand the names into their own columns
    df = df[['id']].merge(df['name'].str.split('!!').apply(pd.Series), left_index = True, right_index = True)
    df.columns = ['id'] + ['level_{}'.format(x) for x in range(len(df.columns) - 1)]
    
    # keep only what I care about
    df = df.loc[df['level_0'].str.lower() == 'estimate']
    
    # set the corresponding index and drop id
    df.index = df['id']
    df = df.drop(columns = ['id'])
    
    return(df.reset_index())

def fix_data(df, year):
    # slice it based on the last observation
    df = df.iloc[-1]
    
    # create a multi-index level including the year. We need to create a list of tupples. 
    
    # option 1
    tuples = [(year, ind) for ind in df.index]
    
    # option 2
    tuples = list(zip(*[[year]*len(df), df.index]))
    index = pd.MultiIndex.from_tuples(tuples, names=["year", "name"])
    
    # assign the new index
    df.index = index
    
    # and just for clarity, let's name this
    df.name = 'data'
    
    return(df)

def fix_file(meta, *args):
    if meta == 'meta':
        return(fix_meta(*args))
    else:
        return(fix_data(*args))
    

path = '.\population_growth\*.csv'

# I want to create a dictionary that keeps the years as keys and the meta/data as elements
years = {}

# This takes care of the file reading; filtering only csv files
for file_path in glob.glob(path):
    # first, get the file type and the year
    year, meta = get_year_type(file_path)
    
    # This if is used to know if this is a first time allocation of the dict index, or if the index exists.
    if year in years.keys():
        # the key was allocated
        years[year][meta] = fix_file(meta, pd.read_csv(file_path))
    else:
        # the structure needs to be created
        years[year] = {meta: fix_file(meta, pd.read_csv(file_path), year)}

'''
    I want to make it so that the output of this script are 2 files: a data file and a meta file so that they can be used later
    I want to then consolidate all the metas and all the data files
'''

meta = pd.DataFrame()
data = pd.Series(index = pd.MultiIndex.from_tuples((), names=["year", "name"]), name = 'data')

for k, v in years.items():
    meta = pd.concat([meta, v['meta']])
    data = pd.concat([data, v['data']])

# final touches before exporting
meta = meta.drop_duplicates()
meta.index = meta.pop('id')
data = data.loc[:, meta.index]

meta.to_csv('.\data\metadata.csv')
data.to_csv('.\data\data.csv')