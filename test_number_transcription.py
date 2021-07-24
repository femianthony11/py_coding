import numTranscriptelegant
from numTranscriptelegant import oned
from numTranscriptelegant import twod
from numTranscriptelegant import threed
from numTranscriptelegant import fourd
from numTranscriptelegant import main
from numTranscriptelegant import runn
import unittest




testlist = [ 0, 11, 103, 200, 504, 479, 902, 999, 1001, 1111, 2040, 3333, 2002, 5555, 9130, 9999]


for item in testlist:
    n = str(item)
    print(n)
    print(runn(n))



if __name__ == "__main__":
    unittest.main()