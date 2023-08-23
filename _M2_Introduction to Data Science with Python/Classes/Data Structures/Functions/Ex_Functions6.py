# op = {}
def sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def show_result(a, b, function):
    # global op
    # op = function
    result = function(a, b)
    print(f'The result of the operation is = {result}')

show_result(10, 10, sum)
show_result(10, 10, subtract)
