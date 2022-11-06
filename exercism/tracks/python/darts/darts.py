import math

distance_from_centre = lambda x, y: math.sqrt(x**2 + y**2)

def score(x, y):
    circonference_to_radius = {0: 10, 5: 5, 10: 1}
    d_f_c = 0 if distance_from_centre(x,y) <= 1 else distance_from_centre(x,y)

    return circonference_to_radius \
            [min([i for i in circonference_to_radius.keys() if i >= d_f_c])] \
            if d_f_c <= 10 else 0