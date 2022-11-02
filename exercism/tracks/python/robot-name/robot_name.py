import random
import string

GLOBAL_CACHE = set()

def generate_name():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(2)) + \
           ''.join(random.choice(string.digits) for _ in range(3))

def choose_name():
    if len(GLOBAL_CACHE) == 676000:  # 26 * 26 * 10 * 10 * 10
        raise RuntimeError('Namespace is full!')

    name = generate_name()
    
    while name in GLOBAL_CACHE:
        name = generate_name()
    GLOBAL_CACHE.add(name)
    return name

class Robot:
    name = ''

    def __init__(self):
        self.name = choose_name()
    
    def reset(self):
        self.name = choose_name()