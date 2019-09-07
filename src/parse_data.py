import csv
import numpy as np
from src.Planet import Planet

def parse_planet_data(filename):
    with open(filename) as planetFile:
        csv_reader = csv.reader(planetFile)
        all_planets = []
        for planet in csv_reader:
            name = planet[0]
            mass = float(planet[1])
            position = np.array([float(planet[2]), float(planet[3])])
            velocity = np.array([float(planet[4]), float(planet[5])])
            radius = float(planet[6])
            colour = str(planet[7])
            p = Planet(name, mass, position, velocity, radius, colour)
            all_planets.append(p)