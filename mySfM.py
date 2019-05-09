# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:51:59 2019

@author: Ayeda Sayeed

Package to implement Structure from Motion techniques to reconstruct a 
3D object from a series of 2D images

*not yet complete*

"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MatchedPoint():
    '''Assuming we have the point correspondences, we input them
    into this object for easy manipulation'''
    def _init_(self):
        '''...'''

def triangulateFun():
    '''Find the 3D points in global coordinates using a pair of camera
    poses and point correspondences'''

def reconstructScatterFun():
    '''Generate a simple 3D scatter plot'''

def reconstructPLYFun():
    '''Generate a PLY file, using plyfile, to be opened in MeshLab or Blender'''
    
def reconstructPCDFun():
    '''Generate a coloured point cloud PCD, using pypcd'''