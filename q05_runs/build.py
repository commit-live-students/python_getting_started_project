# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def BC_runs(data):

    # Write your code here
    
    #Defining variable 'a'. This will store the content of 1st innings delivery wise
    a=data['innings'][0]['1st innings']['deliveries']
    
    #initialising variable runs = 0
    runs = 0
    
    #to check the type of next key/index. Accordingly use .key() or index to access the event drilling down in the .yaml file.
    print(type(a)) 
    
    #For dicts - To see next level keys while drilling down in the list.
    #print(a.keys())
    
    #For lists - To access next level index, values while drilling down in the list.
    #for i,v in enumerate(a):
    #    if i<=9:
    #        print(i,v)
    
    #Each delivery is stored in a separate index. So for loop to iterate thru the deliveries.
    for i,v in enumerate(a):
        for k,v in a[i].items():                     #To loop thru each delivery viz. 0.1, 0.2 etc in dicts.
            #print(a[i][k]['batsman'])               #Print batsman name for test purpose
            #print(a[i][k]['runs']['batsman'])       #Print runs scored by above batsman on each delivery.
            if a[i][k]['batsman'] == 'BB McCullum':  #Narrowing down on BB McCullum
                runs += a[i][k]['runs']['batsman']   #Storing runs scored by BB McCullum in runs variable.
    return(runs)

BC_runs(data)




