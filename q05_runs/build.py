# %load q05_runs/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
  runs=0
    # Write your code here
  for d in data['innings'][0]['1st innings']['deliveries']:
        for ball in d.keys():
            if(d[ball]['batsman'] == 'BB McCullum'):
                runs += d[ball]['runs']['batsman']
  return(runs)
runs = BC_runs(data)
print(BC_runs(data))



