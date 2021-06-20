class Laser:
    def does(self):
        return 'disintergrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self, laser, claw, smartphone):
        self.laser = laser
        self.claw = claw
        self.smartphone = smartphone

    def does(self):
        print('Laser :', self.laser.does(), ', Claw :', self.claw.does(), ", SmartPhone :", self.smartphone.does())


l = Laser()
c = Claw()
s = SmartPhone()
r = Robot(l, c, s)

r.does()
