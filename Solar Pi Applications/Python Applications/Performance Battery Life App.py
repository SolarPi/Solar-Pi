#!/usr/bin/env python3

# Import modules
from appJar import *
import os
import sys
import fileinput
from subprocess import Popen

# Button Events
def ButtonHandler(press):
    if press == "Exit":  # If user clicks Exit
        quit()

    elif press == "More Info":  # If user clicks More Info
        # Infobox showing info
        program.infoBox("More Information", "This program modifies a text file to change the clock speed of the processor.\nThe number shown on the slider marks the maximum clock speed of the CPU in MHz.\nIf the clock speed is low, the Raspberry Pi will draw less power with lower performance, if the clock speed is high, it will draw more power with more performance.\n\nNote: The default value is 1200.")

    elif press == "Apply":  # If user clicks Apply
        data = str(program.getScale("Drag the slider"))  # Fetches number on slider

        # Opens and modifies config.txt file
        for line in fileinput.input(["/boot/config.txt"], inplace=True):
            if line.strip().startswith("arm_freq="):  # Searches for "arm_freq = "
                line = "arm_freq=" + data + "\n"  # Replaces line with clock speed selected
            sys.stdout.write(line)  # Writes back to file

        if program.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?") == True: # Message to user to restart RPi
            Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/Reboot.sh")


# GUI
program = gui("Performance to Battery Life Selector", "400x200")
program.setBg("white")
program.setResizable(canResize=False)

# Widgets

# Title
program.addImage("image", "/usr/local/bin/Solar Pi/Resources/Images/Solar Pi text.gif")
program.zoomImage("image", -50)
program.addLabel("title", "Performance to Battery Life Selector")

# Scale
program.addScale("Drag the slider")  # Adds scale
program.setScaleRange("Drag the slider", 600, 1200, curr=None)  # Changes scale range
program.showScaleIntervals("Drag the slider", 100)  # Changes scale intervals
program.setScaleIncrement("Drag the slider", 50)  # Changes scale increment
program.showScaleValue("Drag the slider", show=True)  # Shows value of slider
program.setScale("Drag the slider", 900, callFunction=False)  # When application opens, slider is set to 900

# Label
program.addLabel("Info", "◄ Greater Battery Life          Performance ►")

# Buttons
program.addButtons(["Apply", "More Info", "Exit"], ButtonHandler)

# Starts program
program.go()
