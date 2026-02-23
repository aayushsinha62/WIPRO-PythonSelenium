#basic assertion

import pytest_check as check


#hard assertion - this will stop the execution of the next line in that testcase

#soft assertion - next line will still run even if the assertion fail
        #python doesn't directly support soft assertion
        #only supports through plugins

def test_add():
    result = 2+3
    assert result==5

#checking true or false

def test_boolean():
    assert True
    assert not False

#none value

    value=None
    assert value is None

#list assertion

def test_list():
    fruits=["apple","banana","orange"]
    assert "banana" in fruits

#soft assertion

def test_equal():
    check.equal(1,5) #false
    print("\n\nhello") #next line works as its soft assertion

test_equal()

def test():
    assert 1==2 #false
    print("Hello") #next line is appearing faint as hard assertion, next line doesnt work

#dictionary assertion

def test_dict():
    creds={"username":"admin","password":"admin123"}
    assert creds["password"] == "admin123"

#comparing lists

def test_comparelist():
    assert [1,2,3]==[1,2,3]

#assertion with custom message

def test_custommsg():
    result=10
    assert result==10,"Should be 10 but got 5"










