# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    runs=0
    for balls in data['innings'][0]['1st innings']['deliveries']:

        for key,values in balls.items():
            if values['batsman']=="BB McCullum":
                runs_count = values['runs']['batsman']
            #print (runs)
                runs = runs_count+runs
    return (runs)


    return(runs)
