from concordance import *
from collections import Counter
import sys

f1 = sys.argv[1]
f2 = sys.argv[2]

def file_concord(file_name):
    fn = file_name
    test1 = concordance(fn, unique = False)
    for key in test1:
        test1[key].append(fn)
    
    return test1
    

def concord_final(f1, f2):
    dict_final = {}
    for key in f1:
        if key in f2:
            dict_final[key] = f1[key],f2[key]
            del f2[key]
            
        else:
            dict_final[key] = f1[key]
            
    dict_final.update(f2)
    return dict_final
    


def linenumbercombined(dictonary):
    a = dictonary
    final_string = ""
    for k,v in dictonary.items():
        if v == 1:
            if final_string == "":
                final_string = final_string + str(k)
            else:
                final_string = final_string +  ", " + str(k)
        
        else:
            if final_string == "":
            
                final_string = final_string + str(k) + "(" + str(v) + ")" 
            else:
                final_string = final_string + ", " +  str(k) + "(" + str(v) + ")" 
    return final_string

def concord(file1, file2):
    
    file1_concord = file_concord(file1)
    file2_concord = file_concord(file2)
    
    m = concord_final(file1_concord, file2_concord)
    z = dict(sorted(m.items()))
    
    for k,v in z.items():
        print(k, "(",(len(v[0]) - 1) + (len(v[1]) - 1), ") :")
        a = linenumbercombined(dict(Counter(v[0][:-1] )) ) 
        b = linenumbercombined(dict(Counter(v[1][:-1] )) ) 
        print("   ", v[0][-1],": ", a )
        print("   ", v[1][-1],": ", b)


if __name__ == "__main__":
    concord(f1, f2)
