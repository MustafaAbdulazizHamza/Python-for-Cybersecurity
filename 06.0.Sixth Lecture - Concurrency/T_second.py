import threading
import time
start_time = time.perf_counter()
def network_request(number):
    time.sleep(1.0)
    return {"success": True, "result": number ** 2}
def fetch_square(number):
    response = network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))
threads = []
for i in [3,7,10]:
    t = threading.Thread(target=fetch_square, args=(i,))
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
end_time = time.perf_counter()
print(f"Finished in {round(end_time-start_time)}")