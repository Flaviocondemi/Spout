import AppTarget
from AppRecord import AppRecord
from MonitorProxy import MonitorProxy
import random
import requests

class AppMonitorProxy(MonitorProxy):

    # target is the ip of prometheus
    def __init__(self, target):
        super().__init__(target)

    def getData(self):
        res = requests.get(self.getTarget())
        print(res)
        if res.status_code == 200:
            jres = res.json()
            jsonlist = []
            i = 0
            while i < len(jres):
                jsonlist.append(AppRecord(jres[i]["app_id"], jres[i]["values"]["bytes_rx"], jres[i]["root_id"],
                          jres[i]["caller"], jres[i]["executor_ip"], jres[i]["action"],
                          jres[i]["response_status"], jres[i]["values"]["start_time"],
                          jres[i]["values"]["end_time"], jres[i]["values"]["bytes_tx"],
                          jres[i]["request_id"], jres[i]["request_name"],
                          jres[i]["values"]["bw_tx"], jres[i]["values"]["bw_rx"],
                          jres[i]["service_name"]))
                i = i + 1
            return jsonlist
        return 0