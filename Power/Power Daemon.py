#!/usr/bin/env python3

from time import sleep
import smbus
from appJar import gui
from SettingsRW import *

i2c = smbus.SMBus(1)
cache = [None, None]

def pwr_mode():  # Function for powering mode
    data = i2c.read_byte_data(0x69, 0x00)
    data = data & ~(1 << 7)
    if data == 1:
        return "C"
    elif data == 2:
        return "B"

def bat_level():  # Function for battery voltage
    data = i2c.read_word_data(0x69, 0x08)
    data = format(data, "02x")
    if pwr_mode() == "C":
        return (float(data) / 100) - 0.25
    elif pwr_mode() == "B":
        return (float(data) / 100) + 0.05

def bat_percent():
   volts = bat_level()
   percentage = ((volts-3.4)/0.75)*100
   return percentage

# Set variables
ignore = False
shown = False

while True:  # Repeat infinitely
    percentage = bat_percent()  # Fetch percentage
    mode = pwr_mode()  # Fetch power mode

    print(percentage, mode)
    
    if cache[0] != percentage or cache[1] != mode or ignore == True:  # If battery data has changed or previous reading was incorrect
        if percentage > 101 and mode == "B":
            ignore = True  # Triggers if reading is incorrect
        else:
            with open("../ramdisk/power", "w") as file:  # Opens power file on ramdisk and writes battery data
                file.write(str(percentage) + "," + mode)
            ignore = False

        cache = [percentage, mode]  # Add battery data to cache

    if percentage < 15 and shown == False:  # Triggered if battery level is low
        shown = True
        with gui("Low battery", useTtk=True) as app:  # GUI for low battery warning
            app.setResizable(False)

            theme = getSetting("theme")
            lang = getSetting("language")

            if theme == "Solar Pi":
                # Configures and sets custom theme
                app.setTtkTheme("plastik")
                app.setTtkTheme("clam")
                app.ttkStyle.configure("TButton", background="#324581", foreground="white", bordercolor="#687396")
                app.ttkStyle.map("TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])
            else:
                app.setTtkTheme(theme)  # Sets ttk theme

            app.setFont(family="piboto")
            app.ttkStyle.configure(".", font=("piboto"))

            # app.hideTitleBar()
            app.setPadding(10, 10)

            app.addImage("warning", "../Resources/Images/warning icon.gif")  # Warning icon
            app.zoomImage("warning", -4)
            app.addLabel("label", "The battery of your Solar Pi is running low.\nPlease save your work, as your Solar Pi will shut down soon.", 0, 1)
            app.addButton("Close", app.stop, colspan=2)  # Button to close GUI

            if theme != "black":
                app.setBg("white")  # Configures options for themes
                app.ttkStyle.configure(".", background="white", foreground="black")

            app.changeLanguage(lang)


    sleep(4)  # Wait 4 secs before polling battery again
