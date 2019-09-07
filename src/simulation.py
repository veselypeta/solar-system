import matplotlib.pyplot as plt
import matplotlib.animation as f
import sys
from src.parse_data import parse_planet_data

def get_animation_range():
    return 1

def move_planets():
    pass

def run_simulation():
    # Create a matplotlib plot
    # We need to use a module from matplotlib for funcanimation
    # We create a patch for each planet and then using funcanimation
    # we move them across the screen.
    fig = plt.figure()
    ax = plt.axes()

    ax.axis('scaled')
    # set the range of the plot
    range = get_animation_range() * 1.5
    ax.set_xlim(-range, range)
    ax.set_ylim(-range, range)

    # create a patches list to hold all patches
    patches = []
    # add patches to the list as planets, with their positions as their centre
    radius_scale_factor = 30000
    planets = parse_planet_data('src/solar_data.csv')
    for p in planets:
        c = plt.Circle((p.position[0], p.position[1]), p.radius * radius_scale_factor, color=p.colour)
        ax.add_patch(c)
        patches.append(c)

    # run the animation and show the plot
    animation = f.FuncAnimation(fig, move_planets, fargs=(patches,))
    plt.show()

# We also need to calculate the next position of a planet from the previous data.

# Data that we need
# Locations/mass of all planets including sun
# We then calculate the force acting on the planet using formulas
# From which we can calculate the acceleration of that planet.
