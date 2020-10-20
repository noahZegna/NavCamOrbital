#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 23:57:51 2020
@author: noahzr
"""

# locate NavCam DEMs in orbital DEM and save NavCam orbital region 


import rasterio
import numpy as np


# NavCam DEM mosaic 
NavCam_sol = 'NC_2602'
NC_mosaic = rasterio.open('/Users/noahzr/Desktop/sol02602/mosaics/N_L000_2602_XYZ077ORR_S_2954_45RNGM1.TIF')

# orbital products
orbital_DEM = "/Users/noahzr/Desktop/TerrainCharacterization/OrbitalData/MSLGaleCraterOrbitalData/MSL_Gale_DEM_Mosaic_1m_v3.tif"
#orthoimage = "/Users/noahzr/Desktop/TerrainCharacterization/OrbitalData/MSLGaleCraterOrbitalData/MSL_Gale_Orthophoto_Mosaic_25cm_v3.tif"

# corner coordinates of NavCam DEM
xcoord = np.array([NC_mosaic.bounds.left, NC_mosaic.bounds.right])
ycoord = np.array([NC_mosaic.bounds.top, NC_mosaic.bounds.bottom])


# MSL orbital DEM
src_DEM = rasterio.open(orbital_DEM)
#src_orthoim = rasterio.open(orthoimage)

# row and cols of the corners of the NavCam DEM in the orbital DEM and orthoimage raster array 
rows_DEM, cols_DEM = rasterio.transform.rowcol(src_DEM.transform, xcoord, ycoord)
#rows_orthoim, cols_orthoim = rasterio.transform.rowcol(src_orthoim.transform, xcoord, ycoord)

# window size for orbital DEM is set to 701 cells, add half the window size to the edges of the orbital NC region to later run geomorphon code
window_size = 701


# Rectangle region enclosing NavCam region 
orbital_DEM_NC_region = src_DEM.read(1)[ int(rows_DEM[0]-(window_size-1)/2) : int(rows_DEM[1]+(window_size+1)/2), int(cols_DEM[0]-(window_size-1)/2) : int(cols_DEM[1]+(window_size+1)/2) ]
#orthoimage_NC_region = src_orthoim.read(1)[ int(rows_orthoim[0]-(window_size-1)/2) : int(rows_orthoim[1]+(window_size+1)/2), int(cols_orthoim[0]-(window_size-1)/2) : int(cols_orthoim[1]+(window_size+1)/2) ]

np.save(NavCam_sol + '_orbital_DEM_region', orbital_DEM_NC_region)
#np.save(NavCam_sol + '_orthoimage_region', orthoimage_NC_region)
