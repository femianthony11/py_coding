import numTranscriptelegant
from numTranscriptelegant import oned
from numTranscriptelegant import twod
from numTranscriptelegant import threed
from numTranscriptelegant import fourd
from numTranscriptelegant import main
from numTranscriptelegant import runn
import unittest

class NumTest(unittest.TestCase):
    def setUp(self):
        self.testlist = { 0:"Zero", 
                11:"Eleven", 
                103:"One Hundred and Three", 
                200:"Two Hundred", 
                504:"Five Hundred and Four", 
                479:"Four Hundred and Seventy Nine", 
                902:"Nine Hundred and Two", 
                999:"Nine Hundred and Ninety Nine", 
                1001:"One Thousand and One", 
                1111:"One Thousand One Hundred and Eleven", 
                2040:"Two Thousand Forty", 
                3333:"Three Thousand Three Hundred and Thirty Three", 
                2002:"Two Thousand and Two", 
                5555:"Five Thousand Five Hundred and Fifty Five", 
                9130:"Nine Thousand One Hundred and Thirty", 
                9999: "Nine Thousand Nine Hundred and Ninety Nine"}
    testlst = [0,11]
    def test_fact(self):
        for item in self.testlist:
            n = str(item)
            res = runn(n)
            print(n)
            print(runn(n))
            self.assertEqual(res,self.testlist[item])



if __name__ == "__main__":
    unittest.main()