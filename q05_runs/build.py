# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    
    count = 0
    key_list=[]
    abc=[]
    
    for i in range(0,124,1):
        abc=[]
        abc =list(data['innings'][0]['1st innings']['deliveries'][i].keys())
        key_list.append(abc[0])
        
    runs = 0
    for i in range(0,124,1):
        if(str(data['innings'][0]['1st innings']['deliveries'][i][key_list[i]]['batsman'])=='BB McCullum'):
            runs+= data['innings'][0]['1st innings']['deliveries'][i][key_list[i]]['runs']['batsman']       
    


    return(runs)


