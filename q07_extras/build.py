# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    #for Ist innings
    
    list_of_extra_runs_in_1st_innings = []
    number_of_balls_played = len(data['innings'][0]['1st innings']['deliveries'])
    
    
    for ball_number in range(number_of_balls_played):
        
        di = data['innings'][0]['1st innings']['deliveries'][ball_number]
        
        for ke in di.keys():
            
            if 'extras' in data['innings'][0]['1st innings']['deliveries'][ball_number][ke]:
                list_of_extra_runs_in_1st_innings.append(data['innings'][0]['1st innings']['deliveries'][ball_number][ke]['extras'])
     
       
    # for 2nd innings
    
    list_of_extra_runs_in_2nd_innings = []
    number_of_balls_played = len(data['innings'][1]['2nd innings']['deliveries'])
    
    
    for ball_number in range(number_of_balls_played):
        
        di = data['innings'][1]['2nd innings']['deliveries'][ball_number]
        
        for ke in di.keys():
            
            if 'extras' in data['innings'][1]['2nd innings']['deliveries'][ball_number][ke]:
                list_of_extra_runs_in_2nd_innings.append(data['innings'][1]['2nd innings']['deliveries'][ball_number][ke]['extras'])
                
                        
                       
    
   
    difference = len(list_of_extra_runs_in_2nd_innings) - len (list_of_extra_runs_in_1st_innings)

    return difference

extras_runs()


