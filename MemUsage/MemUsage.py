import time
import psutil

while True:
    print(psutil.cpu_percent())
    print(psutil.virtual_memory().percent)
    time.sleep(1)