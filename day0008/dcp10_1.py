#Daily Coding Problem #10 [Medium]
#Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
import time
def schedule_job(f,n):
    time.sleep(0.001*n)
    f()

def sum_num(a,b):
    print(a+b)
    
schedule_job(sum_num(10,20),10000)
