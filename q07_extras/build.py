# %load q07_extras/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

from pprint import pprint
# Your Solution
def extras_runs(data=data):

    # Write your code here
    first_inn_run=0
    second_inn_run=0
    second_inning=data['innings'][1]['2nd innings']['deliveries']
    #print second_inning
    first_inning=data['innings'][0]['1st innings']['deliveries']
    #print first_inning



    for i in second_inning:
        for j in i.values():
            if(j['runs']['extras']!=0):
                second_inn_run+=1
        #print(second_inn_run)

    for i in first_inning:
        for j in i.values():
            if(j['runs']['extras']!=0):
                first_inn_run+=1

        #print(first_inn_run)


    difference =second_inn_run-first_inn_run


    return difference

extras_runs()
