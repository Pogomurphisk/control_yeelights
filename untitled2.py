# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:47:03 2018

@author: clayb
"""

import sched, datetime, time

def eat_cheese():
    print("I'm busy eating cheese")

s = sched.scheduler()
current_time = time.monotonic()
run_time = current_time + 4
print(run_time)
s.enterabs(run_time, 1, eat_cheese)
s.run()