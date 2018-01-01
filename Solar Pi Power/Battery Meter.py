#!/usr/bin/env python

from appJar import gui

num = 0
def updateMeter():
    global num
    program.setMeter("battery", num)
    # program.setLabel("level", str(num)+"%")
    num += 1

def over(param):
    program.setTransparency(5)
def leave(param):
    program.setTransparency(100)

with gui() as program:
    program.hideTitleBar()
    program.setLocation(0, 570)
    program.setPadding(0, 0)
    program.addMeter("battery", 1, 2)
    program.setMeterFill("battery", "#13d323")
    program.setMeterOverFunction("battery", [over, leave])
    program.registerEvent(updateMeter)
    program.setPollTime(10000)