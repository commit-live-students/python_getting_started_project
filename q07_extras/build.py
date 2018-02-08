# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def extras_runs(data):

    list_1st_inn = data["innings"]
    #print list_1st_inn
    deliveries_first =  list_1st_inn[0]["1st innings"]["deliveries"]
    #print deliveries_first

    deliveries_second =  list_1st_inn[1]["2nd innings"]["deliveries"]
    #print deliveries_second


    def first():
        count_first = 0
        for keys in deliveries_first:
            for ele in keys.values():
                counts = ele["runs"]["extras"]
                count_first = count_first + counts

        return count_first

    def second():
        count_sec = 0
        for keys in deliveries_second:
            for ele in keys.values():
                counts = ele["runs"]["extras"]
                count_sec = count_sec + counts

        return count_sec

    #print first()
    #print second()
    difference = first() - second()
    return difference


print extras_runs(data)
