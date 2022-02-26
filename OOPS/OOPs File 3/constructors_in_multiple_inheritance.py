# Method Resolution Order

class A: # Super/ Parent Class

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature one is working")

    def feature2(self):
        print("Feature 2 is working")


class B(): # Sub / Child Class

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A, B):
    
    def __init__(self):
        super().__init__()
        print("C in init")

c1 = C() 
# It will inherit all the features of A and C, not B

