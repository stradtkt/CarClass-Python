class Car(object):
  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage
    if self.price > 10000:
      self.tax = 0.15
    else:
      self.tax = 0.12

  def display_all(self):
    print "Price: " + str(self.price)
    print "Speed: " + str(self.speed) + "mph"
    print "Fuel: " + self.fuel
    print "Mileage: " + str(self.mileage) + "mpg"
    print "Tax: " + str(self.tax)

print "\n"
car_1 = Car(1200, 120, "Full", 10)
car_1.display_all()
print "\n"
car_2 = Car(12000, 100, "Half-Full", 30)
car_2.display_all()
print "\n"    
car_3 = Car(10001, 200, "Half-Full", 60)
car_3.display_all()
print "\n"
car_4 = Car(10000, 80, "Full", 130)
car_4.display_all()
print "\n"
car_5 = Car(1000, 60, "Empty", 100)
car_5.display_all()
print "\n"
car_6 = Car(15000, 50, "Half-Full", 330)
car_6.display_all()

