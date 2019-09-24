# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):

    # Write your code here
    # get the first innings
    first_ings_lst = data["innings"][0]
    first_ings_overs_lst = first_ings_lst["1st innings"]["deliveries"]
    # get the batsman who faced the delivery 0.1
    name = first_ings_overs_lst[0][0.1]["batsman"]


    return name
