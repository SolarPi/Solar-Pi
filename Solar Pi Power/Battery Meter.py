#!/usr/bin/env python

from appJar import gui

with gui() as program:
    num = 0


    def updateMeter():
        global num
        program.setMeter("battery", num)
        # program.setLabel("level", str(num)+"%")
        num += 1

    program.hideTitleBar()
    program.setLocation(0, 570)
    program.setPadding(0, 0)
    program.addMeter("battery", 1, 2)
    program.setMeterFill("battery", "#13d323")
    program.registerEvent(updateMeter)
    program.setPollTime(10000)