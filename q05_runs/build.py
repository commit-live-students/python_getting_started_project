# %load q05_runs/build.py
# Default Imports
#om greyatomlib.python_getting_started.q01_read_data.build import read_data
#ata = read_data()
#rint(data)
# Your Solution
#def BC_runs(data):

    # Write your code here


    #return(runs)
import yaml
def BC_runs(data):
    
    data=open('./data/ipl_match.yaml','r')
    data1=yaml.load(data)
    data2=data1['innings'][0]['1st innings']['deliveries']
    runs=0
    for key,value in enumerate(data2):
        for k,v in value.items():
            if v['batsman']=='BB McCullum':
                runs+=(v['runs']['batsman'])
            
            
      
    return runs


