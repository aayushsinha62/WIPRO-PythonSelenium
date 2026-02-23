#used inside the classes
#runs before and after the test method inside the class
#in case of inheritance, setup and teardowns are considered


class Testclass1:

    #class level setup

    def setup_class(cls):
        print("API Authorization needed with username and pw")

    def teardown_class(cls):
        print("API authorization closed")

    def setup_method(method):
        print("opening the browser")

    def teardown_methdod(method):
        print("closing the browser")

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