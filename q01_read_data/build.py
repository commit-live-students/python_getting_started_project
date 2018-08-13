import yaml

def read_data():

    with open("./data/ipl_match.yaml","r") as f :
            data = yaml.load(f)
    # return data variable
            return data

print read_data()
