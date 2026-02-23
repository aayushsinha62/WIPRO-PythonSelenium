import time
from datetime import datetime

def now():
    return datetime.now().strftime("%H:%M:%S.%f")[:-3]  # milliseconds

def test_case1():
    print(f"{now()} → testcase1 started")
    time.sleep(10)
    print(f"{now()} → testcase1 finished")

def test_case2():
    print(f"{now()} → testcase2 started")
    time.sleep(10)
    print(f"{now()} → testcase2 finished")

def test_case3():
    print(f"{now()} → testcase3 started")
    time.sleep(10)
    print(f"{now()} → testcase3 finished")

def test_api(api_url):
    assert "https" in api_url