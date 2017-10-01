import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q05_runs.build import BC_runs

class TestBC_runs(TestCase):
    def test_BC_runs(self):
        data= read_data()
        McCullum_runs = BC_runs(data)
        self.assertIsInstance(McCullum_runs, int)
        self.assertTrue(158 == McCullum_runs)
