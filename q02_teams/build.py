# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def array_reshaped_zeros():

    def array_zeros():

        zero_arrays=np.zeros((3,4,2))

        return zero_arrays

        zeros_array_reshaped = array_zeros().reshape((2,3,4))

        return zeros_array_reshaped
