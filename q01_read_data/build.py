import yaml
def read_data():
    with open('./data/ipl_match.yaml', 'r') as stream:
        data = yaml.load(stream)
        return data
        
        


