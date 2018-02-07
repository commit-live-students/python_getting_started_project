# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def deliveries_count(data):
    list_1st_inn = data["innings"]

    dict_first_inn =  list_1st_inn[0]

    deliveries = dict_first_inn["1st innings"]["deliveries"]

    count = 0
    for keys in deliveries:
        a = keys.values()[0]
        if(a["batsman"] == "RT Ponting"):
            count = count + 1
    return count


print deliveries_count(data)
