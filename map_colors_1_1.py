# =============================================================================
# Takes the output from combination_table.py and maps the colors to it
# Fixes bug with turn 1 from v1.0
# =============================================================================

import numpy as np
import pandas as pd

def map_colors(combination_table, land_list = 'lands.csv', map_name = ''):        
    data = np.loadtxt(combination_table,delimiter = ',')    # Loads the combination table
    land_list = pd.read_csv('Lands.csv')
    
    rows, cols = land_list.shape
    
    mapping = np.zeros((rows,2))    # Creates an empty array to store the mapping table (this takes the land list and converts it to a usable format)
    
    for i in range(rows):
        if i > 0: mapping[i,0] = mapping[i-1,1]
        mapping[i,1] = mapping[i,0] + land_list['Quantity'][i]
        
    land_list['Start'] = mapping[:,0]
    land_list['End'] = mapping[:,1]
    
    color_data = np.full(data.shape,"",dtype='U6')
    
    # Applies the mapping table as a serise of filters
    
    for i in range(rows):
        color = data >= land_list['Start'][i]# and data >= land_list['Start'][i]
        color_data[color] = land_list['Colors'][i]
    
    # Saves the color map
    
    t = data.shape
    r = t[0]
    c = 1
    if len(t) is 2:
        c = t[1]
    
    map_name = '{0}_color_map-{1}-{2}.csv'.format(map_name,int(data[r-1,0]+1),c)
    
    with open('output_files/{0}'.format(map_name), 'wb') as f_handle:
        np.savetxt(f_handle,color_data,delimiter=',',fmt='%s')
    
    return map_name
