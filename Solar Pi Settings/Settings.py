#!/usr/bin/env python

from appJar import gui
import sys
import fileinput
from subprocess import Popen
from ttkthemes import ThemedStyle

# Add translations for all


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



def ScaleChange(value):
    value = int(program.getScale("slider"))
    program.setLabel("scale", value)



with gui("Settings", useTtk=True) as program:
    program.ttkStyle = ThemedStyle(program.topLevel)
    program.ttkStyle.set_theme("plastik")
    #program.setResizable(canResize=False)

    with program.labelFrame("Performance & Power", 0, 0):
        # Title
        program.addLabel("title", "Clock Speed Changer")

        program.addScale("slider")
        #program.setScaleLength("slider", 100)
        program.setStretch("both")
        program.setScaleFunction("slider", ScaleChange)
        program.addLabel("scale", "")
        # Scale
        #program.addScale("Drag the slider", colspan=2)  # Adds scale
        program.setScaleRange("slider", 600, 1200, curr=None)  # Changes scale range
        #program.showScaleIntervals("slider", 100)  # Changes scale intervals
        #program.setScaleIncrement("slider", 50)  # Changes scale increment
        #program.showScaleValue("slider", show=True)  # Shows value of slider
        #program.setScale("Drag the slider", 900, callFunction=False)  # When application opens, slider is set to 900

        # Label
        program.addLabel("Info", "◄ Greater Battery Life          Performance ►")

        # Buttons
        program.addButton("More Info", ButtonHandler)
        program.addCheckBox("Show standalone battery meter")


    with program.labelFrame("Startup", 0, 1):
        program.addCheckBox("Launch the Solar Pi Welcome application at startup")
        #program.setCheckBox("Launch the Solar Pi Welcome application at startup", ticked=True)

    with program.labelFrame("Updates", 1, 0):
        program.addButton("Update System", ButtonHandler)
