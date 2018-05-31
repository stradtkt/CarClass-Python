class Car(object):

  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage

  def drive(self):
    print("Vroom!")
    self.mileage = self.mileage + 15
    return self.mileage


  def display_car(self):
     return print("Price: {}, Speed: {}, Fuel: {}, Mileage: {}".format(self.price, self.speed,self.fuel,self.mileage))
  def taxes(self):
    if self.price > 10000:
      tax = 0.15
      compute_tax = self.price * tax
      final_price = self.price + compute_tax
    else:
      tax = 0.12
      compute_tax = self.price * tax
      final_price = self.price + compute_tax
    print("Tax: {}\nAdded Amount: {}\nFinal Price: {}".format(tax, compute_tax, final_price))
    return final_price

  def detect_speed(self):
    if self.speed > 55:
      print("You are most likely on a highway")

car = Car(12000, 120, 'Full', 30000)
car.display_car()
car.drive()
car.detect_speed()
car.taxes()
car.drive()
car.drive()
car.drive()
car.drive()
car.display_car()