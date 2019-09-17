import matplotlib.pyplot as plt
import matplotlib.animation as f
import numpy as np
from src.parse_data import parse_planet_data
import src.constants as k


def get_animation_range(planets):
    return np.amax([np.linalg.norm(p.position) for p in planets])


def next_position(p):
    return p.position + (p.velocity * k.TIME_STEP) + \
           ((1.0/6.0 * k.TIME_STEP * k.TIME_STEP) * ((4.0 * p.acceleration) - p.previous_acceleration))


def next_velocity(p, next_acceleration):
    return p.velocity + ((1.0/6.0)*(2.0*next_acceleration + 5.0*p.acceleration - p.previous_acceleration) * k.TIME_STEP)


def normalise_vector(v):
    mag = np.linalg.norm(v)
    if mag == 0:
        return v
    return v/mag


def force_gravity(p, planets):
    force = 0
    for P in planets:
        if p != P:
            distance = np.linalg.norm(p.position - P.position)
            force_mag = (k.G * p.mass * P.mass) / distance**2
            direction_vector = normalise_vector(P.position - p.position)
            force += force_mag * direction_vector

    return force


def run_time_step(planets):
    # update positions of planets
    for p in planets:
        p.position = next_position(p)
    next_accelerations = [force_gravity(p, planets)/p.mass for p in planets]
    next_velocities = [next_velocity(p, next_accelerations[i]) for i, p in enumerate(planets)]
    # update the values for acceleration & velocity
    for i, p in enumerate(planets):
        p.velocity = next_velocities[i]
        p.previous_acceleration = p.acceleration
        p.acceleration = next_accelerations[i]


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

    # initialise accelerations for first time_step
    for p in planets:
        p.acceleration = force_gravity(p, planets)/p.mass
        p.previous_acceleration = p.acceleration

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
    animation = f.FuncAnimation(fig, move_planets, interval=1, fargs=(patches, planets))
    plt.show()

