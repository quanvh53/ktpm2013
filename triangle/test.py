from triangle import *
import unittest
import math

class testTriangle(unittest.TestCase):

    def testCheckinput1(self):
        self.assertEqual(True,checkinput(10.0,2.3,4.5))

    def testCheckinput2(self):
        self.assertEqual(True,checkinput(0.00001,0.00001,0.00001))

    def testCheckinput3(self):
        self.assertEqual(True,checkinput(1.0*(2**30),1.0*(2**30),1.0*(2**30)))

    def testCheckinput4(self):
        self.assertEqual(False,checkinput(1,12.0,3))

    def testCheckinput5(self):
        self.assertEqual(False,checkinput(0.00001,1,0.00001))

    def testCheckinput6(self):
        self.assertEqual(False,checkinput(2**30,1.0*(2**30),1.0*(2**30)))

    def testDetect_triangle1(self):
        self.assertEqual('tam giac deu',detect_triangle(5.0,5.0,5.0))
    
    def testDetect_triangle11(self):
        self.assertEqual('tam giac deu',detect_triangle(0.1,0.1,0.1))
    
    def testDetect_triangle2(self):
        self.assertEqual('tam giac deu',detect_triangle(0.00001,0.00001,0.00001))
        
    def testDetect_triangle3(self):
        self.assertEqual('tam giac deu',detect_triangle(1.0*(2**10),1.0*(2**10),1.0*(2**10)))

    def testDetect_triangle31(self):
        self.assertEqual('tam giac deu',detect_triangle(1.0*(2**30),1.0*(2**30),1.0*(2**30)))

    def testDetect_triangle4(self):
        self.assertEqual('tam giac vuong can',detect_triangle(5.0,5.0,5.0*math.sqrt(2)))
    
    def testDetect_triangle41(self):
        self.assertEqual('tam giac vuong can',detect_triangle(5.0,5.0*math.sqrt(2)),5.0)
    
    def testDetect_triangle42(self):
        self.assertEqual('tam giac vuong can',detect_triangle(5.0*math.sqrt(2),5.0,5.0))

    def testDetect_triangle5(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*math.pow(10,-30),1.0*math.pow(10,-30),1.0*math.pow(10,-30)*math.sqrt(2)))
    
    def testDetect_triangle51(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*math.pow(10,-30),1.0*math.pow(10,-30)*math.sqrt(2),1.0*math.pow(10,-30)))
    
    def testDetect_triangle52(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*math.pow(10,-30)*math.sqrt(2),1.0*math.pow(10,-30),1.0*math.pow(10,-30)))
    
    def testDetect_triangle53(self):
        self.assertEqual('tam giac vuong can',detect_triangle(0.1,0.1,1.0*math.sqrt(2)))
    
    def testDetect_triangle54(self):
        self.assertEqual('tam giac vuong can',detect_triangle(0.1,1.0*math.sqrt(2),0.1))
    
    def testDetect_triangle55(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*math.sqrt(2),0.1,0.1))

    def testDetect_triangle6(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*(2**30),1.0*(2**30),1.0*(2**30)*math.sqrt(2)))
    
    def testDetect_triangle61(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*(2**30),1.0*(2**30)*math.sqrt(2),1.0*(2**30)))
        
    def testDetect_triangle62(self):
        self.assertEqual('tam giac vuong can',detect_triangle(1.0*(2**30)*math.sqrt(2),1.0*(2**30),1.0*(2**30)))

    def testDetect_triangle7(self):
        self.assertEqual('tam giac can',detect_triangle(4.0,4.1,4.1))
    
    def testDetect_triangle71(self):
        self.assertEqual('tam giac can',detect_triangle(4.0,4.0,4.1))
    
    def testDetect_triangle72(self):
        self.assertEqual('tam giac can',detect_triangle(4.1,4.0,4.1))

    def testDetect_triangle8(self):
        self.assertEqual('tam giac can',detect_triangle(0.00001,0.000011,0.00001))

    def testDetect_triangle81(self):
        self.assertEqual('tam giac can',detect_triangle(0.000011,0.00001,0.00001))
    
    def testDetect_triangle82(self):
        self.assertEqual('tam giac can',detect_triangle(0.00001,0.00001,0.000011))

    def testDetect_triangle9(self):
        self.assertEqual('tam giac can',detect_triangle(1.0*(2**30),1.0*(2**30),1.2*(2**30)))
    
    def testDetect_triangle91(self):
        self.assertEqual('tam giac can',detect_triangle(1.0*(2**30),1.2*(2**30),1.0*(2**30)))
    
    def testDetect_triangle92(self):
        self.assertEqual('tam giac can',detect_triangle(1.2*(2**30),1.0*(2**30),1.0*(2**30)))
    
    def testDetect_triangle93(self):
        self.assertEqual('tam giac can',detect_triangle(1.0*(2**30),1.0*(2**30),0.00001))
    
    def testDetect_triangle94(self):
        self.assertEqual('tam giac can',detect_triangle(0.00001,1.0*(2**30),1.0*(2**30)))
        
    def testDetect_triangle95(self):
        self.assertEqual('tam giac can',detect_triangle(1.0*(2**30),0.00001,1.0*(2**30)))
    
    def testDetect_triangle96(self):
        self.assertEqual('tam giac can',detect_triangle(0.00001,1.0*(2**30),0.00001))
    
    def testDetect_triangle97(self):
        self.assertEqual('tam giac can',detect_triangle(1.0*(2**30),0.00001,0.00001))
        
    def testDetect_triangle98(self):
        self.assertEqual('tam giac can',detect_triangle(0.00001,0.00001,1.0*(2**30)))
    
    def testDetect_triangle10(self):
        self.assertEqual('tam giac vuong',detect_triangle(4.0,3.0,5.0))
    
    def testDetect_triangle101(self):
        self.assertEqual('tam giac vuong',detect_triangle(3.0,4.0,5.0))
    
    def testDetect_triangle102(self):
        self.assertEqual('tam giac vuong',detect_triangle(4.0,5.0,3.0))

    def testDetect_triangle11(self):
        self.assertEqual('tam giac vuong',detect_triangle(0.00003,0.00004,0.00005))
    
    def testDetect_triangle111(self):
        self.assertEqual('tam giac vuong',detect_triangle(0.00004,0.00003,0.00005))
    
    def testDetect_triangle112(self):
        self.assertEqual('tam giac vuong',detect_triangle(0.00005,0.00004,0.00003))

    def testDetect_triangle12(self):
        self.assertEqual('tam giac vuong',detect_triangle(3.0*(10**31),4.0*(10**31),5.0*(10**31)))
    
    def testDetect_triangle121(self):
        self.assertEqual('tam giac vuong',detect_triangle(4.0*(10**31),3.0*(10**31),5.0*(10**31)))
    
    def testDetect_triangle122(self):
        self.assertEqual('tam giac vuong',detect_triangle(4.0*(10**31),5.0*(10**31),3.0*(10**31)))

    def testDetect_triangle13(self):
        self.assertEqual('tam giac thuong',detect_triangle(4.0,6.0,5.0))
    
    def testDetect_triangle131(self):
        self.assertEqual('tam giac thuong',detect_triangle(5.0,6.0,4.0))
        
    def testDetect_triangle13(self):
        self.assertEqual('tam giac thuong',detect_triangle(6.0,4.0,5.0))

    def testDetect_triangle14(self):
        self.assertEqual('tam giac thuong',detect_triangle(0.00004,0.00006,0.00005))
    
    def testDetect_triangle141(self):
        self.assertEqual('tam giac thuong',detect_triangle(0.00005,0.00006,0.00004))
    
    def testDetect_triangle142(self):
        self.assertEqual('tam giac thuong',detect_triangle(0.00006,0.00005,0.00004))

    def testDetect_triangle15(self):
        self.assertEqual('tam giac thuong',detect_triangle(4.0*(10**31),6.0*(10**31),5.0*(10**31)))
    
    def testDetect_triangle151(self):
        self.assertEqual('tam giac thuong',detect_triangle(6.0*(10**31),5.0*(10**31),4.0*(10**31)))
    
    def testDetect_triangle152(self):
        self.assertEqual('tam giac thuong',detect_triangle(5.0*(10**31),6.0*(10**31),4.0*(10**31)))

    def testDetect_triangle16(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(4.0,3.0,8.0))

    def testDetect_triangle17(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(0.00004,0.00003,0.00008))
    
    def testDetect_triangle18(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(4.0*(10**31),3.0*(10**31),9.0*(10**31)))
    
    def testDetect_triangle181(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(4.0,3.0*(10**31),9.0*(10**31)))
    
    def testDetect_triangle182(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(4.0*(10**31),3.0*(10**31),9.0))
    
    def testDetect_triangle183(self):
        self.assertEqual('khong phai la tam giac',detect_triangle(4.0*(10**31),0.000001,9.0*(10**31)))
    
    
unittest.main()
