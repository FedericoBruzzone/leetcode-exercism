"""Solution to Ellen's Alien Game exercise."""

class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Amount of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    x_coordinate = 0
    y_coordinate = 0
    health = 0
    total_aliens_created = 0

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1
    
    def is_alive(self): 
        return self.health > 0

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
    
    def collision_detection(self, other_alien):
        # return self.x_coordinate == other_alien.x_coordinate and self.y_coordinate == other_alien.y_coordinate
        return None

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_positions):
    return list(map(lambda x: Alien(x[0], x[1]), alien_start_positions))