import diskclean
import unittest
import filecmp

class test_diskclean(unittest.TestCase):
    def test_case_01(self):
        diskclean.main(["./diskclean.py","./TestCases/Case1/D1/", "./TestCases/Case1/D2/"])
        self.assertTrue(filecmp.cmp("./Report.txt","./TestCases/Outputs/1.out",shallow=False),"Output file mismatch")

    def test_case_02(self):
        diskclean.main(["./diskclean.py","./TestCases/Case2/D1/", "./TestCases/Case2/D2/"])
        self.assertTrue(filecmp.cmp("./Report.txt","./TestCases/Outputs/2.out",shallow=False),"Output file mismatch")

    def test_case_03(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case3/D1/", "./TestCases/Case3/D2/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/3.out", shallow=False), "Output file mismatch")

    def test_case_04(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case4/D1/", "./TestCases/Case4/D3/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/4.out", shallow=False), "Output file mismatch")


    def test_case_05(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case5/D1/", "./TestCases/Case5/D3/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/5.out", shallow=False), "Output file mismatch")


    def test_case_06(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case6/D1/", "./TestCases/Case6/D3/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/6.out", shallow=False), "Output file mismatch")


    def test_case_07(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case7/D1/", "./TestCases/Case7/D2/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/7.out", shallow=False), "Output file mismatch")


    def test_case_08(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case8/D1/", "./TestCases/Case8/D2/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/8.out", shallow=False), "Output file mismatch")


    def test_case_09(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case9/D1/", "./TestCases/Case9/D2/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/9.out", shallow=False), "Output file mismatch")


    def test_case_10(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case10/D1/", "./TestCases/Case10/D4/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/10.out", shallow=False), "Output file mismatch")

    def test_case_11(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case11/D1/", "./TestCases/Case11/D4/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/11.out", shallow=False), "Output file mismatch")

    def test_case_12(self):
        diskclean.main(["./diskclean.py", "./TestCases/Case12/D1/", "./TestCases/Case12/D2/"])
        self.assertTrue(filecmp.cmp("./Report.txt", "./TestCases/Outputs/12.out", shallow=False), "Output file mismatch")

if __name__ == '__main__':
    unittest.main()