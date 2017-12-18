# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    extra_1 = data['innings'][0]['1st innings']['deliveries']
    extra_2 = data['innings'][1]['2nd innings']['deliveries']
    ex1_count = 0
    ex2_count = 0


    for i in extra_1:
        sub_list1=i.values()
        if sub_list1[0]['runs']['extras'] > 0:
            ex1_count = ex1_count +  1
    for j in extra_2:
        sub_list2=j.values()
        if sub_list2[0]['runs']['extras'] > 0:
            ex2_count = ex2_count +  1
    difference = ex2_count - ex1_count
    return difference

difference = extras_runs(data)
