#!/usr/bin/env python

from appJar import gui
import sys
import fileinput
from subprocess import Popen, call
from ttkthemes import ThemedStyle
from AutorunConfig import Autorun

# Add translations for all


# Button Events
def ButtonHandler(press):
    if press == "Exit":  # If user clicks Exit
        quit()

    elif press == "More Info":  # If user clicks More Info
        # Infobox showing info
        program.infoBox("More Information", "This program modifies a text file to change the clock speed of the processor.\nThe number shown on the slider marks the maximum clock speed of the CPU in MHz.\nIf the clock speed is low, the Raspberry Pi will draw less power with lower performance, if the clock speed is high, it will draw more power with more performance.\n\nNote: The default value is 1200MHz.")


def ApplySettings(press):
    battery_meter = program.getCheckBox("Show standalone battery meter")
    launch_welcome = program.getCheckBox("Launch the Solar Pi Welcome application at startup")
    clock_speed = program.getScale("slider")

    if battery_meter == True:
        pass

    Autorun(launch_welcome)  # Takes appropriate action for running Welcome at startup

    # Opens and modifies config.txt file
    for line in fileinput.input(["/boot/config.txt"], inplace=True):
        if line.strip().startswith("arm_freq="):  # Searches for "arm_freq = "
            line = "arm_freq=" + str(clock_speed) + "\n"  # Replaces line with clock speed selected
        sys.stdout.write(line)  # Writes back to file



    # After settings have been changed
    if program.yesNoBox("Restart", "Your Solar Pi needs to be restarted in order for these changes to take effect.\nWould you like to restart now?") == True:  # Message to user to restart RPi
        Popen("/usr/local/bin/Solar Pi/Solar Pi Applications/Python Applications/Reboot.sh")

def Update(press):
    if program.getCheckBox("Update Operating System & Installed Programs") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
    if program.getCheckBox("Update appJar") == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")



def ScaleChange(value):
    value = int(program.getScale("slider"))
    program.setLabel("scale", "Clock Speed: " + str(value) + "MHz")



with gui("Settings", useTtk=True) as program:
    program.ttkStyle = ThemedStyle(program.topLevel)
    program.ttkStyle.set_theme("plastik")
    #program.setPadding(5, 5)
    #program.setResizable(canResize=False)

    with program.labelFrame("Performance & Power", 0, 0):
        # Title

        program.setPadding(4, 4)

        program.addLabel("title", "Clock Speed Changer", colspan=2)
        program.setLabelSticky("title", "ew")

        program.addScale("slider", 1, 0)
        program.setScaleFunction("slider", ScaleChange)
        program.setScaleSticky("slider", "ew")

        program.addButton("More Info", ButtonHandler, 1, 1)

        program.addLabel("scale", "", 2, 0)
        program.setLabelSticky("scale", "ew")

        # Scale
        program.setScaleRange("slider", 600, 1200, curr=None)  # Changes scale range

        # Label
        program.addLabel("Info", "◄ Greater Battery Life       Performance ►", colspan=2)

        # Buttons
        program.addLabel("filler1", "")
        program.addCheckBox("Show standalone battery meter")
        program.setCheckBox("Show standalone battery meter", ticked=True)


    with program.labelFrame("Updates", 0, 1):
        program.setPadding(5, 5)
        program.addLabel("info3", "Note: This will only work\nwith an internet connection.")
        program.addCheckBox("Update Operating System & Installed Programs")
        program.addCheckBox("Update appJar")
        program.addButton("Update System", Update)


    with program.labelFrame("Startup", 1, 0):
        program.setPadding(5, 5)
        program.addCheckBox("Launch the Solar Pi Welcome application at startup")
        program.setCheckBox("Launch the Solar Pi Welcome application at startup", ticked=True)



    program.addButton("Apply", ApplySettings, 5, colspan=2)
