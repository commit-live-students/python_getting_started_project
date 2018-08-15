# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    # Write your code here
    innings=data['innings']
    first=innings[0]
    second=innings[1]
    count=0
    count1=0
    first_inning_list=first['1st innings']['deliveries']
    second_inning_list=second['2nd innings']['deliveries']
    
    
    for x in first_inning_list:
        for key,value in x.items():
                 if 'extras' in value:
                    extras=value['extras']
                    for k,v in extras.items():
                        if(k=='legbyes' or k=='wides'):
                            count=count+v
    print(count)
    
    
    for y in second_inning_list:
        for key1,value1 in y.items():
            if 'extras' in value1:
                extras1=value1['extras']
                for k1,v1 in extras1.items():
                    count1=count1+v1
    print(count1)
    
    difference =count1-count
    return difference

extras_runs()


