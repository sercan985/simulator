from PIL import Image, ImageDraw
import constants
import random
from helpers.formulas import Formulas
import os

if not os.path.isdir("output"):
    print("Output folder created")
    os.mkdir("output")
"""
Image: Pos-Time graph
Image width: time
Image height: number of particles multiplied by max mass
Ellipse: particle
Ellipse size: mass
Ellipse colour: random for now i want to make every particle consistent in color 
Ellipse position: position

"""

def get_random_colour(a=255):
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255), a)

def determine_extremities(time):
    all_positions_at_all_times = [i[0] for t in time for i in t]
    return max(all_positions_at_all_times), min(all_positions_at_all_times)

def create_image_from_time(time,time_column_size,miny,maxy):
    
    size_x = len(time) * time_column_size
    #size_y = len(time[0])

    # The issue is that the bounds of the universe is not clearly defined, and clearly not all particles take up exactly one pixel.
    # I will implement something to determine the bounds based on the uppermost point a particle has ever reached and vice versa
    # Then remap the position values so that they are in the range
    size_y = abs(maxy - miny) # absolute justincase :)

    size = (round(size_x), round(size_y))

    img = Image.new("RGBA", size, constants.VISUALIZER_COLOR_EMPTY)
    return img

"""
Size means diameter not radius
"""
def determine_bounds_by_center_and_size(pos, size):
    center_x = pos[0]
    center_y = pos[1]
    bound1 = (center_x - size/2, center_y - size/2)
    bound2 = (center_x + size/2, center_y + size/2)
    return [bound1, bound2]


class Visualizer:

    def __init__(self, time):
        self.time = time
        self.time_column_size = constants.MASS_BOUNDS[-1]
        self.miny, self.maxy = determine_extremities(time)
        self.img = create_image_from_time(time, self.time_column_size,self.miny,self.maxy)
        self.imgdraw = self.create_draw_obj()
        self.mass_multiplier = constants.VISUALIZER_MASS_MULTIPLIER
        self.velocity_multiplier = constants.VISUALIZER_VELOCITY_MULTIPLIER
        self.position_multiplier = constants.VISUALIZER_POSITION_MULTIPLIER
        self.formulas = Formulas(None, None)
        self.particle_colours = []
        for p in range(len(time[0])):
            self.particle_colours.append(get_random_colour())
        
    def create_draw_obj(self):
       return ImageDraw.Draw(self.img)

    def draw_particle(self, particle, point_in_time, particle_id):
        ellipse_size = particle[2] * self.mass_multiplier
        ellipse_colour = self.particle_colours[particle_id]

        #aforementioned remapping is done here
        ellipse_pos = (point_in_time * self.time_column_size, self.formulas.remap(particle[0], self.miny, self.maxy, 0, self.img.size[1]))

        bounds = determine_bounds_by_center_and_size(ellipse_pos, ellipse_size)
        self.imgdraw.ellipse(bounds, fill=ellipse_colour, outline=ellipse_colour)

    def save_image(self):
        self.img.save(constants.VISUALIZER_SAVE_FILE_NAME, format="PNG")
        print(f"Visualization saved at {os.path.join(os.getcwd(), 'output', constants.VISUALIZER_SAVE_FILE_NAME)}")

    def visualize(self):
        img = self.img
        for t in range(len(self.time)):
            for idi, i in enumerate(self.time[t]):
                self.draw_particle(i, t+1, idi) #range starts from 0 so we add 1
        self.save_image()
        
    

