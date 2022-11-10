def check(sides):
    if len(sides) != 3:
        return False
    if not all([i > 0 for i in sides]):
        return False
    tmp = sides[:]
    ipo = max(tmp)
    tmp.remove(ipo)
    return (ipo - tmp[0] - tmp[1]) <= 0

def type_tri(sides):
    if check(sides):
        x = set(sides)
        return (len(x) == 1 and 'equilater') or (len(x) == 3 and 'scalene') or 'isosceles'

def equilateral(sides):
    return type_tri(sides) == 'equilater'

def isosceles(sides):
    return type_tri(sides) in ['isosceles', 'equilater']

def scalene(sides):
    return type_tri(sides) == 'scalene'
