import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q05_runs.build import BC_runs
data= read_data()
McCullum_runs = BC_runs(data)


class TestBC_runs(TestCase):
    def test_BC_runs_return_type(self):
        self.assertIsInstance(McCullum_runs, int, "The Expected type does not match the return type")

    def test_BC_runs_return_values(self):
        self.assertEqual(158, McCullum_runs, "The Expected value does not match the return value")