from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
def teams(data=data):
    ipl_teams=data['info']['teams' ]
    return ipl_teams
