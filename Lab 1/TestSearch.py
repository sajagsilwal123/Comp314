from msilib.schema import Class
import unittest
from LinearSearch import LinearSearch
from BinarySearch import BinarySearch

class SearchTestCase(unittest.TestCase):

    def test_LinearSearch(self):
        values = [3,4,21,12,17,61,55]
        self.assertEqual(LinearSearch(values, 55),6)
        self.assertEqual(LinearSearch(values, 21),2)
        self.assertEqual(LinearSearch(values, 17),4)

    def test_BinarySearch(self):
        values = [3,4,21,12,17,61,55]
        SortedValues = sorted(values)
        self.assertEqual(LinearSearch(SortedValues, 4),1)
        self.assertEqual(LinearSearch(SortedValues, 55),5)   
        

if __name__=="__main__":
    unittest.main()    