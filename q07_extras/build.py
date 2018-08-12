# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()
global count1
global count2
global flag
# Your Solution
def extras_runs(data=data):

    # Write your code here
    count1=0
    count2=0
    first_deliveries_data=data["innings"][0]["1st innings"]["deliveries"]
    second_deliveries_data=data["innings"][1]["2nd innings"]["deliveries"]
    for i in range(0, len(first_deliveries_data)):
            keys=first_deliveries_data[i].keys()
            flag=False
            #print i," ",keys[0]
            if ('extras' in first_deliveries_data[i][keys[0]]) and ('wides' in first_deliveries_data[i][keys[0]]["extras"]):
                flag=True
            elif ('extras' in first_deliveries_data[i][keys[0]]) and ('legbyes' in first_deliveries_data[i][keys[0]]["extras"]):
                flag=True
            else:
                flag=True

            if ('extras' in first_deliveries_data[i][keys[0]]) and flag:
                count1+=1

            flag=False

    for i in range(0, len(second_deliveries_data)):
            keys=second_deliveries_data[i].keys()
            flag=False
            #print i," ",keys[0]
            if ('extras' in second_deliveries_data[i][keys[0]]) and ('wides' in second_deliveries_data[i][keys[0]]["extras"]):
                flag=True
            elif ('extras' in second_deliveries_data[i][keys[0]]) and ('legbyes' in second_deliveries_data[i][keys[0]]["extras"]):
                flag=True
            else:
                flag=True

            if ('extras' in second_deliveries_data[i][keys[0]]) and flag:
                    count2+=1


            flag=False
    difference =count2-count1

    return difference
