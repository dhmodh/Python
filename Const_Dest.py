class TestClass:

    @staticmethod
    def StaticMethod():
        print ("static")
    
    def __init__(self):
        print ("constructor")

    def __del__(self):
        print ("destructor")

if __name__ == "__main__":
    obj = TestClass()
    # the following both are ok.
    TestClass.StaticMethod() 
    obj.StaticMethod()
    del obj
