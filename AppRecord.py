from LogRecord import LogRecord


class AppRecord(LogRecord):

    #LogRecord is void: super() not implemented

    __bytesRx = 0
    __rootid = 0
    __caller = 0
    __executorIP = 0
    __action = 0
    __responseStatus = 0
    __startTime = 0
    __endTime = 0
    __bytesTx = 0
    __requestId = 0
    __requestName = 0
    __bwTx = 0
    __bwRx = 0
    __serviceName = 0
    __appId = 0

    def __init__(self,appid, bytesRx, rootid, caller, executorIP, action, responseStatus, startTime, endTime, bytesTx, requestId, requestName, bwTx, bwRx, serviceName):
        self.__bytes = bytesRx
        self.__appId = appid
        self.__rootId = rootid
        self.__caller = caller
        self.__executorIP = executorIP
        self.__action = action
        self.__responseStatus = responseStatus
        self.__startTime = startTime
        self.__endTime = endTime
        self.__bytesTx = bytesTx
        self.__bytesRx = bytesRx
        self.__requestId = requestId
        self.__requestName = requestName
        self.__bwTx = bwTx
        self.__bwRx = bwRx
        self.__serviceName = serviceName
        #LogRecord is not defined in the class diagram

    #SETTER

    def setRequestName(self, requestName):
        self.__requestName = requestName

    def setAppId(self, apppid):
        self.__appId = apppid

    def setBytesRx(self, brx):
        self.__bytesRx = brx

    def setRootId(self, rId):
        self.__rootId = rId

    def setCaller(self, caller):
        self.__caller = caller

    def setExecutorIp(self, exIp):
        self.__executorIP = exIp

    def setAction(self, action):
        self.__action = action

    def setResponseStatus(self, responseStatus):
        self.__responseStatus = responseStatus

    def setStartTime(self, startTime):
        self.__startTime = startTime

    def setEndTime(self, endTime):
        self.__endTime = endTime

    def setBytesTx(self, bytesTx):
        self.__bytesTx = bytesTx

    def setBytesRx(self, bytesRx):
        self.__bytesRx = bytesRx

    def setRequestId(self, requestId):
        self.__requestId = requestId

    def setBwTx(self, bwTx):
        self.__bwTx = bwTx

    def setBwRx(self, bwRx):
        self.__bwRx = bwRx

    def setServiceName(self, serviceName):
        self.__serviceName = serviceName

    #GETTER


    def getAppId(self):
        return self.__appId

    def getBytesRx(self):
        return self.__bytesRx

    def getRootId(self):
        return self.__rootId

    def getCaller(self):
        return self.__caller

    def getExecutorIp(self):
        return self.__executorIP

    def getAction(self):
       return self.__action

    def getResponseStatus(self):
       return self.__responseStatus

    def getStartTime(self):
        return self.__startTime

    def getEndTime(self):
        return self.__endTime

    def getBytesTx(self):
        return self.__bytesTx

    def getBytesRx(self):
        return self.__bytesRx

    def getRequestId(self):
        return self.__requestId

    def getRequestName(self):
        return self.__requestName

    def getBwTx(self):
        return self.__bwTx

    def getBwRx(self):
        return self.__bwRx

    def getServiceName(self):
        return self.__serviceName


