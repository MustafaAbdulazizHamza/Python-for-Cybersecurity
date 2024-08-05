import concurrent.futures as cf
import time
start = time.perf_counter()
def do_something(seconds):
    for _ in range(seconds):
        print(f'Sleeps for {seconds} s')
    time.sleep(seconds)
    return 'Done'

with cf.ThreadPoolExecutor() as ex:
    results =  ex.map(do_something, [23,4,5,2,3,9])
    for result in results:
        print(result)
end = time.perf_counter()
print(f'Finishes in {round(end - start)} seconds')