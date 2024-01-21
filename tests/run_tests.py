import os
import sys
import inspect
import unittest
import logging

logging.basicConfig(filename="testlog.log", level=logging.DEBUG,filemode='w')

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import constants
import helpers.visualizer
import helpers.formulas
import modals

class TestVisualizer(unittest.TestCase):
    
    def test_image_creator(self):
        logging.debug("Debugging image creator with hardcoded sample")
        sample_data = __import__("sample").data
        vis = helpers.visualizer.Visualizer(sample_data)
        print(vis.img.height)
        print(vis.img.width)

if __name__=='__main__':
    unittest.main()