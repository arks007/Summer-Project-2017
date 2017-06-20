class Engine(object):

    def __init__(self, name, pv):
        self.name = name
        self.pv = 0

    def setPV(self, new_pv):
        self.pv = new_pv

    def getPV (self):
        return self.pv

    def setName(self, new_name):
        self.name = new_name

    def getName(self):
        return self.name





