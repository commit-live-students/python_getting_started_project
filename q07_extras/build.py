# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here

    lst1=data['innings'][0]['1st innings']['deliveries']
    ext1 = []
    for inlst1 in lst1:
        for x,y in inlst1.items():
            for m,n in y.items():
                if (m == 'runs'):
                    for r,s in n.items():
                        if ((r == 'extras') and (s != 0)):
                            ext1.append(s)
                            break
    
    lst2=data['innings'][1]['2nd innings']['deliveries']
    ext2 = []                        
    for inlst2 in lst2:
        for x,y in inlst2.items():
            for m,n in y.items():
                if (m == 'runs'):
                    for r,s in n.items():
                        if ((r == 'extras') and (s != 0)):
                            ext2.append(s)
                            break
   
    difference = len(ext2)-len(ext1)

    return difference

extras_runs()
extras_runs()


