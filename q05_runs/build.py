# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


def BC_runs(data):

    list_1st_inn = data["innings"]
    #print list_1st_inn
    dict_first_inn =  list_1st_inn[0]
    #print dict_first_inn
    deliveries = dict_first_inn["1st innings"]["deliveries"]
    #print deliveries
    runs1 = 0
    runs = 0
    for keys in deliveries:
            for ele in keys.values():
                #print ele
                if(ele["batsman"] == "BB McCullum"):
                    runs1 = int(ele["runs"]["batsman"])
                    runs = runs + runs1
    return runs

print BC_runs(data)
