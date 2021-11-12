import unittest
import time
import Google_NLP as GN

class TestGoogleNLP(unittest.TestCase):
    def setup(self):
        self.startTime =time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_print_result(self):
        #Give this unit one second to stop and then continue running
        time.sleep(1)
        #Open the correct results txt file
        with open("Google_NLP_results.txt","r") as results:
            #Use asserEqual to compare if the results are right
            self.assertEqual(GN.print_result, results)

if __name__ == '__main__':
    #Start testing the program and use time module to test running time of unittest unit
    #Time function is also an example to show how to get every unit running time
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoogleNLP)
    unittest.TextTestRunner(verbosity=0).run(suite)
