# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):

    batsman = 'BB McCullum'
    count = 0
    runs = 0
    for item in data['innings'][0]['1st innings']['deliveries']:
        for k,v in item.items():
            if item[k]['batsman'] == batsman:
                count = count +1
                runs = runs + item[k]['runs']['batsman']
    print count,runs


    return(runs)

BC_runs(data)
