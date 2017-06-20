import Engine.py
import Aileron.py
# import Radio.py

class Plane(object):
    def __init__(self, name, state):
        self.name = name
        # state is a boolean
        self.state = state
        self.state = False

    def setName(self, new_name):
        self.name = new_name

    def getName(self):
        return self.name

    def setState(self, new_state):
        self.state = new_state

    def getState(self):
        return self.state

    def flightInit(self, engine_name, radio_name, aileron_1, aileron_2, aileron_3, perform_diagnostics):
        engine = Engine(engine_name, 0)
        aileron1 = Aileron(aileron_1, 0)
        aileron2 = Aileron(aileron_2, 0)
        aileron3 = Aileron(aileron_3, 0)
        # radio = (radio_name)

        # perform_diagnostics is a boolean

        # set up i/o connections (throw exception if needed)
        # fire up thrusters

        # plane engine/flaps are active
        self.state = True

        if (perform_diagnostics):
            def flightDiagnosticTest(self):
                # step 1:
                aileron1.setAngle(-60)
                aileron2.setAngle(-60)
                aileron3.setAngle(-60)
                # step 2:
                aileron1.setAngle(60)
                aileron2.setAngle(60)
                aileron3.setAngle(60)
                # step 3:
                aileron1.setAngle(0)
                aileron2.setAngle(0)
                aileron3.setAngle(0)
                # step 4:
                aileron1.setAngle(-60)
                aileron2.setAngle(-60)
                aileron3.setAngle(60)
                # step 5:
                aileron1.setAngle(60)
                aileron2.setAngle(60)
                aileron3.setAngle(-60)
                # step 6:
                aileron1.setAngle(0)
                aileron2.setAngle(0)
                aileron3.setAngle(0)
                # step 7:
                engine.setPV(.1)

    def iterativeControl(self):
        # engage flight when the state is True
        while (self.state):
            pass
            # get input radio signals from the radio object (input will be mapped)
            # execute changes in engine power/ailerons
            # send data to user (telemetry)

