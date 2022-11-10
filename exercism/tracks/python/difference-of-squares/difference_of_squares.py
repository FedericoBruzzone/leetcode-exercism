import functools

def square_of_sum(number):
    return functools.reduce(lambda x, y: x+y, range(number+1))**2

def sum_of_squares(number):
    return functools.reduce(lambda x,y: x+y, map(lambda x: x**2, range(number+1)))

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
