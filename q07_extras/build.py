# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extra_score(dat1):
    extras_final = {'legbyes':0, 'wides':0,'byes':0}
            
    for i in list(range(len(dat1))):
        key1 = list(dat1[i].keys())[0]
        key_list = list(dat1[i][key1].keys())
        
        if 'extras' in key_list:
            temp = list(dat1[i][key1]['extras'].keys())[0] 
            extras_final[temp] = extras_final[temp]+1

    return sum(extras_final.values())

def extras_runs(data=data):
    
    # Creating extra function 
    
        
    # Write your code here
    dat1 = data['innings'][0]['1st innings']['deliveries']
    dat2 = data['innings'][1]['2nd innings']['deliveries']
    
    dat1_score = extra_score(dat1)
    dat2_score = extra_score(dat2)
    
    return dat2_score-dat1_score
  



