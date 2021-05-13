from threading import Thread
from AppMonitorProxy import  AppMonitorProxy
from AppRecord import AppRecord
from MonitorProxy import MonitorProxy
from NodeRecord import NodeRecord
from RaphtoryKafkaProxy import RaphtoryKafkaProxy
from ClusterMonitorProxy import ClusterMonitorProxy

class MainThread (Thread):

    __datamonitor = None
    __rkp = None

    def __init__(self, datamonitor, rkp):
        Thread.__init__(self)
        print ("Thread started")
        self.__datamonitor = datamonitor
        self.__rkp = rkp

    def __noneToEmptyStr(self, data):
        if data is None:
            return ""
        return data


    def run(self):

        if isinstance(self.__datamonitor, AppRecord):

            monitordata = self.__datamonitor
            print("AppMonitorProxy sent to thread")

            dataVertex = {'startTime':monitordata.getStartTime(),
                    'duration': monitordata.getEndTime() - monitordata.getStartTime(),
                    'responseStatus': monitordata.getResponseStatus(),
                    'endTime': monitordata.getEndTime(),
                    'rootId': monitordata.getRootId(),
                    'caller': monitordata.getCaller(),
                    'serviceName':monitordata.getServiceName(),
                    'requestId':monitordata.getRequestId(),
                    'action': monitordata.getAction(),
                    'executorIP': monitordata.getExecutorIp(),
                    'appId': monitordata.getAppId(),
                    'requestName': monitordata.getRequestName(),
                     type: "service"
                    }

            dataEdge = {'requestId': monitordata.getRequestId(),
                     'rootId': monitordata.getRootId(),
                     'caller': monitordata.getCaller(),
                     'serviceName': monitordata.getServiceName(),
                     'bytesTx': monitordata.getBytesTx(),
                     'bytesRx': monitordata.getBytesRx(),
                     'bandwidthTx': monitordata.getBwRx(),
                     'appId': monitordata.getAppId(),
                     'reqestName': monitordata.getRequestName(),
                      type: "service"
                    }

            self.__rkp.addVertex(self.__noneToEmptyStr(monitordata.getAppId()) + self.__noneToEmptyStr(monitordata.getRequestName())
                                 + self.__noneToEmptyStr(monitordata.getServiceName()),
                                 monitordata.getRequestId(), dataVertex)

            self.__rkp.addEdge(self.__noneToEmptyStr(monitordata.getAppId()) + self.__noneToEmptyStr(monitordata.getRequestName())
                               + self.__noneToEmptyStr(monitordata.getCaller()),
                               self.__noneToEmptyStr(monitordata.getAppId()) + self.__noneToEmptyStr(monitordata.getRequestName())
                               + self.__noneToEmptyStr(monitordata.getServiceName()),
                               monitordata.getRequestId(), dataEdge)

            self.__rkp.addEdge(self.__noneToEmptyStr(monitordata.getAppId()) + self.__noneToEmptyStr(monitordata.getRequestName())
                               + self.__noneToEmptyStr(monitordata.getServiceName()),
                               monitordata.getServiceName(), monitordata.getRequestId(),
                               {type: "path2appLayer"})

            self.__rkp.addEdge(self.__noneToEmptyStr(monitordata.getAppId()) + self.__noneToEmptyStr(monitordata.getRequestName())
                               + self.__noneToEmptyStr(monitordata.getServiceName()),
                               monitordata.getExecutorIp(), monitordata.getRequestId(), {type: "path2clusterLayer"})

            self.__rkp.addEdge(self.__noneToEmptyStr(monitordata.getAppId()) + self.__noneToEmptyStr(monitordata.getServiceName()),
                               monitordata.getExecutorIp(),
                               monitordata.getRequestId(), {type: "service2clusterLayer"})



        elif isinstance(self.__datamonitor, NodeRecord):

            monitordata = self.__datamonitor
            print("ClusterMonitorProxy sent to thread")

            dataVertex = {'cpuUsage': monitordata.getCpuUsage(),
                     'ramUsage': monitordata.getRamUsage(),
                     'loadFactor': monitordata.getLoadFactor(),
                     'bytesTx': monitordata.getBytesTx(),
                     'bytesRx': monitordata.getBytesRx(),
                     'bandwidthRx': monitordata.getBandwidthRx(),
                     'bandwidthTx': monitordata.getBandwidthTx(),
                     }

            self.__rkp.addVertex(monitordata.getHostname(), monitordata.getTime(), dataVertex)




