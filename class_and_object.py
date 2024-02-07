class Car:
    def __init__(self,name,price):
        self.name = name 
        self.price = price
        
    def ShowDetails(self):
        print(f"Car name : {self.name}")
        print(f"Car Price : {self.price}$\n")



Maruti =Car("Maruti" ,200000)
Maruti.ShowDetails()

Toyota = Car("Toyota", 50000)
Toyota.ShowDetails()