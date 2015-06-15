import unittest
from demolib import demolib


class DemoLibtest(unittest.TestCase):

    def test_compute_demo(self):
        self.assertEqual(demolib.compute_demo(2), 84)
