import math

def df_decarator(dx = 0.01):
	def func_deacarator(func, dx=0.01):
		def wrapper(x, *args, **kwargs):
			res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
			return res
		return wrapper
	return func_deacarator

@df_decarator(dx=0.0000001)
def sinus_df(x):
	return math.sin(x)

print(sinus_df(math.pi/3))


prev_result = None

def remember_result(func):

    def wrapper(*args, **kwargs):
        global prev_result
        print(f"Prev result = '{prev_result}'")
        prev_result = func(*args, **kwargs)
    return wrapper


@remember_result
def sum_list(*args, **kwargs):
	for i in args:
		if type(i) == int:
			result = 0
		else:
			result = ""
	for i in args:
		result += i
	print(f"Current result = '{result}'")
	return result

sum_list("a", "b")
sum_list("abc", "cde")
sum_list(1, 2, 3, 4)


