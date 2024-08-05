import concurrent.futures as cf
import time
start = time.perf_counter()
def do_something(seconds):
    for _ in range(seconds):
        print(f'Sleeps for {seconds} s')
    time.sleep(seconds)
    return 'Done'

with cf.ThreadPoolExecutor() as exe:
    result = [exe.submit(do_something, i) for i in [23,4,5,2,3,9]]
    for f in cf.as_completed(result):
        print(f.result())
        
end = time.perf_counter()
print(f'Finishes in {round(end - start)} seconds')