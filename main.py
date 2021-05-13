import time

from MainWorker import MainWorker

while True:
    print("SPOUT Main thread is running")
    MainWorker()
    # TODO instantiate here a MainWorker and run it with a join 
    time.sleep(10)