import numpy as np
import unittest
from data import read_tdx
from day import norm_days, norm_day, get_high, get_low, get_open, get_close
from day import set_high, set_low, set_open, set_close

class DayTest(unittest.TestCase):
    def test_get_set_rows(self):
        data, dates = read_tdx('testdata/testdata_1.txt')
        row = data[0,:]
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], row.tolist()) 
        self.assertEqual(20.00, get_open(row))
        self.assertEqual(30.00, get_close(row))
        self.assertEqual(40.00, get_high(row))
        self.assertEqual(10.00, get_low(row))

        set_open(row, 100)
        set_close(row, 200)
        set_high(row, 300)
        set_low(row, 400)
        self.assertEqual(100.00, get_open(row))
        self.assertEqual(200.00, get_close(row))
        self.assertEqual(300.00, get_high(row))
        self.assertEqual(400.00, get_low(row))

    def test_norm_day(self):
        data, dates = read_tdx('testdata/testdata_1.txt')
        row = data[0,:]
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], row.tolist()) 

        row1 = norm_day(row)
        # make sure the row is not changed.
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], row.tolist()) 
        self.assertEqual([2.00,4.00,1.00,3.00,1214862,14319652.00], row1.tolist()) 

    def test_norm_days(self):
        data, dates = read_tdx('testdata/testdata_1.txt')
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[0,:].tolist()) 
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[1,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[2,:].tolist())

        days = data[0:3,:]

        normed_days = norm_days(days)
        # make sure that "days" is not changed.
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], days[0,:].tolist()) 
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], days[1,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], days[2,:].tolist())

        self.assertEqual([2.00,4.00,1.00,3.00,1214862,14319652.00], normed_days[0,:].tolist()) 
        self.assertEqual([3.00,5.00,2.00,4.00,2047844,24367328.00], normed_days[1,:].tolist())
        self.assertEqual([4.00,6.00,3.00,5.00,2724569,32872520.00], normed_days[2,:].tolist())


if __name__ == '__main__':
    unittest.main()

