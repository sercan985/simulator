# Provides paramenters which will be used in the world simulation
import time

    

PROC_TICKS = 500 # amount of ticks to calculate
PARTICLE_COUNT = 100 # number of particles in total

G = 25 # gravitational constant

c = 100 # velocity limit
G = G * 10**(-6)

POS_BOUNDS = (-4096,4096) # random position bounds
MASS_BOUNDS = (1,50) # random mass bounds

COLLIDE_THRESHOLD = 10 # UNUSED minimum distance to collide

VISUALIZER_MODE = "visualizer" # "graph" or "visualizer" (visualizer is image renderer)
# VISUALIZER
VISUALIZER_COLOR_EMPTY = (255,255,255,0)

# It changes based on velocity now
# nvm made it random for visibility
# VISUALIZER_COLOR_FULL = (0,0,0,255)

VISUALIZER_DIMENSION_MULTIPLIER = 1
VISUALIZER_MASS_MULTIPLIER = 1
VISUALIZER_VELOCITY_MULTIPLIER = 1
VISUALIZER_POSITION_MULTIPLIER = 1

# not really a constant, though it is consistent in the sense that it is always the current timestamp in miliseconds
VISUALIZER_SAVE_FILE_NAME = f"output/{round(time.time() * 1000)}.png" 
