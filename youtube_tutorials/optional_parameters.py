def add_number(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)

add_number(5, 10, 25, 3365)