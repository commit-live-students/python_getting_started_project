from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

def teams(data=data):
    team_names = data['info']['teams']
    return team_names
    print(team_names)
