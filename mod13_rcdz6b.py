import unittest
import datetime

class TestUnites(unittest.TestCase):

    def setUp(self):
        self.symbol = "GOOGL"
        self.chartType = "1"
        self.timeSeries = "3"
        self.startDate = "2020-10-10"
        self.endDate = "2022-10-10"
        self.dateFormat = "%Y-%m-%d"

    def test_symbol(self):
        self.assertTrue(self.symbol.isalpha)
        self.assertIn(len(self.symbol),range(1,8))

    def test_chartType(self):
        self.assertTrue(self.chartType.isnumeric)
        self.assertTrue(len(self.chartType) == 1)
        self.assertIn(int(self.chartType),range(1,3))

    def test_timeSeries(self):
        self.assertTrue(self.timeSeries.isnumeric)
        self.assertTrue(len(self.timeSeries) == 1)
        self.assertIn(int(self.chartType),range(1,5))

    def test_startDate(self):
        self.assertTrue(bool(datetime.datetime.strptime(self.startDate, self.dateFormat)))

    def test_endDate(self):
        self.assertTrue(bool(datetime.datetime.strptime(self.endDate, self.dateFormat)))





if __name__ == '__main__':
    unittest.main()