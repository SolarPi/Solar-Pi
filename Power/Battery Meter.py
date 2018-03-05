#!/usr/bin/env python

from appJar import gui
from time import sleep

num = 0
def updateMeter():
    global num
    program.setMeter("battery", num)
    # program.setLabel("level", str(num)+"%")
    num += 1

def over(param):
    program.hide()

def leave(param):
    sleep(1)
    program.show()

with gui() as program:
    program.hideTitleBar()
    program.setLocation(0, 573)
    program.setPadding(0, 0)
    program.setGuiPadding(0, 0)
    program.addMeter("battery", 1, 2)
    program.setMeterFill("battery", "#13d323")
    program.setMeterOverFunction("battery", [over, leave])
    program.registerEvent(updateMeter)
    program.setPollTime(10000)
