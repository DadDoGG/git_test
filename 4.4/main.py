a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)
    inner_function()

enclosing_funcion()

a = "I am global variable!"

def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        global a
        print(a)

    inner_function()

enclosing_funcion()

def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        nonlocal a
        print(a)

    inner_function()

enclosing_funcion()