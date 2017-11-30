# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):
    innf = data["innings"][0]["1st innings"]["deliveries"]
    inns = data["innings"][1]["2nd innings"]["deliveries"]
    extraf = 0
    extrasec = 0
    for i in range (0,len(innf)):
        delv = innf[i]
        if delv[delv.keys()[0]].get('extras',None) != None:
            extraf = extraf + 1
    for i in range (0,len(inns)):
        delv = inns[i]
        if delv[delv.keys()[0]].get('extras',None) != None:
            extrasec = extrasec + 1
    difference = extrasec - extraf
    return difference   
