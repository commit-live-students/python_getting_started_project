import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q04_count.build import deliveries_count

class TestDeliveries_count(TestCase):
    def test_deliveries_count(self):
        data = read_data()
        nos_of_delivery = deliveries_count(data)
        self.assertIsInstance(nos_of_delivery, int)
        self.assertTrue(20 == nos_of_delivery)
