import time
def Logging(func):
    def wrapper(*args, **kwargs):
        print("Start the execution")
        func(*args, **kwargs)
        print("Finished")
    return wrapper
# @Logging
def f():
    print("F in execution")
    time.sleep(2)

@Logging
def f1(st):
    print("F in execution. Waithing {}".format(st))
    time.sleep(st)
f1(4)