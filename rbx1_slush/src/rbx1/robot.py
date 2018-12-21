import Slush

from .axis import Axis
from .gripper import Gripper

class Robot:

    def __init__(self):
        #setup all of the axis for the SlushEngine
        Slush.sBoard()
        
        # steps per revolution obtained by manual obervation of steps to do 90 degree
        # multiplying by four to get steps per 360 degree.
        self._axis = [
            Axis(Slush.Motor(1), minimum=-8000, maximum=5500, speed=10, current=[65, 65, 65, 65], steps=32000), #Shoulder
            Axis(Slush.Motor(0), minimum=-4000, maximum=4000, speed=10, current=[65, 70, 60, 70], steps=16000), #Arm
            Axis(Slush.Motor(2), minimum=-20000, maximum=20000, speed=30, current=[50, 50, 50, 50], steps=64000),
            Axis(Slush.Motor(3), minimum=-3000, maximum=3000, speed=20, current=[75, 75, 75, 75], steps=6000),
            Axis(Slush.Motor(4), minimum=-4000, maximum=4000, speed=20, current=[85, 85, 85, 85], steps=14000),
            Axis(Slush.Motor(5), minimum=-1650, maximum =1650, speed=20, current=[65,65, 65, 65], steps=3600)
        ]
        self._gripper = Gripper()

        self._target = list(map(lambda a: a.getPositionInRad(), self._axis))
        posOfGripper = self._gripper.getPosInRad()
        self._target.insert(0, posOfGripper)
        self._target.insert(0, posOfGripper)

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

    def runGripper(self, points):
        self._gripper.goToInRad(points[0])

    def getStatus(self): 
        pos = list(map(lambda a: a.getPositionInRad(), self._axis))
        posOfGripper = self._gripper.getPosInRad()
        pos.insert(0, posOfGripper)
        pos.insert(0, posOfGripper)
        return {
            'busy': self.isBusy(),
            'targetPos' : self._target,
            'currentPos': pos 
        }