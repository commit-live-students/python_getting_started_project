# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data = data):
    y=list(data['info']['teams'])
    return y

#f_list=list(data.values(['info'] ['teams']))
#print(f_list)
#print (x)


teams()
   







