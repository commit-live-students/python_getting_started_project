import yaml

def read_data():

    # import the csv file into `data` variable
    # You can use this path to access the CSV file: '../data/ipl_match.yaml'
    # Write your code here
    f = open('./data/ipl_match.yaml')
    data = yaml.load (f)

    # return data variable
    return data

if __name__ == "__main__":
    print read_data()
