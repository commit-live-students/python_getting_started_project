# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data):
    teams=[]
    #getting atch data information from yml data output
    match_data_info = data['info']
    #getting team information played first match
    teams = match_data_info['teams']
    #returning team
    return teams

teams(data)


