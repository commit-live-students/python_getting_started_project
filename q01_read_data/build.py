import yaml


def read_data():

    ipl_data_path = './data/ipl_match.yaml'
    try:
        my_file = open(ipl_data_path,mode='r')
        # import the csv file into `data` variable
        # You can use this path to access the CSV file: '../data/ipl_match.yaml'
        # Write your code here
    except FileNotFoundError:
        # raise file not found error if it is not found in path
        print "File path {} is not correct".format(ipl_data_path)
        raise FileNotFoundError
    else:
        data = yaml.safe_load(my_file)
        print type(data)
        # close the file
        my_file.close()
        # return data variable
        return data
