class Car(object):

  def __init__(self, price, speed, fuel, mileage):
    self.price = price
    self.speed = speed
    self.fuel = fuel
    self.mileage = mileage

  def drive(self):
    print("Vroom!")
    self.speed = 35


  def display_car(self):
    if self.price > 10000:
      tax = self.price * 0.15
      final_price = self.price + tax
    else:
      tax = self.price * 0.12
      final_price = self.price + tax
    return print("Price: {}, Speed: {}, Fuel: {}, Mileage: {}".format(final_price,self.speed,self.fuel,self.mileage))

  def detect_speed(self):
    if self.speed >= 55 and self.speed <= 80:
      print("You are traveling at a safe speed on the highway")
    elif self.speed < 55 and self.speed >= 35:
      print("You are on a main city road")
    elif self.speed < 35 and self.speed > 0:
      print("You are in a parking lot")
    elif self.speed == 0:
      print("Your car is stopped")
    else:
      print("You are most likely going to fast")

car = Car(12000, 120, 'Full', 30000)
car.display_car()
car.drive()