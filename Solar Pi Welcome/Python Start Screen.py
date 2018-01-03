#!/usr/bin/env python
# Solar Pi Welcome

from appJar import gui
from subprocess import Popen, call
#from AutorunConfig import Autorun
from sys import exit
from SettingsGet import LaunchWelcome


with open("../Solar Pi Settings/Settings.ini", "r") as file:
    data = file.readlines()[0]
data = data.split(",")
theme = data[3]

program = gui("Solar Pi Welcome", useTtk=True)  # When switch to ttk, change to 650x375
program.setTtkTheme(theme)
program.ttkStyle.configure(".", background="white", foreground="black")
program.ttkStyle.configure("TLabelframe", background="white")

# program.ttkStyle = ThemedStyle(program.topLevel)
# program.ttkStyle.set_theme(theme)

#program.useTtk()

#program.setIcon("E:\\1Home\\Main\\School\\Homework\\Year 10\\Solar Pi NEW\\Solar Pi Applications & Resources\\Applications\\Python Start Screen\\Logo_NEW_2.gif")
#program.setIcon("/usr/local/bin/Solar Pi/Resources/Images/Logo_NEW_2.gif")

def ButtonHandler(press):
    #tab_selected = program.getTabbedFrameSelectedTab("MainTabs")  # Fetches the current tab

    if press == "Exit" or press == "Exit3" or press == "Exit2" or press == "Exit4":  # Exits program
        exit()
    elif press == "About":  # Opens the About subwindow
        program.showSubWindow("About Solar Pi")
    elif press == "Close":  # Closes the About subwindow
        program.hideSubWindow("About Solar Pi")
    elif press == "Scratch":  # Launches Scratch
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
    elif press == "Python":  # Launches a Python IDE
        if program.yesNoBox("Python", "Would you like to use the Thonny Python IDE instead of the IDLE?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Thonny Launcher.sh")
        else:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")
    elif press == "Java":  # Launches BlueJ
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/BlueJ Launcher.sh")
    elif press == "Change Advanced Settings":  # Launches RPi settings window
        Popen("/usr/bin/rc_gui")
    elif press == "Change\nLanguage":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")
    elif press == "Get Started":
        program.setNotebook("MainTabs", "Get Started")  # Set tab/note to Get Started
    elif press == "Charging":
        print("Charging")  # Set tab/note to Charging


def MenuHandler(press):
    if press == "Shutdown":
        if program.yesNoBox("Shutdown", "Are you sure that you want to shutdown your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Shutdown.sh")
    elif press == "Reboot":
        if program.yesNoBox("Reboot", "Are you sure that you want to reboot your Solar Pi now?") == True:
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

def ToolbarHandler(press):
    if press == "Off":
        Popen("/usr/bin/lxde-pi-shutdown-helper")
    elif press == "Settings":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Settings Launcher.sh")  # Call Settings menu
    elif press == "Files":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/pcmanfm Launcher.sh")
    elif press == "About":
        program.showSubWindow("About Solar Pi")
    elif press == "Help":
        # TODO: Fix docs launch
        Popen("../Resources/Launchers/Docs/welcome.sh")

