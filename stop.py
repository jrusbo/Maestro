#!/usr/bin/python

import time
import maestro as m
s= m.Controller()

# Paro todos Servomotores (0-5)
s.setTarget(0,0)
s.setTarget(1,0)
s.setTarget(2,0)
s.setTarget(3,0)
s.setTarget(4,0)
s.setTarget(5,0)
