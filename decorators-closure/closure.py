def outer_func():
    message = "Hello"

    def inner_func():
        print(message + " World")
        return "Executed!"

    return inner_func


f = outer_func()

print(f)
print(outer_func())
print(f())
print(outer_func()())
