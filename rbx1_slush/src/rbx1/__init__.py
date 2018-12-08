try:
    import RPi.GPIO as GPIO
    from .robot import Robot
except ImportError:
    from .mock_robot import MockRobot as Robot

class RobotSingleton:
    __instance = None

    @staticmethod
    def getInstance():
        if RobotSingleton.__instance == None:
            RobotSingleton()
        return RobotSingleton.__instance 

    def __init__(self):
        """ Virtually private constructor. """
        if RobotSingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            RobotSingleton.__instance = Robot()