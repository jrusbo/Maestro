#!/usr/bin/python

import time
import maestro as m

s= m.Controller()

while True:
	# 1. Arrancamos maquinas FW!!!
	s.setTarget(0,1)
	s.setTarget(1,-1)
	
	time.sleep(3)
	
	# 2. Paramos maquinas!!!
	s.setTarget(0,0)
	s.setTarget(1,0)
	
	# 3. Revertimos maquinas BW!!!
	s.setTarget(0,-1)
	s.setTarget(1,1)

	time.sleep(3)
