import requests as r 
import concurrent

def multi_threaded_req(req_func, iterable):

    with concurrent.futures.ThreadPoolExecutor() as executor: 
        res = [executor.submit(req_func, req_item) for req_item in iterable]
        concurrent.futures.wait(res) 
    
    return res 