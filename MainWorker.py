from ConfigurationSingleton import  ConfigurationSingleton
from RaphtoryKafkaProxy import  RaphtoryKafkaProxy
from Target import Target
from MonitorProxy import  MonitorProxy
from MainThread import MainThread
import time

class MainWorker:

    def __init__(self):
        ConfigurationSingleton.getInstance(self).update()

        #infinite loop
        while True:
            for monitor in ConfigurationSingleton.getInstance(self).getMonitors():
                for data in monitor.getData():
                    MainThread(data, ConfigurationSingleton.getInstance(self).getRaphtoryKafkaProxy()).start()
            #sleep of 15 seconds
            time.sleep(15) # 15 seconds as required in issue #18 ==> DONE


