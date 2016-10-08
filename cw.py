#!/usr/bin/python

import time
import maestro as m
s= m.Controller()
s.setTarget(0,1)
s.setTarget(1,-1)

time.sleep(5)

s.setTarget(0,0)
s.setTarget(1,0)

