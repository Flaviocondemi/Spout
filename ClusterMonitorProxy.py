from MonitorProxy import MonitorProxy
import random
from NodeRecord import NodeRecord
import requests
import json


class ClusterMonitorProxy(MonitorProxy):

    # target is the ip of prometheus
    def __init__(self, target):
        super().__init__(target)

    def getData(self):
        res = requests.get(self.getTarget())
        print(res)
        if res.status_code == 200:
            jres = res.json()
            jsonlist = []
            for item in jres[0]["net"]:
                jsonlist.append(NodeRecord(jres[0]["cpu_usage"], jres[0]["ram_usage"], jres[0]["load_factor"],
                              item["values"]["bytes_tx"], item["values"]["bytes_rx"],
                              item["values"]["bw_rx"], item["values"]["bw_tx"],
                              item["destination"], jres[0]["time"]))
                print(jres[0])
            return jsonlist
        return 0
