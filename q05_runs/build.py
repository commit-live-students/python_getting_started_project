# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    run = 0
    count = 0
    for i in range (len(data['innings'][0]['1st innings']['deliveries'])):
        a = data['innings'][0]['1st innings']['deliveries'][i].values()
        if (a[0]['batsman']) == "BB McCullum":
            run = a[0]['runs']['batsman']
            count = count+run
            #print count
        print count


    return(runs)
