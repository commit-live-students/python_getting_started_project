# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here
    all_innings = data['innings'] # all_innings is a list
    first_inninglist = all_innings[0] #getting 1st inning details from list # first_inninglist is a dictionary
    first_inning = first_inninglist['1st innings']
    delivery = first_inning['deliveries']
    match = delivery[0] # delivery is a list
    first_match = match[0.1]
    name = first_match['batsman']    #or name data['innings'][0]['1st innings']['deliveries'][0][0.1]['batsman']
    #print name
    #print type(name)

    return name
#first_batsman(data)
