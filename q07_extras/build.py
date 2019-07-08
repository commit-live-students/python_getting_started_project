# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    first_innings = []
    second_innings =[]
    list_1 = data['innings'][0]['1st innings']['deliveries']
    
    for x in list_1:
        for y in x:
            first_innings.append(x[y]['runs']['extras'])
            
                
    list_2 = data['innings'][1]['2nd innings']['deliveries']
    for i in list_2:
        for z in i:
            second_innings.append(i[z]['runs']['extras'])
            
            
    first_innings =[e for g, e in enumerate(first_innings) if e!=0]
    second_innings = [e for g, e in enumerate(second_innings)if e!=0]
        
    difference = abs(len(first_innings)- len(second_innings))


    return difference

extras_runs()





