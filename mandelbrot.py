# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 12:54:28 2020

@author: Dante de Lang (11014083) & Karim Semin (11285990)
"""

""" 
This file contains the Mandelbrot formula as mathmatically known. 
This function will be requested in other files in order to determine its area.
"""
def mandelbrot(real_nr, imag_nr, max_iter):
    c = complex(real_nr, imag_nr)
    z = 0.0j # define z as complex nr
    for iteration in range(max_iter):
        z = z * z + c
        if (z.real * z.real + z.imag * z.imag) >= 4:
            return iteration
    return max_iter
