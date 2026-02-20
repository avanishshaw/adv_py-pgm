# Threading - execution of tasks
# Multithreading - execution of many task at atime - concurrent execution

# Multiprocessing -

# Threading - imported

#Process - execution unit
#Threads - light weight unit inside the process

# Simple thread

import threading
import time

def task():
    print("Thread started")
    time.sleep(2)
    print("Thread ended")

t = threading.Thread(target = task)
t.start()
t.join()

print("Thread terminated")

# Multi Threading
