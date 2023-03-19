prev_result = None

def call_once(func):

    def wrapper(*args, **kwargs):
        global prev_result
        if prev_result == None:
            prev_result = func(*args, **kwargs)
            return prev_result
    return wrapper



@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
print(sum_of_numbers(13, 42))
