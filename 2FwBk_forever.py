#!/usr/bin/python

import time
import maestro as m

s= m.Controller()

servo_izq=0
servo_dcho=1

while True:
	# 1. Arrancamos maquinas FW!!!
	s.setTarget(servo_izq,1)
	s.setTarget(servo_dcho,-1)
	
	time.sleep(3)
	
	# 2. Paramos maquinas!!!
	s.setTarget(servo_izq,0)
	s.setTarget(servo_dcho,0)
	
	# 3. Revertimos maquinas BW!!!
	s.setTarget(servo_izq,-1)
	s.setTarget(servo_dcho,1)

	time.sleep(3)
