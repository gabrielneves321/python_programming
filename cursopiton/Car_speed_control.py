

class Car: 
    def __init__(self,maximum_speed ):
     self.maximum_speed = maximum_speed
     self.current_speed = 0

    def speed_up(self,delta=5):
     maximum = self.maximum_speed
     new = self.current_speed + delta
     self.current_speed = new if new <= maximum else maximum
     return self.current_speed

    def brake(self, delta=5):
        new = self.current_speed - delta
        self.current_speed = new if new >=0 else 0
        return self.current_speed

if __name__ == '__main__':
        c1 = Car(180)

        for _ in range(25):
         print(c1.speed_up(8))

        for _ in range(10):
         print(c1.brake(delta=20))   

         



    