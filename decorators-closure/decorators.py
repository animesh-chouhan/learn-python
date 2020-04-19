# def decorator_function(*args):
#     def wrapper_function():
#         print("Display function ran")
#     return wrapper_function


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper was executed before {}".format(
            original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


def display():
    print("Display function ran")


@decorator_function
def display_fancy():
    print("Fancy Display function ran")


@decorator_function
def display_info(name, age):
    print("Display info function ran with arguments {} and {}".format(name, age))


decorated_display = decorator_function(display)
decorated_display()

display_fancy()

display_info("John", 28)
