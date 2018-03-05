from appJar import gui
from subprocess import Popen, call
from AutorunConfig import Autorun
from sys import exit
from ttkthemes import ThemedStyle

app = gui(useTtk=True)
app.ttkStyle = ThemedStyle(app.topLevel)
app.ttkStyle.set_theme("plastik")

#app.addLabel("l1", "Themed tkinter!")

app.setPadding(3, 3)
# app.addImage("logo1", "E:\\1Home\\Main\\School\\Homework\\Year 10\\Solar Pi NEW\\Solar Pi Applications & Resources\\Applications\\Python Start Screen\\Solar Pi text.gif")
# #app.addImage("logo1", "/usr/local/bin/Solar Pi/Resources/Images/Solar Pi text.gif")
# app.zoomImage("logo1", -45)

def MenuHandler():
    pass

def ButtonHandler():
    pass

def ButtonHandler(press):
    tab_selected = app.getTabbedFrameSelectedTab("MainTabs")  # Fetches the current tab

    if press == "Exit" or press == "Exit3" or press == "Exit2" or press == "Exit4":  # Exits program
        exit()
    elif press == "About":  # Opens the About subwindow
        app.showSubWindow("About Solar Pi")
    elif press == "Close":  # Closes the About subwindow
        app.hideSubWindow("About Solar Pi")
    elif press == "Scratch":  # Launches Scratch
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
    elif press == "Python":  # Launches a Python IDE
        if app.yesNoBox("Python", "Would you like to use the Thonny Python IDE instead of the IDLE?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Thonny Launcher.sh")
        else:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")
    elif press == "Java":  # Launches BlueJ
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/BlueJ Launcher.sh")
    elif press == "Change Advanced Settings":  # Launches RPi settings window
        Popen("/usr/bin/rc_gui")


def MenuHandler(press):
    if press == "Shutdown":
        if app.yesNoBox("Shutdown", "Are you sure that you want to shutdown your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Shutdown.sh")
    elif press == "Reboot":
        if app.yesNoBox("Reboot", "Are you sure that you want to reboot your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")
    elif press == "Leafpad":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Leafpad Launcher.sh")
    elif press == "Start Programming":
        Programming(None)
    elif press == "Python Guides":
        PythonGuides(None)
    elif press == "Performance to Battery Life":
        PerfBattery(None)
    elif press == "All Files":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/pcmanfm Launcher.sh")
    elif press == "Desktop":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Desktop Launcher.sh")
    elif press == "Documents":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Documents Launcher.sh")
    elif press == "Music":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Music Launcher.sh")
    elif press == "Pictures":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Pictures Launcher.sh")
    elif press == "Videos":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Videos Launcher.sh")

