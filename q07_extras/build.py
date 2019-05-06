# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_inn=list()
    sec_inn=list()
    lst1=data['innings'][0]['1st innings']['deliveries']
    for i,e in enumerate(lst1):
        for k in lst1[i].keys():
            if 'extras' in lst1[i][k].keys():
                first_inn.append(lst1[i][k]['extras'])
          
    lst2=data['innings'][1]['2nd innings']['deliveries']
    for i,e in enumerate(lst2):
        for k in lst2[i].keys():
            if 'extras' in lst2[i][k].keys():
                sec_inn.append(lst2[i][k]['extras'])

    difference=len(sec_inn)-len(first_inn)
                
    return difference



