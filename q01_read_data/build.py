



import yaml
def read_data(filepath='data/ipl_match.yaml'):
        data=yaml.load(open(filepath))
        return data
read_data()



