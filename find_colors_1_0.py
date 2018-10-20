import numpy as np

# match is W U B R G C

def find_colors(match,color_combinations):
    
    data = np.load(color_combinations);
    
    count = 0;
    
    for entry in data:
        for lands in entry:
            flgMatch = True
            for land, threshold in zip(lands, match):
                if land == -1:
                    flgMatch = False
                    break
                #print("Land: {0}, Threshold: {1}".format(land,threshold))
                if land < threshold:
                   # print("No Match!")
                    flgMatch = False
                    break
            if flgMatch == True:
                #print("Match!")
                count+=1
                break
    
    return count