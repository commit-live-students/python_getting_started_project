import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from greyatomlib.python_getting_started.q01_read_data.build import read_data
from q07_extras.build import extras_runs

data = read_data()
extras = extras_runs(data)


class TestExtras_runs(TestCase):
    def test_extras_runs_return_type(self):
        self.assertIsInstance(extras, int, "Expected type does not match the return type")

    def test_extras_runs_return_values(self):
        self.assertEqual(extras, 6, "The Expected value does not match the return value")