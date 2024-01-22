import time
import psutil

while True:
    print(psutil.cpu_percent())
    print(psutil.virtual_memory().percent)
    time.sleep(1)
    
#visualise values
def displayUsage(cpu_usage, mem_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar '' * int(cpu_percent * bars) + ' ' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)