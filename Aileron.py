class Aileron(object):
    def __init__(self, name, angle):
        # angle will go from -60deg --> 60deg#
        self.name = name
        self.angle = angle

    def setName(self, new_name):
        self.name = new_name

    def getName(self):
        return self.name

    def setAngle(self, new_angle):
        self.pv = new_angle
        # implement a time parameter

    def getAngle(self):
        return self.angle
