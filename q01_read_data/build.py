import yaml


def read_data():
    path = './data/ipl_match.yaml'
    with open(path, mode='r') as stream:
        data = yaml.load(stream)

    return data
