
class Axis():
    
    radPerRevolution = 6.28319

    def __init__(self, driver, min=0, max=0, speed=20, microstep=16, current=None, steps=3200):
        self._min = min
        self._max = max
        self._stepsPerRevolution = steps
        self._microstep = microstep
        self._driver = driver

        driver.resetDev()
        driver.setMicroSteps(microstep)
        if current is None: 
            driver.setCurrent(65,65,65,65)
        else:
            driver.setCurrent(*current)
        print("setting up drive with", speed, current)
        driver.setMaxSpeed(speed)


    def isBusy(self):
        return self._driver.isBusy()
    
    def getPosition(self):
        return self._driver.getPosition()

    def goTo(self, posInStep):
        self._driver.goTo(posInStep)

    def goToRad(self, rad):
        # step / stepPerRevolution = rad / radPerRevolution
        step = rad * self._stepsPerRevolution / Axis.radPerRevolution
        withinLimitStep = max(min(step, self._max), self._min)
        self._driver.goTo(withinLimitStep)

    def getPositionInRad(self):
        # step / stepPerRevolution = rad / radPerRevolution
        step = self._driver.getPosition()
        stepInRad = step * Axis.radPerRevolution/ float(self._stepsPerRevolution)
        return stepInRad