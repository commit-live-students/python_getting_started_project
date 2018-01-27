# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_innings = [] #list for storing extra runs of 1st innings
    second_innings = []#list for storing extra runs of 2nd innings
    sum1 = 0 #addition of all extra runs in 1st innings
    sum2 = 0 #addition of all extra runs in 2nd innings
    difference = 0 #difference of extra runs between 1st and 2nd innings
    deliv1 = data['innings'][0]['1st innings']['deliveries']#1st innings
    deliv2 = data['innings'][1]['2nd innings']['deliveries']#2nd innings

    #for getting extras in 1st innings and store in fst list
    for b in  deliv1:
        for k in b:
            if b[k]['runs']['extras'] != 0 :
                first_innings.append(b[k]['runs']['extras'])


    #for getting extras in 1st innings and store in scnd list
    for b in deliv2:
        for k in b:
            if b[k]['runs']['extras'] !=0 :
                second_innings.append(b[k]['runs']['extras'])





    difference = abs(len(first_innings) - len(second_innings))


    return difference
