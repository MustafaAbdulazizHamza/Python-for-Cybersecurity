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
thread0 = threading.Thread(target=fetch_square, args=(3,))
thread1 = threading.Thread(target=fetch_square, args=(7,))
thread2 = threading.Thread(target=fetch_square, args=(10,))
thread0.start()
thread1.start()
thread2.start()
thread0.join()
thread1.join()
thread2.join()
end_time = time.perf_counter() 
print(f"Finished in {round(end_time-start_time)}")