#module level - runs once per module(file)
#use module level setup and tear down when you want to execute
#      the setup and teardown once in the current file
#       eg: open the db connection, execute all testcases and at last close the db connection


import pytest

def setup_module(module):
    print("open the db connection")

# setup_module - -> only one per file
# setup_class() -> one per class
# setup_method() -> one per class
# setup_function() -> one per file
#if created multiple, it overrides it


def teardown_module(module):
    print("close the db connection")




#testcase1

def testread():
    print("reading is executed")

#testcase2

def testwrite():
    print("write is executed")

#testcase3

def testupdating():
    print("update is executed")