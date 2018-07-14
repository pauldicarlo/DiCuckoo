#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  
#  Copyright 2017  Paul DiCarlo
#  
import pygame
from ClockFace import ClockFace

class ClockHand:
	
	def __init__(self, imageFileName, rotationAngle, subRotationAngle, clockFace):
		self.imageFileName = imageFileName
		self.subRotationAngle = subRotationAngle
		self.rotationAngle = rotationAngle
		self.clockFace = clockFace
		#self.screen = screen
		self.handSurface = pygame.image.load(imageFileName).convert_alpha()
		
		
	

