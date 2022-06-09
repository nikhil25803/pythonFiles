
class Ws:

    def displayinfo(self):
        print("Welcome to Wscubetech ")

class Ws2(Ws):

    
    def displayinfo(self):
        # Overriding
        super().displayinfo()

        print("Welcome to Wscubetech 2")

obj = Ws2()
obj.displayinfo()
