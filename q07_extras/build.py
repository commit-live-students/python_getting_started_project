# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    
    a = data['innings'][0]['1st innings']['deliveries']
    b = data['innings'][1]['2nd innings']['deliveries']
   
    extra_1st_inn = []
    extra_2nd_inn = []

    #For 1st innings
    for i,v in enumerate(a):      #Tracking delivery by delivery elemnt of list viz. [0],[1],[2] etc.
        for k,v in a[i].items():    #Going inside each delivery viz. 0.1, 0.2 etc.
            if 'extras' in a[i][k].keys():  #if there's an 'extra' key in the delivery go inside it and get its value.
                for key,val in a[i][k]['extras'].items():
                    print(a[i][k]['extras'][key])
                    extra_1st_inn.append(a[i][k]['extras'][key])

    #For second innings (logic same as 1st innings)
    for i,v in enumerate(b):
        for k,v in b[i].items():
            if 'extras' in b[i][k].keys():
                for key,val in b[i][k]['extras'].items():
                    print(b[i][k]['extras'][key])
                    extra_2nd_inn.append(b[i][k]['extras'][key])

    difference = len(extra_2nd_inn) - len(extra_1st_inn)
    
    return difference



