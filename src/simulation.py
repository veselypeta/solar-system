import matplotlib.pyplot as plt
import matplotlib.animation as f
import numpy as np
from src.parse_data import parse_planet_data
import src.constants as k


def get_animation_range(planets):
    return np.amax([np.linalg.norm(p.position) for p in planets])


def next_position(planet):
    pass


def run_time_step(planets):
    # calculate the next position
    next_positions = [next_position(p) for p in planets]


def move_planets(i, patches, planets):
    # run a time_step
    run_time_step(planets)
    for i in range(len(patches)):
        patches[i].center = (planets[i].position[0], planets[i].position[1])


def run_simulation():
    # Create a matplotlib plot
    # We need to use a module from matplotlib for funcanimation
    # We create a patch for each planet and then using funcanimation
    # we move them across the screen.
    planets = parse_planet_data('src/solar_data.csv')
    fig = plt.figure()
    ax = plt.axes()

    ax.axis('scaled')
    # set the range of the plot
    ani_range = get_animation_range(planets) * 1.5
    ax.set_xlim(-ani_range, ani_range)
    ax.set_ylim(-ani_range, ani_range)

    # create a patches list to hold all patches
    patches = []
    # add patches to the list as planets, with their positions as their centre
    radius_scale_factor = 30000
    for p in planets:
        c = plt.Circle((p.position[0], p.position[1]), p.radius * radius_scale_factor, color=p.colour)
        ax.add_patch(c)
        patches.append(c)

    # run the animation and show the plot
    animation = f.FuncAnimation(fig, move_planets, fargs=(patches, planets))
    plt.show()

# We also need to calculate the next position of a planet from the previous data.

# Data that we need
# Locations/mass of all planets including sun
# We then calculate the force acting on the planet using formulas
# From which we can calculate the acceleration of that planet.
