import unittest
import akinatorDB as db

class test(unittest.TestCase):
        
    def testfichierPresent(self):
        p = db.bdd()
        self.assertEqual(p.openCSV(),True)

    
if __name__ == '__main__':
    unittest.main()

