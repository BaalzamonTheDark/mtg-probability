# =============================================================================
# Added enter_data as alternative to command line
# shortened lib names for easier updating 
# =============================================================================

import combination_table_1_2 as ct
import map_colors_1_1 as mc
import color_combination_1_0 as cc
import find_colors_1_0 as fc
import numpy as np

def color_probability(count_lands, target_depth, color_requirements, land_list = 'Lands.csv', name = '', out_file = 'out'):
    file_name, combinations = ct.make_combination_table(count_lands,target_depth)
    file_name = mc.map_colors('output_files/{0}'.format(file_name), land_list)
    file_name = cc.combine_colors('output_files/{0}'.format(file_name), target_depth)
    probability = fc.find_colors(color_requirements, 'output_files/{0}'.format(file_name))
    with open(out_file,'a') as f_:
        f_.write('{0},{1}\n'.format(name,probability/combinations))
    return probability/combinations

def enter_data():
    count_lands = int(input("Lands in Deck: "))
    target_depth = int(input("# of Lands per combination: "))
    cr_tmp = input("Colored Mana cost (Siege Rhino = WGB): ")
    land_list = input("Land List csv: ")
    name = input("Name of combination (for logging to outfile): ")
    out_file = input("Name of outfile: ")
    
    color_requirements = np.zeros((6))
    
    color_dict = {
            'W':0,
            'U':1,
            'B':2,
            'R':3,
            'G':4,
            'C':5
            }
    
    for color in cr_tmp:
        color_requirements[color_dict[color]] +=1
        
        
    
    print("% chance: ",color_probability(count_lands, target_depth, color_requirements, land_list, name, out_file))