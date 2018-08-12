# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()


# Your Solution
def BC_runs(data):
    runs = 0
    for x in data['innings'][0]['1st innings']['deliveries']:
        for y,v in x.items():
            if v['batsman']== 'BB McCullum':
                for u, y in v.items():
                    if type(y) == dict:
                        if y.has_key('batsman'):
                            runs += y['batsman']
    return(runs)
# runs = 0
# for x in data['innings'][0]['1st innings']['deliveries']:
#     for y,v in x.items():
#             if v['batsman']== 'BB McCullum':
#
#                 for u, y in v.items():
#                     if type(y) == dict:
#                         # for a,b in y.items():
#                             if y.has_key('batsman'):
#                                 runs+=y['batsman']
#                             # runs += b
# print runs



            #  if i[1] == 'BB McCullum':
