import RPi.GPIO as GPIO

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

    def getPosInRad(self):
        # From 7 to 17
        return ((self._gripper - 7) / 10) * 1.5708

    def goToInRad(self, rad):
        nStep = ((rad / 1.5708) * 10) + 7
        nStep = max(7, min(int(nStep), 17))
        if nStep != self.getPosition():
            print("Gripper go to: ", rad, nStep)
            self.goTo(nStep)
        
    def goTo(self, nStep):
        if nStep >= 0 and nStep <= 17:
            self._gripper = nStep
            self._pwm.start(self._gripper)