class MockRobot:
    def __init__(self):
        self._axis = [
            Axis(),
            Axis(),
            Axis(),
            Axis(),
            Axis(),
            Axis()
        ]
        self._target = list(map(lambda a: a.getPosition(), self._axis))

    def isBusy(self):
        return False

    def runRobot(self, points):
        print('runRobot', points)

    def runGripper(self, points):
        print('runGripper', points)

    def getStatus(self): 
        return {
            'busy': self.isBusy(),
            'targetPos' : self._target,
            'currentPos' : list(map(lambda a: a.getPosition(), self._axis))
        }

class Axis():
    def __init__(self):
        self._pos = 0

    def getPosition(self):
        return self._pos