def PerfBattery(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Perf Battery Launcher.sh")
def Programming(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Programming Launcher.sh")
def PythonGuides(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Python Guide Launcher.sh")
def Update(press):
    box1 = app.getCheckBox("Update Operating System\n& Installed Programs")
    box2 = app.getCheckBox("Update appJar")
    if box1 == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
    if box2 == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")
def Settings(press):
    if app.getCheckBox("Launch this application at startup") == True:
        Autorun("add")
    else:
        Autorun("remove")

# Main Window
app.setPadding(3, 3)
#app.addImage("logo1", "E:\\1Home\\Main\\School\\Homework\\Year 10\\Solar Pi NEW\\Solar Pi Applications & Resources\\Applications\\Python Start Screen\\Solar Pi text.gif")
#app.addImage("logo1", "/usr/local/bin/Solar Pi/Resources/Images/Solar Pi text.gif")
#app.zoomImage("logo1", -45)
app.startNotebook("MainTabs", colspan=4)

# Menu bar
app.addMenuList("Power", ["Shutdown", "Reboot"], MenuHandler)
app.addMenuList("Applications", ["Leafpad", "Start Programming", "Performance to Battery Life"], MenuHandler)
app.addMenuList("Guides", ["Python Guides"], MenuHandler)
app.addMenuList("Files", ["All Files", "Desktop", "Documents", "Music", "Pictures", "Videos"], MenuHandler)


# Welcome Tab
app.startNote("Welcome!")
app.setPadding(10, 10)
app.addLabel("welcome", "Welcome to the")
app.getLabelWidget("welcome").config(font="50")
#app.addImage("logo", "Solar Pi logo.gif")
#app.zoomImage("logo", -2)

app.addLabel("label1", "Your Solar Pi is a solar powered Raspberry Pi based computer.\nStart by clicking one of the tabs above.  ^^^")
#app.addButtons(["About", "Exit"], ButtonHandler)

app.stopNote()

# Applications Tab
app.startNote("Applications")
app.startLabelFrame("Applications")
app.setSticky("ew")
app.setPadding(10, 10)
app.addLabel("applications_info", "Hover over the icons to see more information about each app.", colspan=2)

# Start Programming
app.startLabelFrame("Start Programming", 1, 0)
app.setPadding(10, 15)
#app.addImage("programming_icon", "Programming icon cropped.gif", 0, 0)
#app.zoomImage("programming_icon", -13)
#app.setImageTooltip("programming_icon", "This allows you to see and try the different options for programming.")
app.addButton("Start Programming", Programming, 0, 1)
app.stopLabelFrame()

# Performance to Battery Life
app.startLabelFrame("Performance to Battery Life Selector", 1, 1)
app.setPadding(10, 10)
##app.addImage("perf_icon", "speedometer1600.gif", 0, 0)
##app.zoomImage("perf_icon", -37)
##app.setImageTooltip("perf_icon", "This allows you to increase the performance or battery life of your Solar Pi.")
app.addButton("Performance to Battery Life", PerfBattery, 0, 1)
app.stopLabelFrame()

# IDEs
app.startLabelFrame("IDEs", 2, 0, colspan=2)
app.setPadding(10, 10)

app.startLabelFrame("Scratch", 1, 0)
app.setPadding(10, 10)
##app.addImage("scratch_logo2", "scratch logo.gif", 0, 0)
##app.zoomImage("scratch_logo2", -50)
##app.setImageTooltip("scratch_logo2", "The Scratch 2 IDE. Create Scratch programs and games with this.")
app.addButton("Scratch", ButtonHandler, 0, 1)
app.stopLabelFrame()

app.startLabelFrame("Python", 1, 1)
app.setPadding(10, 10)
##app.addImage("python_logo2", "Python icon.gif", 0, 0)
##app.zoomImage("python_logo2", -4)
##app.setImageTooltip("python_logo2", "The Python IDE. Write and run Python applications.")
app.addButton("Python", ButtonHandler, 0, 1)
app.stopLabelFrame()

app.startLabelFrame("Java", 1, 2)
app.setPadding(10, 10)
#app.addImage("java_logo", "java logo.gif", 0, 0)
##app.zoomImage("java_logo", -5)
##app.setImageTooltip("java_logo", "The BlueJ Java IDE. Create Java applications.")
app.addButton("Java", ButtonHandler, 0, 1)
app.stopLabelFrame()

app.stopLabelFrame()

app.stopLabelFrame()
app.stopNote()


# Guides & Tutorials Tab
app.startNote("Guides & Tutorials")
app.startLabelFrame("Guides & Tutorials")
app.setSticky("ew")
app.setPadding(10, 10)
app.addLabel("guides_info", "Hover over the icons to see more information about each guide/tutorial.", colspan=2)

# Python Guides
app.startLabelFrame("Python Guides & Tutorials")
app.setPadding(10, 10)
##app.addImage("python_logo", "Python icon.gif", 0, 0)
##app.zoomImage("python_logo", -4)
##app.setImageTooltip("python_logo", "A collection of tutorials and Python documentation to help you learn Python.")
app.addButton("Python Guides", PythonGuides, 0, 1)
app.stopLabelFrame()

# Scratch Tutorial
app.startLabelFrame("Scratch Tutorial", 1, 1)
app.setPadding(10, 10)
##app.addImage("scratch_logo", "scratch logo.gif", 0, 0)
##app.zoomImage("scratch_logo", -50)
##app.setImageTooltip("scratch_logo", "A beginner's tutorial on how to use Scratch.")
app.addButton("Scratch Tutorial", ButtonHandler, 0, 1)
app.stopLabelFrame()

app.stopLabelFrame()
app.stopNote()


# Settings Tab
app.startNote("Settings")
app.startLabelFrame("Settings")
app.setSticky("ew")
app.setPadding(10, 10)

app.startLabelFrame("General Settings", 0, 0)
app.setSticky("ew")
app.setPadding(10, 10)
app.addCheckBox("Launch this application at startup")
##app.setCheckBox("Launch this application at startup", ticked=True)
app.addButton("Change Advanced Settings", ButtonHandler)
app.addButton("Change Performance\n& Battery Life Settings", PerfBattery)
app.addButton("Apply Changes", Settings)
app.setButtonSticky("Apply Changes", "Both")
#app.setButtonBg("Apply Changes", "gray")
#app.setButtonFg("Apply Changes", "white")
app.stopLabelFrame()

app.startLabelFrame("Update", 0, 1)
app.setSticky("ew")
app.setPadding(10, 10)
app.addLabel("info3", "Note: This will only work\nwith an internet connection.")
app.addCheckBox("Update Operating System\n& Installed Programs")
app.addCheckBox("Update appJar")
app.addButton("Go", Update)
#app.setButtonBg("Go", "gray")
#app.setButtonFg("Go", "white")
app.stopLabelFrame()


app.stopLabelFrame()
app.stopNote()

app.stopNotebook()

app.addSplitMeter("battery", 1, 0)
app.setMeterFill("battery", ["light blue", "red"])
num = 0
def updateMeter():
    global num
    num += 1
    app.setMeter("battery", num, text=str(num)+"%")
    app.setLabel("level", str(num)+"%")

app.addLabel("battery", "Battery Remaining: ", 1, 1)
app.addLabel("level", "", 1, 2)
app.registerEvent(updateMeter)
app.setLabelAlign("level", "left")
#app.addButton("Battery", ButtonHandler, 1, 3)

app.go()
