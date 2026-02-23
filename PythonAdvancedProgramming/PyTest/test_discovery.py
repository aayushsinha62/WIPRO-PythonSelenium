#unit testing is type of testing done by developers
#what component they have developed they do the testing before integrating it to other modules
#get defects earlier
#Pytest in python, Junit and unit-Java

#pytest is used by developers and testers

#test discovery -  rules used to create pytest tests
#-v verbose - show detailed output
#-s - show print statements

#rules
#files should start with test/test_/test1
#functions should also start with test

import pytest



#testcase1

def testcase1():
    print("Testcase1 is executed")

#testcase2

def testcase2():
    print("Testcase2 is executed")

#testcase3

def test_case3():
    print("Testcase3 is executed")

#testcase4

def testopenbrowser():
    print("Opening the browser")



