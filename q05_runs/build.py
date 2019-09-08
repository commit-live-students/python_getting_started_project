# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    first_inning = data['innings'][0]['1st innings']['deliveries']
    runs = 0
    for balls in first_inning:
        for ball in balls:
            valid_balls = balls[ball]
            if valid_balls['batsman'] == 'BB McCullum':
                runs_per_delivery = valid_balls['runs']
                run = runs_per_delivery['batsman']
                runs = runs + run

    return(runs)

print(BC_runs(data))
