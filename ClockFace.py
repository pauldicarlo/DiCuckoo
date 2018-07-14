#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ClockFace.py
#  
#  Copyright 2017  Paul DiCarlo
#  
#  

import pygame

class ClockFace:	
	
	def __init__(self, imageFileName, clock_center, screen):
		self.imageFileName = imageFileName
		self.screen = screen
		self.faceSurface = pygame.image.load(imageFileName).convert()
		self.clock_center = clock_center
		
	

