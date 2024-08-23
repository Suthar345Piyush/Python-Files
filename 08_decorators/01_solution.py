import time

def timer(func):
    def wrapper(*args ,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper




@timer  # it always go through the timer function when we call example_function(2)
def example_function(n):
    time.sleep(n)


example_function(2)