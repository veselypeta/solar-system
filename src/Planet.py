class Planet:
    def __init__(self, name, mass, position, velocity, radius, colour):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
        self.colour = colour
        self.acceleration = 0
        self.previous_acceleration = 0

