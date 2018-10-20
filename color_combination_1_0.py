import numpy as np

def combine_colors(color_map, target_depth, output_name = ''):
    #color_map = 'output_files/Humans_color_map-22.0-3.csv'
    #output_name = 'TEST'
    data = np.loadtxt(color_map, delimiter = ',', dtype=str)    # Loads the combination table
    r, c = data.shape
    color_dict = {
            'W':0,
            'U':1,
            'B':2,
            'R':3,
            'G':4,
            'C':5
            }
    
    output = np.full((r,6*6*6,6),-1)
    
    i=0
    
    for row in data:
        colors = []
        
        color_combination(row,target_depth,color_dict,colors)
        unique_colors = np.unique(colors,axis=0)
        output[i,0:len(unique_colors),:] = unique_colors
        
        i+=1
        #if i % 100 == 0:
        #    print(i)
        #    print(colors)
        del colors
    
    output_name = '{0}_color_combinations.npy'.format(output_name)
    
    np.save('output_files/{0}'.format(output_name),output)
    
    return output_name
    
    
def color_combination(row, num_cols, color_dict, color_combos, col=0, buffer=[0,0,0,0,0,0]):
    #print(color_combos)
    for color in row[col]:
        
        new_buffer = buffer.copy()
        new_buffer[color_dict[color]]+=1
        
        #print('Color: {0}, Column: {1}, Cell: {2}, Buffer: {3}'.format(color,col,row[col],new_buffer))
        
        if col == num_cols - 1: # -1 accounts for 0-indexing
            color_combos.append(new_buffer)
        else:
            color_combination(row, num_cols, color_dict, color_combos, col+1, new_buffer)
    
    return