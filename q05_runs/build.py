# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def BC_runs(data):
    runs=0
    
    innings=data['innings']
    first=innings[0]
    final_inning_list=first['1st innings']['deliveries']
    for x in final_inning_list:
        for key,value in x.items():
            if(value['batsman'] == 'BB McCullum'):
                runs += value['runs']['batsman']
    return runs
                
                
              
        


BC_runs(data)

                    


