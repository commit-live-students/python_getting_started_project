# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data1 = read_data()

def extras_runs(data):
    def extras_runs_1(data):
        lst = data['innings'][0]['1st innings']['deliveries']

        ext = 0
        for d in lst:
            extra_runs = d.values()
            if 'extras' in extra_runs[0]:
                for k in extra_runs[0]['extras']:
                    ext += 1
        return ext

    def extras_runs_2(data):
        lst = data['innings'][1]['2nd innings']['deliveries']

        ext = 0
        for d in lst:
            extra_runs = d.values()
            if 'extras' in extra_runs[0]:
                for k in extra_runs[0]['extras']:
                    ext += 1
        return ext

    one = extras_runs_1(data)
    two = extras_runs_2(data)

    if one > two:
        difference = one - two
    else: difference = two - one

    return difference

extras_runs(data1)
