from InsertionSort import InsertionSort
from MergeSort import MergeSort
import unittest

input1  =  [1,2,3,4,5,6,7,8,9,10]
output1 =  [1,2,3,4,5,6,7,8,9,10]
input2 = [9,1,21,5,6,8,109,4,20,50]
output2  =  [1,4,5,6,8,9,20,21,50,109]
input3  =  [10,9,8,7,6,5,4,3,2,1]
output3  = [1,2,3,4,5,6,7,8,9,10]


class   InsertionTestCase(unittest.TestCase):
    def test_insertionSort(self):
        
        InsertionSort(input1)
        InsertionSort(input2)
        InsertionSort(input3)
        self.assertEqual(input1,output1)
        self.assertEqual(input2,output2)
        self.assertEqual(input3,output3)

r1=len(input1)
r2=len(input2)
r3=len(input3)

class MergeSortCase(unittest.TestCase):
    def test_MergeSort(self):
        MergeSort(input1,0,r1)
        MergeSort(input2,0,r2)
        MergeSort(input3,0,r3)
        self.assertEqual(input1,output1)
        self.assertEqual(input2,output2)
        self.assertEqual(input3,output3)
        

if  __name__=="__main__":
    unittest.main() 

