#used inside the classes
#it will run for every class definition once
#it will run in starting and ending of the class

class Testclass1:

    #class level setup

    def setup_class(cls):
        print("API Authorization needed with username and pw")

    def teardown_class(cls):
        print("API authorization closed")


    #testcase1
    def testcase1(self):
        print("Testcase1 is executed")

    #testcase2

    def testcase2(self):
        print("Testcase2 is executed")

    #testcase3

    def test_case3(self):
        print("Testcase3 is executed")

class Testclass2:

    #testcase1
    def testcase1(self):
        print("Testcase1 is executed")

    #testcase2

    def testcase2(self):
        print("Testcase2 is executed")

    #testcase3

    def test_case3(self):
        print("Testcase3 is executed")