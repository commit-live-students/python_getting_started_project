# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    first_inning_extras = 0
    second_inning_extras = 0
    first_inning_overs = data["innings"][0]["1st innings"]["deliveries"]
    second_inning_overs = data["innings"][1]["2nd innings"]["deliveries"]

    for balls in first_inning_overs:
        for ball in balls:
            #print ball
            if balls[ball]['runs']['extras']!=0:
                first_inning_extras = first_inning_extras + 1



    for balls in second_inning_overs:
        for ball in balls:
            #print ball
            if balls[ball]['runs']['extras']!=0:
                second_inning_extras = second_inning_extras + 1


    difference = second_inning_extras - first_inning_extras

    return difference
