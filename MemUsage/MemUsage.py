import time
import psutil

print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)