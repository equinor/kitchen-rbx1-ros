import RPi.GPIO as GPIO
import Slush

from .axis import Axis

class Robot:

    def __init__(self):
        #setup all of the axis for the SlushEngine
        Slush.sBoard()
        
        # steps per revolution obtained by manual obervation of steps to do 90 degree
        # multiplying by four to get steps per 360 degree.
        self._axis = [
            Axis(Slush.Motor(1), minimum=-8000, maximum=5500, speed=10, current=[65, 65, 65, 65], steps=32000), #Shoulder
            Axis(Slush.Motor(0), minimum=-4000, maximum=4000, speed=10, current=[65, 70, 60, 70], steps=16000), #Arm
            Axis(Slush.Motor(2), minimum=-20000, maximum=20000, speed=20, current=[50, 50, 50, 50], steps=64000),
            Axis(Slush.Motor(3), minimum=-3000, maximum=3000, speed=20, current=[75, 75, 75, 75], steps=6000),
            Axis(Slush.Motor(4), minimum=-4000, maximum=4000, speed=20, current=[85, 85, 85, 85], steps=14000),
            Axis(Slush.Motor(5), minimum=-1650, maximum=1650, speed=20, current=[65,65, 65, 65], steps=3600)
        ]

        self._target = list(map(lambda a: a.getPositionInRad(), self._axis))
        self._target.insert(0, 0)
        self._target.insert(0, 0)

    def isBusy(self):
        for axis in self._axis:
            if axis.isBusy(): return True
        return False

    def runRobot(self, points):
        if self.isBusy(): return
        self._target = points
        
        for axis, value in zip(self._axis, self._target):
            if (value is not None):
                axis.goToRad(value)


    def getStatus(self): 
        pos = list(map(lambda a: a.getPositionInRad(), self._axis))
        pos.insert(0,0)
        pos.insert(0,0)
        return {
            'busy': self.isBusy(),
            'targetPos' : self._target,
            'currentPos': pos 
        }

class Gripper:
    def __init__(self):
        #setup the gripper
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self._pwm = GPIO.PWM(18, 100)
        self._gripper = 7

    def isBusy(self):
        return False
    
    def getPosition(self):
        return self._gripper

    def goTo(self, nStep):
        self._gripper = nStep
        self._pwm.start(self._gripper)