import time
def network_request(number):
    time.sleep(1.0)
    return {"success": True, "result": number ** 2}
def fetch_square(number):
    response = network_request(number)
    if response["success"]:
        print("Result is: {}".format(response["result"]))