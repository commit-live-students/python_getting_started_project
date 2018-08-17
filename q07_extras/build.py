# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
# Your Solution
def extras_runs(data=data):
    ext1=[]
    ext2=[]
    del_1stInnings = data['innings'][0]['1st innings']['deliveries']
    del_2ndInnings = data['innings'][1]['2nd innings']['deliveries']
    # Write your code here
    for x in del_1stInnings:
        for y in x:
            ext1.append(x[y]['runs']['extras'])
    for a in del_2ndInnings:
        for b in a:
            ext2.append(a[b]['runs']['extras'])
            
    length_ext1=0
    length_ext2=0
    
    for i in ext1:
        if i>0:
            length_ext1+=1
    
    for i in ext2:
        if i>0:
            length_ext2+=1
            
    difference = length_ext2-length_ext1


    return difference




