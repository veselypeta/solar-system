import csv
import numpy as np
from src.Planet import Planet


def parse_planet_data(filename):
    with open(filename) as planetFile:
        csv_reader = csv.reader(planetFile)
        all_planets = []
        for planet in csv_reader:
            name = planet[0]
            mass = np.float64(planet[1])
            position = np.array([np.float64(planet[2]), np.float64(planet[3])])
            velocity = np.array([np.float64(planet[4]), np.float64(planet[5])])
            radius = np.float64(planet[6])
            colour = str(planet[7])
            p = Planet(name, mass, position, velocity, radius, colour)
            all_planets.append(p)

    return all_planets
