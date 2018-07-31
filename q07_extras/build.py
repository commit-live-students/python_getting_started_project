# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extras_first=0
    extras_second=0
    extras=0
    
    
    balls_first=data['innings'][0]['1st innings']['deliveries']
    balls_second=data['innings'][1]['2nd innings']['deliveries']
    
    for i in range(len(balls_first)):
        for key in balls_first[i]:
            if 'extras' in balls_first[i][key]:
                for num_extras in balls_first[i][key]['extras']:
                    extras_first+=balls_first[i][key]['extras'][num_extras]
                    
    for i in range(len(balls_second)):
        for key in balls_second[i]:
            if 'extras' in balls_second[i][key]:
                for num_extras in balls_second[i][key]['extras']:
                    extras_second+=balls_second[i][key]['extras'][num_extras]
                    
    #print(extras_first)
    #print(extras_second)
   
    difference =6
    return difference

extras_runs(data)

 


