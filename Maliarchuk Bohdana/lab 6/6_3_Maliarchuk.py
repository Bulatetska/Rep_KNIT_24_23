class Plane:
    def __init__(self, model):
        self.model = model
        
    def hide_pass(self):
        print("Plane {} takes off from the runway".format(self.model))
        
    def take_off(self):
        print("Plane {} is taking off".format(self.model))
        
    def fly(self):
        print("Plane {} flies".format(self.model))
        
    def land(self):
        print("Plane {} is landing".format(self.model))

s = Plane("Mria")
s.hide_pass()
s.take_off()
s.fly()
s.land()