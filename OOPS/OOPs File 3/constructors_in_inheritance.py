
class A: # Super/ Parent Class

    def __init__(self):
        print("in A init")

    def feature1(self):
        print("Feature one is working")

    def feature2(self):
        print("Feature 2 is working")


class B(A): # Sub / Child Class

    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

# a1 = B() 
# Will it call constructor of A? Yes it will !

# But if B will also have a constructor, then it call constructor of B only

# This can be solved using super() method

a1 = B()

