# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def first_batsman(data=data):
    innings=data['innings']
    for i in innings:
        inning=i
        for n in inning:
            delivaries = inning[n]
            for d in delivaries:
                balls= delivaries[d]
                for b in balls:
                    first_ball= b
                    for bat in first_ball:
                        first_bats = first_ball[bat]
                        a = first_bats
                        break
                    break
                break
            break
        break

    return a['batsman']
name=first_batsman()
print name
