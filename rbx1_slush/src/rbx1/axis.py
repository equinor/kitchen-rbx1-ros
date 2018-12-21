
class Axis():
    
    radPerRevolution = 6.28319

    def __init__(self, driver, minimum=0, maximum=0, speed=20, microstep=16, current=None, steps=3200, negate=False):
        self._minimum = minimum
        self._maximum = maximum
        self._negate = negate
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
        if self._driver.isBusy(): return
        if self._negate: rad = -rad
        step = rad * self._stepsPerRevolution / Axis.radPerRevolution
        withinLimitStep = max(min(step, self._maximum), self._minimum)
        print("Go to step: ", withinLimitStep)
        self._driver.goTo(withinLimitStep)

    def getPositionInRad(self):
        # step / stepPerRevolution = rad / radPerRevolution
        step = self._driver.getPosition()
        stepInRad = step * Axis.radPerRevolution/ float(self._stepsPerRevolution)
        return stepInRad