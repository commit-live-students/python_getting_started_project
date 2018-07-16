# %load q03_first_batsman/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def first_batsman(data=data):
    # Write your code here
    innings=data['innings']
    print(innings)
    print(type(innings))
    print('----'*50)
    first=innings[0]
    print(first)
    print(type(first))
    print('----'*50)
    second=first['1st innings']['deliveries'] 
    print(second)
    third=second[0]
    print('----'*50)
    print(third)
    print(type(third))
    name=third[0.1]['batsman']
    print(name)
  
  
   
    #final=  deliveries[0.1]
    #name=final[batsman]
    return name

first_batsman()

