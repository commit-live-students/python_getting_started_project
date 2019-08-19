# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data=data):

    # Write your code here
   dc = data['innings'][0]['1st innings']['deliveries']

   runs = 0

   for i in range(0,len(dc)):
      for x in dc[i].values():
        if dc[i].values()[0]['batsman'] == "BB McCullum":
            runs = runs + dc[i].values()[0]['runs']['batsman']

   return runs
