import yaml

def read_data():
    with open('./data/ipl_match.yaml') as info:
        data = yaml.load(info)


    # return data variable
    return data
