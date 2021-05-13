from LogRecord import LogRecord


class NodeRecord(LogRecord):
    # These fields can be private, no classes will extend NodeRecord ==> DONE
    __cpuUsage = 0
    __ramUsage = 0
    __loadFactor = 0
    __bytesTx = 0
    __bytesRx = 0
    __bandwidthRx = 0
    __bandwidthTx = 0
    __hostname = 0
    __time = 0

    def __init__(self, cpuUsage, ramUsage, loadFactor, bytesTx, bytesRx, bandwidthRx, bandwidthTx, hostname, time):
        self.__cpuUsage = cpuUsage
        self.__ramUsage = ramUsage
        self.__loadFactor = loadFactor
        self.__bytesTx = bytesTx
        self.__bytesRx = bytesRx
        self.__bandwidthRx = bandwidthRx
        self.__bandwidthTx = bandwidthTx
        self.__hostname = hostname
        self.__time = time
        # LogRecord is not define in the class diagram

    #SETTER

    def setCpuUsage(self, cpuUsage):
        self.__cpuUsage = cpuUsage

    def setRamUsage(self, ramUsage):
        self.__ramUsage = ramUsage

    def setLoadFactor(self, loadfactor):
        self.__loadFactor = loadfactor

    def setBytesRx(self, bytesRx):
        self.__bytesRx = bytesRx

    def setBytesTx(self, bytesTx):
        self.__bytesTx = bytesTx

    def setBandwidthRx(self, bandwidthRx):
        self.__bandwidthRx = bandwidthRx

    def setBandwidthTx(self, bandwidthTx):
        self.__bandwidthTx = bandwidthTx

    def setHostname(self, hostname):
        self.__hostname = hostname

    def setTime(self, time):
        self.__time = time

    #GETTER

    def getCpuUsage(self):
        return self.__cpuUsage

    def getRamUsage(self):
        return self.__ramUsage

    def getLoadFactor(self):
        return self.__loadFactor

    def getBytesRx(self):
        return self.__bytesRx

    def getBytesTx(self):
        return self.__bytesTx

    def getBandwidthRx(self):
        return self.__bandwidthRx

    def getBandwidthTx(self):
        return self.__bandwidthTx

    def getHostname(self):
        return self.__hostname

    def getTime(self):
        return self.__time
