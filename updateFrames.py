#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:57:15 2021

@author: ruben
"""


import numpy as np
import h5py

framelist = np.array([np.arange(798500, 803000, 500)])

with h5py.File("state.hdf5", 'a') as state:
    print(state['frames'][()])
    del state['frames']
    state.create_dataset('frames', data=framelist)
    print(state['frames'][()])
    