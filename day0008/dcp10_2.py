#Daily Coding Problem #10 [Medium]
#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import threading
from time import sleep

class Scheduler:
    def __init__(self):
        pass
    
    def delay(self,f,n):
        def sleep_then_call(n):
            sleep(n/1000)
            f()
        t = threading.Thread(target=sleep_then_call, args=(n,))
        t.start()

def sum_num(a,b):
    print(a+b)

schd = Scheduler()
schd.delay(sum_num(10,20),10000)
