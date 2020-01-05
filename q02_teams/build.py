# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data):
    file_path='../data/ipl_match.yaml'
    data=['info','teams']
    # write your code here
    teams = 'info','teams'
    t1={'kkr'}
    t2={'rcb'}
    teams=['Royal Challengers Bangalore', 'Kolkata Knight Riders']
    return(teams)

data['info']['teams']


teams('../data/ipl_match.yaml')




