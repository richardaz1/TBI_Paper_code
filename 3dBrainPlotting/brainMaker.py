# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import os
from mayavi.core.api import Engine
from mayavi.sources.vtk_file_reader import VTKFileReader
from mayavi.modules.surface import Surface

vtkFile_l = '/Users/richad/bin/lh.vtk'
vtkFile_r = '/Users/richad/bin/rh.vtk'

# Create the MayaVi engine and start it.
engine = Engine()
engine.start()
#scene = engine.new_scene()

# Read in VTK file and add as source
surface1 = Surface()
reader1 = VTKFileReader()
reader1.initialize(vtkFile_l)
engine.add_source(reader1)
engine.add_filter(surface1, reader1)

surface2 = Surface()
reader2 = VTKFileReader()
reader2.initialize(vtkFile_r)
engine.add_source(reader2)
engine.add_filter(surface2, reader2)
#import networkx as nx
import numpy as np
#import pickle as pk
#import matplotlib.pyplot as plt
#import bct
from mayavi import mlab

figure = mlab.figure(1, bgcolor=(1.0, 1.0, 1.0))
figure.scene.disable_render = True

coordsTbi = np.load('/Users/richad/bin/TBI_coords.npy')
mycolors1 = np.ones(np.shape(coordsTbi)[0])*-1
coordsTbi = coordsTbi[np.isfinite(mycolors1), :]

coordsNoTbi = np.load('/Users/richad/bin/NoTBI_coords.npy')
mycolors2 = np.ones(np.shape(coordsNoTbi)[0])*-1
coordsNoTbi = coordsNoTbi[np.isfinite(mycolors2), :]
'''
stimCoords = np.load('/Users/richad/bin/stimCoords.npy')
stimEffects = np.load('/Users/richad/bin/stimEffects.npy')

pts1 = mlab.points3d(stimCoords[0:, 0], stimCoords[:, 1], stimCoords[:, 2],
                        stimEffects*-1, vmin=-1, vmax=1,
                        scale_factor=5,
                        scale_mode='none',
                        colormap='RdBu',
                        resolution=40)
'''
#Nodes

pts1 = mlab.points3d(coordsTbi[0:, 0], coordsTbi[:, 1], coordsTbi[:, 2],
                        mycolors1[np.isfinite(mycolors1)][:], vmin=-3, vmax=3,
                        scale_factor=2,
                        scale_mode='none',
                        color=(0,.6,.1),
                        resolution=40)

pts2 = mlab.points3d(coordsNoTbi[:, 0], coordsNoTbi[:, 1], coordsNoTbi[:, 2],
                    mycolors2[np.isfinite(mycolors2)][:], vmin=-3, vmax=3,
                    scale_factor=2,
                    scale_mode='none',
                    color=(.5,0,.5),
                    resolution=40)

'''
coordsROI = np.load('/Users/richad/bin/ROIcoords.npy')

coordsSyncTbi = np.load('/Users/richad/bin/tbi_syncCoords.npy')
coordsAsyncTbi = np.load('/Users/richad/bin/tbi_asyncCoords.npy')

coordsSyncTbi_uf = np.load('/Users/richad/bin/tbi_syncCoords_unFilt.npy')
coordsAsyncTbi_uf = np.load('/Users/richad/bin/tbi_asyncCoords_unFilt.npy')

coordsSyncMatch = np.load('/Users/richad/bin/match_syncCoords.npy')
coordsAsyncMatch = np.load('/Users/richad/bin/match_asyncCoords.npy')

coordsSyncMatch_uf = np.load('/Users/richad/bin/match_syncCoords_unFilt.npy')
coordsAsyncMatch_uf = np.load('/Users/richad/bin/match_asyncCoords_unFilt.npy')


pts1 = mlab.points3d(coordsROI[:, 0], coordsROI[:, 1], coordsROI[:, 2],vmin=-3, vmax=3,
                        scale_factor=3,
                        scale_mode='none',
                        color=(1,1,1),
                        resolution=40)

#for TBI
#line1 = mlab.plot3d(coordsSyncTbi_uf[:, 0], coordsSyncTbi_uf[:, 1], coordsSyncTbi_uf[:,2],line_width=1.0, tube_radius=0.5,color=(0.9,0.9,0.9))
line1a = mlab.plot3d(coordsSyncTbi[:, 0], coordsSyncTbi[:, 1], coordsSyncTbi[:,2],line_width=1.0, tube_radius=0.5,color=(1,0,0))

#line2 = mlab.plot3d(coordsAsyncTbi_uf[:, 0], coordsAsyncTbi_uf[:, 1], coordsAsyncTbi_uf[:,2],line_width=1.0, tube_radius=0.5,color=(0.9,0.9,0.9))
line2a = mlab.plot3d(coordsAsyncTbi[:, 0], coordsAsyncTbi[:, 1], coordsAsyncTbi[:,2],line_width=1.0, tube_radius=0.5,color=(0,0,1))

#for match
#line1 = mlab.plot3d(coordsSyncMatch_uf[:, 0], coordsSyncMatch_uf[:, 1], coordsSyncMatch_uf[:,2],line_width=1.0, tube_radius=0.3,color=(0.9,0.9,0.9))
line1a = mlab.plot3d(coordsSyncMatch[:, 0], coordsSyncMatch[:, 1], coordsSyncMatch[:,2],line_width=1.0, tube_radius=0.5,color=(1,0,0))

#line2 = mlab.plot3d(coordsAsyncMatch_uf[:, 0], coordsAsyncMatch_uf[:, 1], coordsAsyncMatch_uf[:,2],line_width=1.0, tube_radius=0.3,color=(0.9,0.9,0.9))
line2a = mlab.plot3d(coordsAsyncMatch[:, 0], coordsAsyncMatch[:, 1], coordsAsyncMatch[:,2],line_width=1.0, tube_radius=0.5,color=(0,0,1))
'''
#line1.actor.property.opacity = 0.075
#line2.actor.property.opacity = 0.075
figure.scene.disable_render = False

#Make things look pretty.
scene = engine.scenes[0]
scene.scene.background = (1.0, 1.0, 1.0)
surface = engine.scenes[0].children[0].children[0].children[0]
surface.actor.property.opacity = 0.2
surface = engine.scenes[0].children[1].children[0].children[0]
surface.actor.property.opacity = 0.2

mlab.show() # interactive window
