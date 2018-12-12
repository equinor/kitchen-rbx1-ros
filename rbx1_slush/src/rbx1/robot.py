import RPi.GPIO as GPIO
import Slush

class Robot:
    def __init__(self):
        #setup all of the axis for the SlushEngine
        Slush.sBoard()
        joints = [Slush.Motor(0), Slush.Motor(1), Slush.Motor(2), Slush.Motor(3), Slush.Motor(4), Slush.Motor(5)]
        
        #reset the joints to clear previous errors
        for joint in joints:
            joint.resetDev()
            joint.setMicroSteps(16)

        #some initalization stuff that needs cleanup
        joints[0].setMaxSpeed(30)
        joints[1].setMaxSpeed(30)
        joints[2].setMaxSpeed(30)
        joints[3].setMaxSpeed(30)
        joints[4].setMaxSpeed(30)
        joints[5].setMaxSpeed(30)

        #joint current limits. Still setting manually becuase testing (hold A, run A, acc A, dec, A)
        joints[0].setCurrent(65, 85, 75, 70)
        joints[1].setCurrent(65, 85, 85, 65)
        joints[2].setCurrent(50, 50, 50, 50)
        joints[3].setCurrent(75, 75, 75, 75)
        joints[4].setCurrent(85, 85, 85, 85)
        joints[5].setCurrent(65,65, 65, 65)
        
        self._axis = [
            Axis(-5000,5000,joints[0]),
            Axis(-12500,12500,joints[1]),
            Axis(-22500,22500,joints[2]),
            Axis(-3500,3500, joints[3]),
            Axis(-4000,4000,joints[4]),
            Axis(-1650,1650,joints[5])
        ]
        self._target = list(map(lambda a: a.getPosition(), self._axis))

    def isBusy(self):
        for axis in self._axis:
            if axis.isBusy(): return True
        return False

    def runRobot(self, points):
        if self.isBusy(): return
        self._target = points
        
        for axis, value in zip(self._axis, self._target):
            if (value is not None):
                axis.goTo(value)


    def getStatus(self): 
        return {
            'busy': self.isBusy(),
            'targetPos' : self._target,
            'currentPos' : list(map(lambda a: a.getPosition(), self._axis))
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

class Axis():
    def __init__(self, min, max, driver):
        self._min = min
        self._max = max
        self._driver = driver

    def isBusy(self):
        return self._driver.isBusy()
    
    def getPosition(self):
        return self._fromStep(self._driver.getPosition())

    def goTo(self, pos):
        self._driver.goTo(self._toStep(pos))

    def _toStep(self, value):
        value = (value + 1) / 2
        value = value * (self._max - self._min)
        return int(value + self._min)
    
    def _fromStep(self, value):
        value -= self._min
        value = value / (self._max - self._min)
        return (value * 2) -1