
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
# Your Solution Here
def BC_runs (data=data):
    # Initialize the variable
    runs = 0
    runs_scored = 0
    # Read list value for deliveries
    deliveries_info = data['innings'][0]['1st innings']['deliveries']
    for ele in deliveries_info:
          # Read jey value pair
        for key, value in ele.items():
            batsman_name = value['batsman']
            runs_scored = value['runs']['batsman']
            #Check specific batsman
            if (batsman_name == 'BB McCullum'):
                runs += runs_scored
    return runs
data = read_data()
print (data['innings'][0]['1st innings']['deliveries'][0][0.1])
BC_runs(data)


