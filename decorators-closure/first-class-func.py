def square(num):
    return num*num


f = square
res = square(5)

print(f)
print(res)
print(f(5))


numbers = range(1, 10)
for x in map(square, numbers):
    print(x, end=" ")
print()


def html_tag(tag):

    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text


print_h1 = html_tag("h1")
print_h1("Test Headline")
