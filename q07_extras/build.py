# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here




    one=0
    second=0


    for i in data["innings"][0]["1st innings"]["deliveries"]:

        for key in i:
            if i[key]["runs"]["extras"]>0:
                one+=1


    for i in data["innings"][1]["2nd innings"]["deliveries"]:

        for key in i:
            if i[key]["runs"]["extras"]>0:
                second+=1


    difference = second-one

    return difference
