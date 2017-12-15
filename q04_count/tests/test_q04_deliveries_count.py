import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q04_count.build import deliveries_count

data = read_data()
nos_of_delivery = deliveries_count(data)

class TestDeliveries_count(TestCase):
    def test_deliveries_count_return_type(self):
       
        self.assertIsInstance(nos_of_delivery, int)
    def test_deliveries_count_return_values(self):
        self.assertEqual(20 , nos_of_delivery,"The Expected value does not match the return value")
