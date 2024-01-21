from modals import World
import constants
import logging,sys
import helpers.graph
import helpers.visualizer

G = constants.G
c = constants.c
POS_BOUNDS = constants.POS_BOUNDS
MASS_BOUNDS = constants.MASS_BOUNDS
PARTICLE_COUNT = constants.PARTICLE_COUNT
PROC_TICKS = constants.PROC_TICKS
COLLIDE_THRESHOLD = constants.COLLIDE_THRESHOLD
VISUALIZER_MODE = constants.VISUALIZER_MODE

logging.basicConfig(filename="log.log", level=logging.DEBUG,filemode='w')

if __name__ == "__main__":

    print("Running simulation...")
    simulation = World.World(G, c, COLLIDE_THRESHOLD, PARTICLE_COUNT)
    simulation.populate(POS_BOUNDS, MASS_BOUNDS)
    simulation.run(PROC_TICKS) # simulate for x ticks
    print("Simulation finished")
    
    if VISUALIZER_MODE == "graph":
        helpers.graph.graph_visualize(simulation.time, simulation.particle_count_per_tick, PROC_TICKS)

    if VISUALIZER_MODE == "visualizer":
        v = helpers.visualizer.Visualizer(simulation.time)
        v.visualize()
    
    else: # does both for debug purposes
        
        helpers.graph.graph_visualize(simulation.time, simulation.particle_count_per_tick, PROC_TICKS)
        v = helpers.visualizer.Visualizer(simulation.time)
        v.visualize()
