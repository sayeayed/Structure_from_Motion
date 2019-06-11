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

class myBundle():
    '''Bundle adjustment object'''
    def _init_(self):
        '''Assuming we have the point correspondences from a Bundler .out file, we parse the relevant data
        into this object for easy manipulation:   
        - camera data/parameters (focal and distortion coefficients, rotation matrix, translation vector)
        - 3D points
        - corresponding 2D image points
        - number of cameras chosen for reconstruction from the dataset
        - total number of views/observations from the cameras
        - indices matching the 2D points to corresponding 3D points and camera parameters'''
        self.camera_data = np.array([], dtype = float)
        self.points_3d = None
        self.xp = np.array([], dtype = float)
        self.yp = np.array([], dtype = float)
        self.total_num_views = 0
        self.num_cameras = 0
        self.total_num_cameras = 0
        self.total_num_points = 0
        self.camera_index = np.array([], dtype = int)
        self.point_index = np.array([], dtype = int)
        
    def parseDataset(self, outFile, numChosen):
        '''Parse data from .out file (result of Bundler). Inputs are <outFile>: path to .out file, and <numChosen>: userdefined number
        of cameras to analyze'''
        
        chosenImages = range(numChosen)
        self.num_cameras = numChosen
        num_line_holds = 0
        
        try:
            with open(outFile) as fp:
                print('Parsing data file...')
                line0 = fp.readline() #read line 0 (the title)
                self.total_num_cameras, self.total_num_points = map(int, fp.readline().strip('\n').split(' ')) #read line 1
                
                self.points_3d = np.empty([total_num_points,3], dtype = float)
                
                if numChosen > total_num_cameras:
                    print('The range of cameras you have chosen exceeds (or is equal to) the limit of cameras available. The total number of cameras available, {}, will be used instead'.format(total_num_cameras))
                    # add feature to handle this case in memory-efficient way

                # extract camera parameters, starts reading on line 2
                for i in range(total_num_cameras):
                    if chosenImages.count(i) == 1:
                        c = 5
                        if len(self.camera_data) == 0:
                            self.camera_data = np.array(fp.readline().strip('\n').split(' '),dtype = float)
                            c = 4
                        for j in range(c):
                            self.camera_data = np.vstack([camera_data,np.array(fp.readline().strip('\n').split(' '),dtype = float)]) #reads 5 lines
                    else:
                        for k in range(5):
                            line_hold = fp.readline()
                            num_line_holds += 1

                # extract point correspondences of outputted 3D points, starts reading on line 2+num_cameras*5
                for i in range(total_num_points):
                    self.points_3d[i] =  np.array(fp.readline().strip('\n').split(' '),dtype = float) #read 3D coordinates
                    line = np.array(fp.readline().strip('\n').split(' '),dtype = float) #read view list
                    num_views = int(line[0])
                    for j in range(num_views):
                        cameraID = int(line[j*4+1])
            #             num_views_per_point = 0
                        if chosenImages.count(cameraID) == 1: #does camera match chosen images?
            #                 num_views_per_point += 1
                            x = line[j*4+3]
                            y = line[j*4+4]
                            self.camera_index = np.append(camera_index,cameraID)
                            self.point_index = np.append(point_index,i)
                            self.xp = np.append(xp,x)
                            self.yp = np.append(yp,y)
                            self.total_num_views += 1
                print('Data parsing successsful')
        except:
            print('Data parsing unsuccessful. Check data file format')
            print('Check the following numbers and vector lengths...:')
            print('  total_num_views:',self.total_num_views)
            unique_points = list(set(self.point_index))
            print('  num_unique_points:',len(unique_points))
            unique_cameras = list(set(camera_index))
            print('  num_uniqe_cameras:',len(unique_cameras))
            print('  total_num_cameras: ',self.total_num_cameras)
            print('  total_num_points: ', self.total_num_points)
            print('  number of cameras chosen: ', numChosen)
            print('  length of camera_index: ',len(self.camera_index))
            print('  length of point_index: ',len(self.point_index))
            print('  length of xp(/yp): ',len(self.xp))
            print('  total_num_views: ', self.total_num_views)
            print('  Final iteration in points parsing loop: ',i)

        if ((len(self.camera_index)==len(self.point_index)) and (len(self.point_index) == len(self.xp)) 
            and (len(self.xp)==len(self.yp)) and (len(self.yp)==self.total_num_views)):
            print('Vector lengths match')
            print('-Numbers of interest-')
            unique_points = list(set(self.point_index))
            print('  num_unique_points: ',len(unique_points))
            unique_cameras = list(set(self.camera_index))
            print('  num_uniqe_cameras: ',len(unique_cameras))
            print('  number of cameras chosen: ', numChosen)
            num_points = len(unique_points)
            print('  total_num_views: ', self.total_num_views)
        else:
            print('Data parsing unsuccessful. Check data file format. Number of views and points do not match')

def triangulateFun():
    '''Find the 3D points in global coordinates using a pair of camera
    poses and point correspondences'''

def reconstructScatterFun():
    '''Generate a simple 3D scatter plot'''

def reconstructPLYFun():
    '''Generate a PLY file, using plyfile, to be opened in MeshLab or Blender'''
    
def reconstructPCDFun():
    '''Generate a coloured point cloud PCD, using pypcd'''