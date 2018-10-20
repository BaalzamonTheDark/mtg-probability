# =============================================================================
# Changelog: Version 1.2 calculates combinations instead of permutations
# =============================================================================

import numpy as np
from itertools import islice
import collections
import math

def make_combination_table(ct_lands, target_depth, file_name = 'combination_table'):
    if file_name == 'combination_table':
        file_name = '{}-{}-{}.csv'.format(file_name,ct_lands,target_depth)
    print(file_name)
    print(int(math.factorial(ct_lands)/math.factorial(ct_lands-target_depth)/math.factorial(target_depth)))
    with open('output_files/{}'.format(file_name), 'bw') as f_handle:
        combination_table(ct_lands,target_depth,f_handle)
    return file_name, int(math.factorial(ct_lands)/math.factorial(ct_lands-target_depth)/math.factorial(target_depth))

def combination_table(ct_lands, target_depth, f_handle, buffer = np.array([None]), exclusions = np.empty(()), curr_depth = 0):
    
    # Target Depth must be 1-indexed!
    
    if buffer.all() == None: buffer = np.full((1,target_depth),-1)
    #if exclusions.all() == None: exclusions = np.full((target_depth),-1)
    
    numbers = iter(range(ct_lands))
    for i in numbers:
        # Prevents the same card being used twice
        while i in exclusions:
            consume(numbers,1)
            i += 1
            if i >= ct_lands: return
        exclusions = np.append(exclusions,i)
        # Updates buffer with the current card
        buffer[0, curr_depth] = i
        # Writes buffer if at max depth, else go deeper
        if curr_depth == target_depth-1:
            np.savetxt(f_handle,buffer,delimiter=',',fmt='%i')
        else:
            combination_table(ct_lands, target_depth, f_handle, buffer = buffer, exclusions = exclusions, curr_depth = curr_depth+1)
            

def consume(iterator, n):
    #print("Advance the iterator n-steps ahead. If n is none, consume entirely.")
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

