import numpy as np
import unittest
from data import read_tdx, match_one, match_all

class MyTest(unittest.TestCase):
    def test(self):
        print('MyTest:test()')


class DataTest(unittest.TestCase):
    def test_read_tdx(self):
        data, dates = read_tdx('testdata/testdata_1.txt')
        self.assertEqual(9, len(data))
        self.assertEqual(9, len(dates))
        expected_dates = ['2010/10/08', '2010/10/11', '2010/10/12',
                          '2010/10/13', '2010/10/14', '2010/10/15',
                          '2010/10/16', '2010/10/17', '2010/10/18']
        self.assertEqual(expected_dates, dates)
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[0,:].tolist())
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[1,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[2,:].tolist())
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[3,:].tolist())
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[4,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[5,:].tolist())
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[6,:].tolist())
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[7,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[8,:].tolist())

    def test_match_one(self):
        data, dates = read_tdx('testdata/testdata_1.txt')
        self.assertEqual(9, len(data))
        self.assertEqual(9, len(dates))

        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[0,:].tolist())
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[1,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[2,:].tolist())
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[3,:].tolist())
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[4,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[5,:].tolist())

        target = data[0:3,:]
        cand =   data[3:6,:]
        score = match_one(target, cand)
        self.assertEqual(0, score)
        score = match_one(target, cand, body_only=True)
        self.assertEqual(0, score)

        cand =   data[1:4,:]
        score = match_one(target, cand)
        self.assertEqual(160, score)
        score = match_one(target, cand, body_only=True)
        self.assertEqual(80, score)

    def test_match_all(self):
        data, dates = read_tdx('testdata/testdata_1.txt')
        self.assertEqual(9, len(data))
        self.assertEqual(9, len(dates))

        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[0,:].tolist())
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[1,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[2,:].tolist())

        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[3,:].tolist())
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[4,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[5,:].tolist())
        self.assertEqual([20.00,40.00,10.00,30.00,1214862,14319652.00], data[6,:].tolist())
        self.assertEqual([30.00,50.00,20.00,40.00,2047844,24367328.00], data[7,:].tolist())
        self.assertEqual([40.00,60.00,30.00,50.00,2724569,32872520.00], data[8,:].tolist())

        target = data[0:3,:]
        # cands =   data[3:,:]
        cands =   data[3:7,:]

        scores = match_all(target, cands)
        self.assertEqual(2, len(scores))
        self.assertEqual([0, 21], scores)

#        normed_target:
#        self.assertEqual([2.00,4.00,1.00,3.00,1214862,14319652.00], normed_days[0,:].tolist())
#        self.assertEqual([3.00,5.00,2.00,4.00,2047844,24367328.00], normed_days[1,:].tolist())
#        self.assertEqual([4.00,6.00,3.00,5.00,2724569,32872520.00], normed_days[2,:].tolist())

#        second candidate:
#        self.assertEqual([1.50,2.50,1.00,2.00,2047844,24367328.00], data[4,:].tolist()) 3
#        self.assertEqual([2.00,3.00,1.50,2.50,2724569,32872520.00], data[5,:].tolist()) 5
#        self.assertEqual([1.00,2.00,0.50,1.50,1214862,14319652.00], data[3,:].tolist()) 9.5 + 3.5 = 13


if __name__ == '__main__':
    unittest.main()

