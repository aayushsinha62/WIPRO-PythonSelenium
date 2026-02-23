
#function level - runs once per function

def test_function_1(function_setup):
    print("Executing test_function_1")

def test_function_2(function_setup):
    print("Executing test_function_2")

def test_function_3(function_setup):
    print("Executing test_function_3")

#class level - runs once per class

class TestUserActions1:

    def test_class_action_1(self, class_setup):
        print("Executing test_action_1")

    def test_class_action_2(self, class_setup):
        print("Executing test_action_2")

    def test_class_action_3(self, class_setup):
        print("Executing test_action_3")

class TestUserActions2:

    def test_class_action_1(self, class_setup):
        print("Executing test_action_4")

    def test_class_action_2(self, class_setup):
        print("Executing test_action_5")

    def test_class_action_3(self, class_setup):
        print("Executing test_action_6")


#module level - runs once per file // teardown runs at second last if session level present else at last

def test_module_1(module_setup):
    print("Executing test_module_1")

def test_module_2(module_setup):
    print("Executing test_module_2")

def test_module_3(module_setup):
    print("Executing test_module_3")

#session level - runs once per whole session so at the last printed

def test_session_one(session_setup):
    print("Test one executed")

def test_session_two(session_setup):
    print("Test two executed")

def test_session_three(session_setup):
    print("Test three executed")

