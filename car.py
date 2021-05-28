class car:
    def __init__(self,color,make,model,registration,) :
        self.color=color
        self.make=make
        self.model=model
        self.registration=registration
    def car(self):
        return f"hello this is{self.make} {self.model} and it's  {self.registration}  {self.color} in color"

    def hoot(self):
        hoots="peeeeeeep"
        mileage=2800
        return "A car{} has a mileage of {} and it hoots like this {}.".format(self.make,mileage,hoots)
