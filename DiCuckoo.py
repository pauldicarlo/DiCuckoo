#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Main.py
#  
#  Copyright 2017  Paul DiCarlo
#  
#  
#  
import pygame, sys, time
from ClockFace import ClockFace
from ClockHand import ClockHand
from PIL import Image # uses pillo

from pygame.locals import *
from datetime import datetime

# For a given clock hand (hrs/min/sec), rotate the hand to the 
# appropriate location on the clock face given the time for that
# hand.  If it is an hour or minute hand, there is a subUnits parameter
# which will allow the hand to incrementally move to the next location
# based on the % the clock hand with time units smaller is to reaching
# the 12 position on the face.
def rotateHand(theHand, timeUnits, subUnits):
	rotAngle = int(theHand.rotationAngle * timeUnits) + subUnits + 90
	curHand = pygame.transform.rotate(theHand.handSurface, rotAngle)
	x = theHand.clockFace.clock_center - curHand.get_width()/2
	y = theHand.clockFace.clock_center - curHand.get_height()/2
	theHand.clockFace.screen.blit(curHand, (x,y))

#     #
##   ##    ##       #    #    #
# # # #   #  #      #    ##   #
#  #  #  #    #     #    # #  #
#     #  ######     #    #  # #
#     #  #    #     #    #   ##
#     #  #    #     #    #    #
if __name__ == '__main__':
	clockFaceFile = "clockFace.png"
	handsSecondsFile = "secondHand.png"
	handsMinutesFile = "minuteHand.png"
	handsHoursFile = "hourHand.png"
	
	# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
	
	im = Image.open(clockFaceFile)
	dim_clock_x, dim_clock_y = im.size
	clock_center =  dim_clock_x/2 # we're hoping that it is square

	screen = pygame.display.set_mode((dim_clock_x, dim_clock_y), 0, 32)

	clockFace  = ClockFace(clockFaceFile, clock_center, screen)
	
	pygame.font.init()
	myfont1 = pygame.font.SysFont("Times", 24)
	myfont2 = pygame.font.SysFont("Times", 36)
	#myfont = pygame.font.Font("a_Allgidus.ttf", 24)
	

	
	secondHand = ClockHand(handsSecondsFile, - 6,  0, clockFace)
	minuteHand = ClockHand(handsMinutesFile, - 6, 10, clockFace)
	hourHand   = ClockHand(handsHoursFile,   -30,  2, clockFace)
		
	now = datetime.now()
	while True:
	
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				
		# no need to run the screen update than once per second...
		later = datetime.now()
		difference = (later - now).total_seconds()
		if (difference > 0):
			now = later
			second = now.second
			screen.blit(clockFace.faceSurface, (0,0))
			
			# render text
			label = myfont2.render("DiCuckoo", 110, (0,0,0))
			screen.blit(label, (clock_center - label.get_width()/2, clock_center/2-45))
			plug = myfont1.render("www.DiCarloAndSons.com", 100, (0,0,0))
			screen.blit(plug, (clock_center - plug.get_width()/2, clock_center/2))
			
			
			rotateHand(hourHand,   now.hour,   -(now.minute//hourHand.subRotationAngle))
			rotateHand(minuteHand, now.minute, -(now.second//minuteHand.subRotationAngle))
			rotateHand(secondHand, now.second, 0)

			
			pygame.display.update()
	


	
