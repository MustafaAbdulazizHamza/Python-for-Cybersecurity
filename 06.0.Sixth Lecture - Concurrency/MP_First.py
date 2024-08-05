import time
import multiprocessing
start =time.perf_counter()
def Do_Something():
    print("Sleeping 1 second")
    time.sleep(1)
    print('Done')
end = time.perf_counter()
p1 = multiprocessing.Process(target=Do_Something)
p2 = multiprocessing.Process(target=Do_Something)
p3 = multiprocessing.Process(target=Do_Something)
p1.start()
p2.start()
p3.start()
p3.join()
p1.join()
p2.join()
print(f'{round(end-start)} seconds')
