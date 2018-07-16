# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here


    deliveries_list=data["innings"][0]["1st innings"]["deliveries"]
    firstInningRuns=0
    for target_list in deliveries_list:
     for overs in target_list:
        if target_list[overs]["runs"]["extras"]!=0:
                firstInningRuns=firstInningRuns+1
    print(firstInningRuns)
    deliveries_list2=data["innings"][1]["2nd innings"]["deliveries"]
    secondInningsRuns=0
    for target_list in deliveries_list2:
     for overs in target_list:
        if target_list[overs]["runs"]["extras"]!=0:
                secondInningsRuns=secondInningsRuns+1
    print(secondInningsRuns)
    run=secondInningsRuns-firstInningRuns
    return run
