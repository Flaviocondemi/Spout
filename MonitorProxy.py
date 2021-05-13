
class MonitorProxy:

    _target = None

    def __init__(self, target):
        self._target = target

    def getTarget(self):
        return self._target

    def setTarget(self, target):
        self._target = target

    def getData(self):
        pass
