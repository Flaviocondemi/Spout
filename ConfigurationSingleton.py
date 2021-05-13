from AppMonitorProxy import AppMonitorProxy
from ClusterMonitorProxy import ClusterMonitorProxy
from Target import Target
from MonitorProxy import MonitorProxy
from RaphtoryKafkaProxy import RaphtoryKafkaProxy

class ConfigurationSingleton(Target, MonitorProxy, RaphtoryKafkaProxy):

    __instance = None
    __monitors = None
    __targets = None
    __raphKafkaProxy = None

    def __init__(self):

        """ Virtually private constructor. """
        if ConfigurationSingleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            ConfigurationSingleton.__instance = self
            self.__monitors = set()
            self.__targets = set()
            self.__raphKafkaProxy = RaphtoryKafkaProxy().getInstance()

    def getInstance(self):
        if ConfigurationSingleton.__instance == None:
            ConfigurationSingleton()
        return ConfigurationSingleton.__instance

    def __fillData(self):
        self.__monitors.add(AppMonitorProxy("http://fake-app-generator:5000/metrics"))
        self.__monitors.add(ClusterMonitorProxy("http://fake-cluster-generator:5000/metrics"))
        return self.__monitors

    def __addTarget(self, targets):
        self.__targets = targets

    def update(self):
        print("Data updated")
        return self.__fillData()

    def getTargets(self):
        return self.__targets

    def getMonitors(self):
        return self.__monitors

    def getRaphtoryKafkaProxy(self):
        return self.__raphKafkaProxy