def PerfBattery(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Perf Battery Launcher.sh")
def Programming(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Programming Launcher.sh")
def PythonGuides(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Python Guide Launcher.sh")
def Update(press):
    box1 = program.getCheckBox("Update Operating System & Installed Programs")
    box2 = program.getCheckBox("Update appJar")
    if box1 == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/System Update.sh")
    if box2 == True:
        call("/usr/local/bin/Solar Pi/Resources/Launchers/appJar Update.sh")
def Settings(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Settings Launcher.sh")

def Guides(press):
    # TODO: Fix docs launch
    Popen("../Resources/Launchers/Docs/Docs Launcher.sh")  # Launch guides here

#program.setFont(11, font="Dejavu Sans")


# About Popup
with program.subWindow("About Solar Pi", modal=True):
    program.ttkStyle.configure(".", background="white", foreground="black")
    program.setPadding(5, 5)
    program.setBg("white")
    program.addImage("solar_pi_logo", "../Resources/Images/Solar Pi logo.gif")
    program.zoomImage("solar_pi_logo", -3)
    program.setLocation(250, 150)
    program.setResizable(canResize=False)
    with program.labelFrame("About"):
        program.setBg("white")
        #program.getLabelFrameWidget("About").config(font="bold")
        program.setPadding(10, 10)
        program.addMessage("about", "The Solar Pi is charity oriented project, aiming to deliver low cost Raspberry Pi based solar powered computers to developing countries. Our aim is to teach people how to code, so that they can become employed and move on financially and socially.\n\nWe hope that you enjoy your Solar Pi!")
    program.addButton("Close", ButtonHandler)
    program.setBg("white")


# Languages Window



# Main Window
program.setPadding(3, 3)
with program.notebook("MainTabs", colspan=2):

    #program.setTabbedFrameTabExpand("MainTabs", expand=True)

    # Menu bar
    program.addMenuList("Power", ["Shutdown", "Reboot"], MenuHandler)
    program.addMenuList("Applications", ["Leafpad", "Start Programming", "Performance to Battery Life"], MenuHandler)
    program.addMenuList("Guides", ["Python Guides"], MenuHandler)
    program.addMenuList("Files", ["All Files", "Desktop", "Documents", "Music", "Pictures", "Videos"], MenuHandler)


    tools = ["Off", "Settings", "Files", "About", "Help"]
    program.addToolbar(tools, ToolbarHandler, findIcon=True)


    """
                Old Welcome Tab
    """
    # Welcome Tab
    # with program.note("Welcome!"):
    #     program.setPadding(10, 10)
    #     program.addImage("logo", "../Resources/Images/Solar Pi logo.gif", colspan=2)
    #     program.zoomImage("logo", -2)
    #     program.addLabel("welcome", "Welcome to your Solar Pi!", colspan=2)  # Update translation
    #     program.setLabelAlign("welcome", "center")
    #     program.getLabelWidget("welcome").config(font=("Dejavu Sans", "20"))
    #     program.addLabel("get_started", "To help you start to use your Solar Pi, click\non the button to open the starter guide -->", 2, 0)  # Update translation
    #     #program.addButton("Get Started", ButtonHandler, 2, 1)
    #     #program.addLabel("label1", "Your Solar Pi is a solar powered Raspberry Pi based computer.\nStart by clicking one of the tabs above.  ^^^", colspan=2)
    #     #program.addButtons(["About", "Languages", "Exit"], ButtonHandler, colspan=2)


    with program.note("Welcome!"):
        program.setPadding(10, 10)
        with program.frame("frame4", 0, 0, colspan=3):
            program.addLabel("text3", "Welcome to your ", 0, 0)
            program.setLabelAlign("text3", "right")
            program.getLabelWidget("text3").config(font=("Dejavu Sans", "20"))
            program.addImage("logo text", "../Resources/Images/Solar Pi text.gif", 0, 1)
            program.zoomImage("logo text", -45)
            program.setImageSticky("logo text", "nsw")
        with program.frame("frame5", 1, 0):
            program.setPadding(10, 10)
            program.setBg("white", override=True)
            program.addButton("Get Started", ButtonHandler)
            program.addNamedButton("Docs", "docs", Guides)
            program.addButton("About", ButtonHandler)

        program.addImage("logo4", "../Resources/Images/Logo_NEW_2 small.gif", 1, 1, rowspan=3)
        program.zoomImage("logo4", -4)

        with program.frame("frame6", 1, 2):
            program.setPadding(10, 10)
            program.addNamedButton("Programming", "programming2", Programming)
            program.addButton("Settings", Settings)
            program.addButton("Change\nLanguage", ButtonHandler)


    with program.note("Get Started"):
        program.setPadding(10, 10)
        program.addLabel("title", "Solar Pi Starter Guide", colspan=2)
        program.getLabelWidget("title").config(font=("Dejavu Sans", "15"))
        program.setLabelSticky("title", "ew")
        program.setLabelAlign("title", "center")
        program.addLabel("info1", "Your Solar Pi has a touchscreen. This means that\nyou can use your finger to touch the screen\nand control the computer.")
        program.addImage("desktop", "../Resources/Images/Desktop.gif", 1, 1, rowspan=2)
        program.zoomImage("desktop", -7)
        #program.addLabel("info1", "Your Solar Pi is a Raspberry Pi based\ncomputer. It can do almost anything you\nwant, if you know how to program it.\nWe aim to teach you how to use a computer\nand how to code, so that you have an\nadvantage over others when you get\nemployed.")
        program.addLabel("info2", "•  The image on the right is of the Solar Pi desktop.\n•  There is a bar at the top, showing you what\nwindows are open.\n•  At the top left, there is a button to open a\nmenu. From here, you can open all the\napplications that are installed on your Solar Pi.")

        with program.frame("frame"):
            program.addLabel("info4", "Read more:  ", 0, 0)
            program.setLabelAlign("info4", "right")
            program.addButton("Charging", ButtonHandler, 0, 1)



    with program.note("Charging"):
        program.setPadding(10, 10)
        program.addLabel("title5", "Charging your Solar Pi", colspan=2)
        program.getLabelWidget("title5").config(font=("Dejavu Sans", "15"))
        program.setLabelSticky("title5", "ew")
        program.setLabelAlign("title5", "center")
        text = """The battery meter below this page and in the
bottom left of the display shows how much power
is left in the batteries of your Solar Pi.
A full bar (100%) means most power, and an empty
bar (0%) means no power left.
    
When the battery meter gets close to 0% and your
Solar Pi shuts down, you need to charge it.
To do this, fold out the solar panels, and make
sure that the Solar Pi is facing the sun.
You will then need to wait for a few hours until it is
charged up.
    
Once your Solar Pi is charged, the battery meter
should show 100%."""
        program.addLabel("info5", text)
        #program.getLabelWidget("info5").config(font=("Piboto", "13"))
        with program.frame("frame1", 1, 1, rowspan=5):
            program.addLabel("read", "Read more:", 0, 0)
            program.setLabelAlign("read", "e")
            program.addButton("Starter Guide", Guides, 0, 1)


    # Applications Tab
    with program.note("Applications"):
        with program.labelFrame("Applications"):
            program.setSticky("ew")
            program.setPadding(10, 10)
            program.addLabel("applications_info", "Hover over the icons to see more information about each program.", colspan=2)

            # Start Programming
            with program.labelFrame("Start Programming", 1, 0):
                program.setPadding(10, 15)
                program.addImage("programming_icon", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                program.zoomImage("programming_icon", -13)
                program.setImageTooltip("programming_icon", "This allows you to see and try the different options for programming.")
                program.addButton("Start Programming", Programming, 0, 1)

            # Performance to Battery Life
            with program.labelFrame("Solar Pi Settings", 1, 1):
                program.setPadding(10, 10)
                program.addImage("settings", "../Resources/Images/settings icon.gif", 0, 0)
                program.zoomImage("settings", -5)
                program.setImageTooltip("settings", "This allows you to change the settings for your Solar Pi.")
                program.addButton("Solar Pi Settings", Settings, 0, 1)

            # IDEs
            with program.labelFrame("IDEs", 2, 0, colspan=2):
                program.setPadding(10, 10)

                with program.labelFrame("Scratch", 1, 0):
                    program.setPadding(10, 10)
                    program.addImage("scratch_logo2", "../Resources/Images/scratch logo.gif", 0, 0)
                    program.zoomImage("scratch_logo2", -50)
                    program.setImageTooltip("scratch_logo2", "The Scratch 2 IDE. Create Scratch programs and games with this.")
                    program.addButton("Scratch", ButtonHandler, 0, 1)

                with program.labelFrame("Python", 1, 1):
                    program.setPadding(10, 10)
                    program.addImage("python_logo2", "../Resources/Images/Python icon.gif", 0, 0)
                    program.zoomImage("python_logo2", -4)
                    program.setImageTooltip("python_logo2", "The Python IDE. Write and run Python applications.")
                    program.addButton("Python", ButtonHandler, 0, 1)

                with program.labelFrame("Java", 1, 2):
                    program.setPadding(10, 10)
                    program.addImage("java_logo", "../Resources/Images/java logo.gif", 0, 0)
                    program.zoomImage("java_logo", -5)
                    program.setImageTooltip("java_logo", "The BlueJ Java IDE. Create Java applications.")
                    program.addButton("Java", ButtonHandler, 0, 1)


    # Guides & Tutorials Tab
    with program.note("Guides & Tutorials"):
        with program.labelFrame("Guides & Tutorials"):
            program.setSticky("ew")
            program.setPadding(10, 10)
            program.addLabel("guides_info", "Hover over the icons to see more information about each guide/tutorial.", colspan=2)

            # Python Guides
            with program.labelFrame("Python Guides & Tutorials"):
                program.setPadding(10, 10)
                program.addImage("python_logo", "../Resources/Images/Python icon.gif", 0, 0)
                program.zoomImage("python_logo", -4)
                program.setImageTooltip("python_logo", "A collection of tutorials and Python documentation to help you learn Python.")
                program.addButton("Python Guides", PythonGuides, 0, 1)

            # Scratch Tutorial
            with program.labelFrame("Scratch Tutorial", 1, 1):
                program.setPadding(10, 10)
                program.addImage("scratch_logo", "../Resources/Images/scratch logo.gif", 0, 0)
                program.zoomImage("scratch_logo", -50)
                program.setImageTooltip("scratch_logo", "A beginner's tutorial on how to use Scratch.")
                program.addButton("Scratch Tutorial", ButtonHandler, 0, 1)


    """
                Removed Settings
    """

    # Settings Tab
    # with program.note("Settings"):
    #     with program.labelFrame("Settings"):
    #         program.setSticky("ew")
    #         program.setPadding(10, 10)
    #         with program.labelFrame("General Settings", 0, 0):
    #             program.setSticky("ew")
    #             program.setPadding(10, 10)
    #             program.addCheckBox("Launch this application at startup")
    #             program.setCheckBox("Launch this application at startup", ticked=True)
    #             program.addButton("Change Advanced Settings", ButtonHandler)
    #             program.addButton("Change Performance & Battery Life Settings", PerfBattery)
    #             program.addButton("Apply Changes", Settings)
    #             program.setButtonSticky("Apply Changes", "Both")
    #             program.setButtonBg("Apply Changes", "gray")
    #             program.setButtonFg("Apply Changes", "white")
    #
    #         with program.labelFrame("Update", 0, 1):
    #             program.setSticky("ew")
    #             program.setPadding(10, 10)
    #             program.addLabel("info3", "Note: This will only work\nwith an internet connection.")
    #             program.addCheckBox("Update Operating System & Installed Programs")
    #             program.addCheckBox("Update appJar")
    #             program.addButton("Go", Update)
    #             program.setButtonBg("Go", "gray")
    #             program.setButtonFg("Go", "white")


#program.setBg("white")


def Startup(param):
    value = program.getCheckBox("Launch this at startup")
    with open("../Solar Pi Settings/Settings.ini", "r") as file:
        data = file.readlines()
    data = data[0]
    data = data.split(",")
    clock = data[0]
    battery = data[1]
    value = str(value)
    theme = data[3]

    data = clock + "," + battery + "," + value + "," + theme
    with open("../Solar Pi Settings/Settings.ini", "w") as file:
        file.write(data)

with program.frame("startup", 1, 0):
    program.setPadding(3, 3)
    program.addCheckBox("Launch this at startup", 0, 1)
    program.setCheckBoxChangeFunction("Launch this at startup", Startup)
    program.setCheckBox("Launch this at startup", ticked=LaunchWelcome())


num = 0
def updateMeter():
    global num
    program.setMeter("battery", num)
    #program.setLabel("level", str(num)+"%")
    num += 1
with program.frame("battery", 1, 1):
    program.addLabel("battery", "Battery Remaining: ", 0, 0)  # Update translation
    #program.setLabelAlign("battery", "right")
    program.setLabelAnchor("battery", "e")
    program.addMeter("battery", 0, 2)
    program.setMeterFill("battery", "#13d323")
    program.addLabel("blank", "", 0, 3)
    #program.setMeterPadding("battery", 5, 5)
    program.registerEvent(updateMeter)
    program.setPollTime(10000)


with open("language.txt", "r") as file:
    lang = file.readline()
    lang.rstrip("\n")


#print(lang)

program.setLabelFrameStyle("Applications", "TFrame")
program.setLabelFrameStyle("Start Programming", "TFrame")
program.setLabelFrameStyle("Solar Pi Settings", "TFrame")
program.setLabelFrameStyle("IDEs", "TFrame")
program.setLabelFrameStyle("Scratch", "TFrame")
program.setLabelFrameStyle("Python", "TFrame")
program.setLabelFrameStyle("Java", "TFrame")
program.setLabelFrameStyle("Guides & Tutorials", "TFrame")
program.setLabelFrameStyle("Python Guides & Tutorials", "TFrame")
program.setLabelFrameStyle("Scratch Tutorial", "TFrame")

program.go(language=lang)
