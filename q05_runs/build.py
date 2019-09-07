# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    deliveries = data['innings'][0]['1st innings']['deliveries']
    runs = sum([v["runs"]["batsman"] for d in deliveries for k,v in d.items() if v["batsman"] == "BB McCullum" ])
    return(runs)
