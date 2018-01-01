# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def extras_runs(data=data):

    # Write your code here
    firstinnings = data["innings"][0]["1st innings"]["deliveries"]
    secondinnings = data["innings"][1]["2nd innings"]["deliveries"]

    extrafirst = 0
    extrasecond = 0

    for extraruns in firstinnings:
        for delivery,info in extraruns.items():
            if info["runs"]["extras"] > 0:
                extrafirst = extrafirst + 1

    for extraruns in secondinnings:
        for delivery,info in extraruns.items():
            if info["runs"]["extras"] > 0:
                extrasecond = extrasecond + 1

    difference = abs(extrasecond - extrafirst)


    return difference
