import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        ret = func(*args, **kwargs)
        end_time = time.perf_counter()
        print("Finished in ", round(end_time - start_time, 4), " second(s)")
        return ret
    return wrapper


@timer
def sleepy(sec):
    time.sleep(sec)


sleepy(2)
