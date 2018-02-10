#!/usr/bin/env python3
# Solar Pi Welcome

from appJar import gui
from subprocess import Popen, call
#from AutorunConfig import Autorun
from sys import exit
from SettingsGet import LaunchWelcome
import webbrowser
from AutorunConfig import Autorun


with open("../Solar Pi Settings/Settings.ini", "r") as file:  # Read Settings.ini file
    data = file.readlines()[0]
data = data.split(",")
theme1 = data[3]

program = gui("Solar Pi Welcome", useTtk=True)
program.setResizable(True)
#program.setLocation("CENTER")

if theme1 == "Solar Pi":
    msgFg = "black"
    msgBg = "white"
    solar_theme = True
else:
    solar_theme = False
    program.setTtkTheme(theme1)
    msgFg = "white"
    msgBg = "#424242"
    if theme1 != "black":
        program.ttkStyle.configure(".", foreground="black", background="white")
        program.ttkStyle.map("TCheckbutton", background=[("active", "white")])
        program.setBg("white")
        msgFg = "black"
        msgBg = "white"

if solar_theme == True:
    program.setTtkTheme("plastik")
    program.setTtkTheme("clam")
    #program.ttkStyle.configure(".", font="10")

    # Custom Notebook
    program.ttkStyle.configure("TNotebook", background="white", bordercolor="#687396")
    program.ttkStyle.map("TNotebook.Tab", background=[("selected", "#76a928")],  # Selected tab
                foreground=[("selected", "white")])
    program.ttkStyle.configure("TNotebook.Tab", background="#dbdce2", foreground="black", bordercolor="#687396")  # Unselected tab

    # Custom buttons

    # Highlighted button
    program.ttkStyle.configure("H.TButton", background="#324581", foreground="white", bordercolor="#687396")
    program.ttkStyle.map("H.TButton", background=[("pressed", "#172141"), ("active", "#4059a9")])

    program.ttkStyle.map("TCheckbutton", background=[("active", "white")])

    # Regular button
    program.ttkStyle.configure("TButton", background="#dbdce2", bordercolor="#687396")

    program.ttkStyle.map("TLabelFrame", border=[("active", "black")])

    program.ttkStyle.configure("TLabelframe", bordercolor="#687396")

title_font = ("ubuntu", 14, "normal")
program.ttkStyle.configure("H.TLabel", background="#687396", foreground="white", padding=[10, 10]) # #dbdce2, #687396
program.ttkStyle.configure("Info.TLabel", padding=[10, 10])

# Event Handler for buttons
def ButtonHandler(press):
    #tab_selected = program.getTabbedFrameSelectedTab("MainTabs")  # Fetches the current tab
    press = press.lower()

    if press == "Exit" or press == "Exit3" or press == "Exit2" or press == "Exit4":  # Exits program
        exit()  # Quits program
    elif press == " about":  # Opens the About subwindow
        program.showSubWindow("About Solar Pi")
    elif press == "close":  # Closes the About subwindow
        program.hideSubWindow("About Solar Pi")
    elif press == "scratch":  # Launches Scratch
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Scratch Launcher.sh")
    elif press == "python":  # Launches a Python IDE
        if program.yesNoBox("Python", "Would you like to use the Thonny Python IDE instead of the IDLE?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Thonny Launcher.sh")  # Launches Thonny
        else:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/IDLE Launcher.sh")  # Launches IDLE
    elif press == "java":  # Launches BlueJ
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/BlueJ Launcher.sh")
    elif press == "change advanced settings":  # Launches RPi settings window
        Popen("/usr/bin/rc_gui")
    elif press == "  languages":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")  # Launches settings for display language
    elif press == "get started":
        program.getNotebookWidget("MainTabs").select([1])  # Sets selected note/tab to Get Started

    elif press == "charging":
        program.getNotebookWidget("MainTabs").select([2])  # Set selected note/tab to Charging


# Menu event handler
def MenuHandler(press):
    if press == "Shutdown":
        if program.yesNoBox("Shutdown", "Are you sure that you want to shutdown your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Shutdown.sh")  # Shuts down RPi
    elif press == "Reboot":
        if program.yesNoBox("Reboot", "Are you sure that you want to reboot your Solar Pi now?") == True:
            Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Reboot.sh")  # Reboots RPi
    elif press == "Leafpad":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/Leafpad Launcher.sh")  # Launches Leafpad
    elif press == "Start Programming":
        Programming(None)
    elif press == "Python Guides":
        PythonGuides(None)
    elif press == "Performance to Battery Life":
        PerfBattery(None)
    elif press == "All Files":
        Popen("/usr/local/bin/Solar Pi/Resources/Launchers/pcmanfm Launcher.sh")  # Launches file manager
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
        webbrowser.get("chromium-browser").open("http://localhost/solar-pi-apps/index.html#solar-pi-welcome")

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

def Docs(press):
    webbrowser.get("chromium-browser").open("http://localhost/")  # Launch guides here

def PythonIntro(press):  # RPi Python Introduction
    webbrowser.get("chromium-browser").open("http://localhost/Advanced-Things/python/index.html")
def Glossary(press):  # Programming Glossary
    webbrowser.get("chromium-browser").open("http://localhost/Glossaries/programming-glossary/index.html")
def ByteofPython(press):  # Byte of Python
    webbrowser.get("chromium-browser").open("http://localhost:81/")
def Java(press):  # Google's Python Tutorial
    webbrowser.get("chromium-browser").open("http://localhost:82/java/index.htm")


#program.setFont(11, font="Dejavu Sans")


# About Popup
with program.subWindow("About Solar Pi", modal=True):
    #program.setBg("white")
    with program.frame("frame7"):  # Rename to frame6 to remove right hand button column on Welcome tab
        program.setPadding(5, 5)
        #program.setBg("white")
        program.addImage("solar_pi_logo", "../Resources/Images/Solar Pi logo.gif")
        program.zoomImage("solar_pi_logo", -3)
        program.setResizable(canResize=False)
        with program.labelFrame("About"):
            #program.setBg("white")
            program.setPadding(10, 10)
            program.addMessage("about", "The Solar Pi is charity oriented project, aiming to deliver low cost Raspberry Pi based solar powered computers to developing countries. Our aim is to teach people how to code, so that they can become employed and move on financially and socially.\n\nWe hope that you enjoy your Solar Pi!")
            program.setMessageBg("about", msgBg)
            program.setMessageFg("about", msgFg)
        program.addButton("Close", ButtonHandler)
        program.setButtonSticky("Close", "")
        if solar_theme == True:
            program.setButtonStyle("Close", "H.TButton")

# Menu bar
program.addMenuList("Power", ["Shutdown", "Reboot"], MenuHandler)
program.addMenuList("Applications", ["Leafpad", "Start Programming", "Performance to Battery Life"], MenuHandler)
program.addMenuList("Guides", ["Python Guides"], MenuHandler)
program.addMenuList("Files", ["All Files", "Desktop", "Documents", "Music", "Pictures", "Videos"], MenuHandler)


tools = ["Off", "Settings", "Files", "About", "Help"]
program.addToolbar(tools, ToolbarHandler, findIcon=True)
#if theme1 == "Solar Pi":
#    var = program.widgetManager.group(program.Widgets.Toolbar)
#    var["Off"].config(fg="#dbdce2")
#program.setToolbarFg("white")

# Main Window
program.setPadding(3, 3)

with program.notebook("MainTabs", colspan=2):
    with program.note("Welcome!"):
        program.setPadding(10, 10)
        with program.frame("frame4", 0, 0, colspan=3):
            program.addLabel("text4", "Welcome to your  ", 0, 0)
            program.setLabelAlign("text4", "right")
            program.getLabelWidget("text4").config(font=("ubuntu", "20"))
            program.addImage("logo text1", "../Resources/Images/Solar Pi text small.gif", 0, 1)
            program.zoomImage("logo text1", -2)
            program.setImageSticky("logo text1", "nsw")

        with program.frame("frame5", 1, 0):
            program.setPadding(10, 10)
            if solar_theme == True or theme1 == "black":
                program.addImageButton("Get Started", ButtonHandler, "../Resources/Images/md-play.gif", align="left", row=1, column=0)
            else:
                program.addIconButton("Get Started", ButtonHandler, "md-play", align="left", row=1, colspan=0)
            program.setButtonSticky("Get Started", "nesw")
            program.addImageButton(" Docs", Docs, "../Resources/Images/docs icon.gif", align="left", row=2, column=0)
            program.setButtonSticky(" Docs", "nesw")
            program.addIconButton(" About", ButtonHandler, "about", align="left", row=3, column=0)
            program.setButtonSticky(" About", "nesw")
        program.addImage("logo5", "../Resources/Images/Logo_NEW_2 small.gif", 1, 1, rowspan=3)
        program.zoomImage("logo5", -4)

        with program.frame("frame6", 1, 2):
            program.setPadding(10, 10)
            program.addImageButton("  Coding", Programming, "../Resources/Images/Programming icon small.gif",
                                   align="left", row=1, column=2)
            program.setButtonSticky("  Coding", "nesw")
            program.addIconButton(" Settings", Settings, "settings", align="left", row=2, column=2)
            program.setButtonSticky(" Settings", "nesw")
            program.addImageButton("  Languages", ButtonHandler, "../Resources/Images/languages small.gif",
                                   align="left", row=3, column=2)
            program.setButtonSticky("  Languages", "nesw")


        if solar_theme == True:
            program.setButtonStyle("Get Started", "H.TButton")


    with program.note("Starter Guide"):
        with program.scrollPane("scroll1"):
            program.addLabel("starter_title", "Solar Pi Starter Guide", colspan=2)
            program.getLabelWidget("starter_title").config(font=title_font)
            program.setLabelStyle("starter_title", "H.TLabel")
            #program.setLabelSticky("title", "ew")
            #program.setLabelAlign("title", "center")
            #program.addLabel("info1", "Your Solar Pi has a touchscreen. This means that\nyou can use your finger to touch the screen\nand control the computer.")

            with program.frame("frame19"):
                program.setPadding(10, 10)
                program.addImage("desktop", "../Resources/Images/Desktop.gif", 0, 1)
                program.zoomImage("desktop", -7)
                #program.addLabel("info1", "Your Solar Pi is a Raspberry Pi based\ncomputer. It can do almost anything you\nwant, if you know how to program it.\nWe aim to teach you how to use a computer\nand how to code, so that you have an\nadvantage over others when you get\nemployed.")
                #program.addLabel("info2", "

                starter_info = """Your Solar Pi has a touchscreen. This means that you can use your finger to touch the screen and control the computer.
        
•  The image on the right is of the Solar Pi desktop.
•  There is a bar at the top, showing you what windows are open.
•  At the top left, there is a button to open a menu. From here, you can see and run all of the applications that are installed on your Solar Pi."""
                program.addMessage("starter_info", starter_info, 0, 0)
                program.setMessageBg("starter_info", msgBg)
                program.setMessageFg("starter_info", msgFg)
                program.setMessageSticky("starter_info", "nesw")

                with program.frame("frame"):
                    program.addLabel("info4", "Read more:  ", 0, 0)
                    program.setLabelAlign("info4", "right")
                    program.addNamedButton("Docs", "docs", ButtonHandler, 0, 1)

            program.addHorizontalSeparator()

            program.addLabel("charging_title", "Charging your Solar Pi", colspan=3)
            program.setLabelStyle("charging_title", "H.TLabel")
            program.getLabelWidget("charging_title").config(font=title_font)
            #program.setLabelSticky("title5", "ew")
            #program.setLabelAlign("title5", "center")
            with program.frame("frame20"):
                program.setPadding(10, 10)
                program.setStretch("columns")
                charge_info = """The battery meter below this page and in the bottom left of the display shows how much power is left in the batteries of your Solar Pi. A full bar (100%) means most power, and an empty bar (0%) means no power left.
When the battery meter gets close to 0% and your Solar Pi shuts down, you need to charge it. To do this, fold out the solar panels, and make sure that the Solar Pi is facing the sun. You will then need to wait for a few hours until it is charged up.
Once your Solar Pi is charged, the battery meter should show 100%."""
                # program.addLabel("info5", text)
                # program.setLabelAlign("info5", "center")
                # program.getLabelWidget("info5").config(font=("Piboto", "13"))

                program.addMessage("charge_info", charge_info)
                program.setMessageBg("charge_info", msgBg)
                program.setMessageFg("charge_info", msgFg)

                with program.frame("frame21"):
                    program.addLabel("read", "Read more:", 0, 0)
                    program.setLabelAnchor("read", "e")
                    program.addButton("Starter Guide", Docs, 0, 1)
                    program.setButtonSticky("Starter Guide", "")

            if solar_theme == True:
                program.setButtonStyle("docs", "H.TButton")
                program.setButtonStyle("Starter Guide", "H.TButton")


#     with program.note("Charging"):
#
#         #program.setPadding(10, 10)
#         program.addLabel("title5", "Charging your Solar Pi", colspan=3)
#         program.getLabelWidget("title5").config(font=("Dejavu Sans", "15"))
#         program.setLabelSticky("title5", "ew")
#         program.setLabelAlign("title5", "center")
#         charge_info = """The battery meter below this page and in the bottom left of the display shows how much power is left in the batteries of your Solar Pi. A full bar (100%) means most power, and an empty bar (0%) means no power left.
# When the battery meter gets close to 0% and your Solar Pi shuts down, you need to charge it. To do this, fold out the solar panels, and make sure that the Solar Pi is facing the sun. You will then need to wait for a few hours until it is charged up.
# Once your Solar Pi is charged, the battery meter should show 100%."""
#         #program.addLabel("info5", text)
#         #program.setLabelAlign("info5", "center")
#         #program.getLabelWidget("info5").config(font=("Piboto", "13"))
#
#         program.addMessage("charge_info", charge_info)
#         program.setMessageBg("charge_info", msgBg)
#         program.setMessageFg("charge_info", msgFg)
#         program.setMessageSticky("charge_info", "nesw")
#
#         program.addLabel("read", "Read more:", 1, 1)
#         program.setLabelAnchor("read", "e")
#         program.addButton("Starter Guide", Docs, 1, 2)
#         program.setButtonSticky("Starter Guide", "")
#
#         if solar_theme == True:
#             program.setButtonStyle("Starter Guide", "H.TButton")


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
                program.setSticky("nesw")

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

        if solar_theme == True:
            program.setButtonStyle("Start Programming", "H.TButton")


    with program.note("Applications b"):
        program.setSticky("nesw")
        program.setPadding(0, 0)

        with program.scrollPane("scroll"):
            program.setPadding(0, 0)
            program.setSticky("nesw")
            program.addLabel("applications_title", "Solar Pi Applications")
            program.setLabelStyle("applications_title", "H.TLabel")
            program.getLabelWidget("applications_title").config(font=("ubuntu", 15, "normal"))

            program.addHorizontalSeparator()

            program.addLabel("coding_title", "Start Coding", colspan=3)
            #program.setLabelAlign("coding_title", "center")
            program.setLabelStyle("coding_title", "Info.TLabel")
            program.getLabelWidget("coding_title").config(font=title_font)
            with program.frame("frame8"):
                program.setPadding(10, 10)
                program.addImage("coding_icon", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                program.zoomImage("coding_icon", -13)
                program.addLabel("coding_info", "This allows you to see and try the different options for coding.", 0, 1)
                #program.addLabel("coding_info", "Cela vous permet de voir et d'essayer les différentes options de programmation.", 0, 1)
                program.addNamedButton("Try it out!", "tryit1", Programming, 0, 2)

            program.addHorizontalSeparator()

            program.addLabel("settings_title", "Solar Pi Settings")
            program.setLabelStyle("settings_title", "Info.TLabel")
            program.getLabelWidget("settings_title").config(font=title_font)
            with program.frame("frame9"):
                program.setPadding(10, 10)
                program.addImage("settings_icon", "../Resources/Images/settings icon.gif", 0, 0)
                program.zoomImage("settings_icon", -6)
                program.addLabel("settings_info", "This allows you to change the settings for your Solar Pi.", 0, 1)
                program.addButton("Settings", Settings, 0, 2)

            #program.addHorizontalSeparator()
            program.addLabel("filler", "")

            program.addLabel("ides", "IDEs (Places where you can code)")
            program.setLabelStyle("ides", "H.TLabel")
            program.getLabelWidget("ides").config(font=title_font)
            program.addHorizontalSeparator()

            program.addLabel("scratch_title", "Scratch")
            program.setLabelStyle("scratch_title", "Info.TLabel")
            program.getLabelWidget("scratch_title").config(font=title_font)
            with program.frame("frame10"):
                program.setPadding(10, 10)
                program.addImage("scratch_icon", "../Resources/Images/scratch logo.gif", 0, 0)
                program.zoomImage("scratch_icon", -50)
                program.addLabel("scratch_info", "The Scratch 2 IDE. Create Scratch programs and games with this.", 0, 1)
                program.addNamedButton("Scratch", "scratch", ButtonHandler, 0, 2)

            program.addHorizontalSeparator()

            program.addLabel("python_title", "Python")
            program.setLabelStyle("python_title", "Info.TLabel")
            program.getLabelWidget("python_title").config(font=title_font)
            with program.frame("frame11"):
                program.setPadding(10, 10)
                program.addImage("python_icon", "../Resources/Images/Python icon.gif", 0, 0)
                program.zoomImage("python_icon", -4)
                program.addLabel("python_icon", "The Python IDE. Write and run Python applications.", 0, 1)
                program.addNamedButton("Python", "python", ButtonHandler, 0, 2)

            program.addHorizontalSeparator()

            program.addLabel("java_title", "Java")
            program.setLabelStyle("java_title", "Info.TLabel")
            program.getLabelWidget("java_title").config(font=title_font)
            with program.frame("frame12"):
                program.setPadding(10, 10)
                program.addImage("java_icon", "../Resources/Images/java logo.gif", 0, 0)
                program.zoomImage("java_icon", -5)
                program.addLabel("java_info", "The BlueJ Java IDE. Create Java applications.", 0, 1)
                program.addNamedButton("Java", "java", ButtonHandler, 0, 2)

            #program.addHorizontalSeparator()
            program.addLabel("filler2", "")

            # TODO: Add launchers + calls for ButtonHandler for Libreoffice
            program.addLabel("libreoffice_title", "LibreOffice: A free office suite")
            program.setLabelStyle("libreoffice_title", "H.TLabel")
            program.getLabelWidget("libreoffice_title").config(font=title_font)
            program.addHorizontalSeparator()

            program.addLabel("writer_title", "Writer")
            program.setLabelStyle("writer_title", "Info.TLabel")
            program.getLabelWidget("writer_title").config(font=title_font)
            with program.frame("frame13"):
                program.setPadding(10, 10)
                program.addImage("writer_icon", "../Resources/Images/writer.gif", 0, 0)
                #program.zoomImage("writer_icon", -2)
                program.addLabel("writer_info", "A simple, easy to use word processor.", 0, 1)
                program.addButton("Writer", ButtonHandler, 0, 2)

            program.addHorizontalSeparator()

            program.addLabel("calc_title", "Calc")
            program.setLabelStyle("calc_title", "Info.TLabel")
            program.getLabelWidget("calc_title").config(font=title_font)
            with program.frame("frame14"):
                program.setPadding(10, 10)
                program.addImage("calc_icon", "../Resources/Images/calc.gif", 0, 0)
                # program.zoomImage("writer_icon", -2)
                program.addLabel("calc_info", "Quickly make speadsheets and crunch numbers.", 0, 1)
                program.addButton("Calc", ButtonHandler, 0, 2)

            program.addHorizontalSeparator()

            program.addLabel("impress_title", "Impress")
            program.setLabelStyle("impress_title", "Info.TLabel")
            program.getLabelWidget("impress_title").config(font=title_font)
            with program.frame("frame15"):
                program.setPadding(10, 10)
                program.addImage("impress_icon", "../Resources/Images/impress.gif", 0, 0)
                # program.zoomImage("writer_icon", -2)
                program.addLabel("impress_info", "Create presentations!", 0, 1)
                program.addButton("Impress", ButtonHandler, 0, 2)

            program.addHorizontalSeparator()

            program.addLabel("draw_title", "Draw")
            program.setLabelStyle("draw_title", "Info.TLabel")
            program.getLabelWidget("draw_title").config(font=title_font)
            with program.frame("frame16"):
                program.setPadding(10, 10)
                program.addImage("draw_icon", "../Resources/Images/draw.gif", 0, 0)
                # program.zoomImage("writer_icon", -2)
                program.addLabel("draw_info", "Show off your art skills!", 0, 1)
                program.addButton("Draw", ButtonHandler, 0, 2)

            program.addHorizontalSeparator()

            program.addLabel("apps_more_info", "Want to look at more apps?\nGo to the Main Menu to see all of the apps installed on your Solar Pi.")
            program.setLabelStyle("apps_more_info", "H.TLabel")

        if solar_theme == True:
            program.setButtonStyle("tryit1", "H.TButton")
            #program.setButtonStyle("Settings", "H.TButton")
            #program.setButtonStyle("scratch", "H.TButton")
            #program.setButtonStyle("python", "H.TButton")
            #program.setButtonStyle("java", "H.TButton")


    #     program.setSticky("nesw")
    #    # program.setBg("white")
    #     with program.scrollPane("scroll1"):
    #         program.setSticky("nesw")
    #         with program.frame("frame9"):
    #             #program.setBg("white")
    #             program.setSticky("nesw")
    #             program.addButton("Button", None)
    #             program.addMessage("m1", "jlkf;afd jfdkalf jkla;f jlk;afjkl;ajfkdlasf jkal; fjkadsl;f jkla;jklajkl;a kls akfl\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n;fjoiwejioruiowreu wqopuiqwopruiowqru oq[wruwioq[ruioq[ wru oq[wruoqwuro[iqruo[q uoq[urqow[ruoq")
    #     #program.setScrollPaneBg("scroll1", "white")

    # Guides & Tutorials Tab
    with program.note("Guides & Tutorials"):

        with program.labelFrame("Guides & Tutorials"):
            program.setSticky("nesw")
            program.setPadding(10, 10)
            program.addLabel("guides_info", "Hover over the icons to see more information about each resource.", 0, 0, colspan=2)
            #    program.addImage("python", "../Resources/Images/Python icon.gif", 0, 1)
             #   program.zoomImage("python", -2)

            # RPi Foundation Python Tutorial
            with program.labelFrame("Introduction to Python", 1, 0):
                program.setPadding(10, 10)
                program.addImage("python2", "../Resources/Images/Python icon.gif", 0, 0)
                program.zoomImage("python2", -4)
                program.setImageTooltip("python2", "An introduction to Python, written by the Raspberry Pi Foundation")
                program.addButton("Python Intro", PythonIntro, 0, 1)

            # Programming Glossary
            with program.labelFrame("Programming Glossary", 1, 1):
                program.setPadding(10, 10)
                program.addImage("programming_icon2", "../Resources/Images/Programming icon cropped.gif", 0, 0)
                program.zoomImage("programming_icon2", -10)
                program.setImageTooltip("programming_icon2", "Gives you definitions of words that you might not have heard before")
                program.addButton("Glossary", Glossary, 0, 1)

            # A Byte of Python
            with program.labelFrame("A Byte of Python", 2, 0):
                program.setPadding(10, 10)
                program.addImage("python3", "../Resources/Images/Python icon.gif", 0, 0)
                program.zoomImage("python3", -4)
                program.setImageTooltip("python3", "A popular Ebook that teaches you Python")
                program.addButton("A Byte of Python", ByteofPython, 0, 1)

            # Google Python Tutorial
            with program.labelFrame("Java Guide", 2, 1):
                program.setPadding(10, 10)
                program.addImage("java_logo2", "../Resources/Images/java logo.gif", 0, 0)
                program.zoomImage("java_logo2", -5)
                program.setImageTooltip("java_logo2", "A guide on Java to help you get to know the basics of Java 8")
                program.addButton("Java Guide", Java, 0, 1)


        if solar_theme == True:
            program.setButtonStyle("Python Intro", "H.TButton")

    with program.note("System Info"):
        try:
            call("uname -r > \"/usr/local/bin/Solar Pi/Solar Pi Welcome/sysinfo\"")
            call("df -h --output=size,used,avail,pcent >> \"/usr/local/bin/Solar Pi/Solar Pi Welcome/sysinfo\"")
            call("cat /etc/*release* > \"/usr/local/bin/Solar Pi/Solar Pi Welcome/osinfo\"")
        except FileNotFoundError:
            print("Running under Windows! ...or another machine that isn't a Solar Pi")

        with open("osinfo", "r") as file:
            data = file.readlines()
        for line in data:
            if line.startswith("DISTRIB_DESCRIPTION="):
                os_v = line.split("=")[1]
                os_v = os_v.lstrip("\"")
                os_v = os_v.rstrip("\"\n")
                break
        with open("sysinfo", "r") as file:
            data = file.readlines()
        kernel_v = data[0].rstrip("\n")
        disk_data = data[2].split()
        total_disk = disk_data[0] + "B"
        used_disk = disk_data[1] + "B"
        avail_disk = disk_data[2] + "B"
        pcent_disk_used = int(disk_data[3].rstrip("%"))
        pcent_disk_avail = 100 - pcent_disk_used

        bold_font = ("ubuntu", 12, "bold")

        with program.labelFrame("Raspberry Pi Info"):
            program.setPadding(10, 5)
            program.addLabel("rpi_model", "Raspberry Pi Model:", 0, 0)
            program.getLabelWidget("rpi_model").config(font=bold_font)
            program.addLabel("rpi_model_value", "Raspberry Pi 3 Model B", 0, 1)

            program.addLabel("soc", "SoC:", 0, 2)
            program.getLabelWidget("soc").config(font=bold_font)
            program.addLabel("soc_value", "Broadcom BCM2837", 0, 3)

            program.addLabel("cpu", "CPU:", 1, 0)
            program.getLabelWidget("cpu").config(font=bold_font)
            program.addLabel("cpu_value", "4 x ARM Cortex A53, 1.2GHz", 1, 1)

            program.addLabel("ram", "RAM:", 1, 2)
            program.getLabelWidget("ram").config(font=bold_font)
            program.addLabel("ram_value", "LPDDR2 1.0GB", 1, 3)

        with program.labelFrame("OS Info"):
            program.setPadding(10, 5)
            program.addLabel("os_version", "Operating System:", 0, 0)
            program.getLabelWidget("os_version").config(font=bold_font)
            program.addLabel("os_version_value", os_v, 0, 1)

            program.addLabel("kernel_version", "Kernel Version:", 0, 2)
            program.getLabelWidget("kernel_version").config(font=bold_font)
            program.addLabel("kernel_version_value", kernel_v, 0, 3)

        with program.labelFrame("Disk Info"):
            program.setPadding(10, 5)
            program.addLabel("total_disk", "Total Disk Space:", 0, 0)
            program.getLabelWidget("total_disk").config(font=bold_font)
            program.addLabel("total_disk_value", total_disk, 0, 1)

            program.addLabel("used_disk", "Used Disk Space:", 0, 2)
            program.getLabelWidget("used_disk").config(font=bold_font)
            program.addLabel("used_disk_value", used_disk, 0, 3)

            program.addLabel("avail_disk", "Free Disk Space:", 0, 4)
            program.getLabelWidget("avail_disk").config(font=bold_font)
            program.addLabel("avail_disk_value", avail_disk, 0, 5)

            with program.frame("frame22", 1, 0, colspan=2):
                program.setPadding(5, 1)
                program.addMeter("disk_usage", 0, 0)
                program.setMeter("disk_usage", pcent_disk_used)
                if pcent_disk_used < 85:
                    program.setMeterFill("disk_usage", "#687396")
                else:
                    program.setMeterFill("disk_usage", "red")
                program.setMeterSticky("disk_usage", "ew")
                program.setMeterTooltip("disk_usage", "Used: " + used_disk + "\nFree: " + avail_disk)
                program.addLabel("disk_label", avail_disk + " free of " + total_disk, 1, 0)
            program.setFrameSticky("frame22", "ew")
            #program.addPieChart("disk_chart", {"Available": pcent_disk_avail, "Used": pcent_disk_used}, 0, 1, rowspan=3)


def Startup(param):
    value = program.getCheckBox("Launch at startup")
    with open("../Solar Pi Settings/Settings.ini", "r") as file:
        data = file.readlines()
    data = data[0]
    data = data.split(",")
    clock = data[0]
    battery = data[1]
    welcome = str(value)
    theme = data[3]

    data = clock + "," + battery + "," + welcome + "," + theme
    with open("../Solar Pi Settings/Settings.ini", "w") as file:
        file.write(data)
    
    Autorun("welcome", value, "/home/pi/.config/autostart/Welcome Launcher.desktop")

program.setPadding(5, 5)
program.addCheckBox("Launch at startup", 1, 0)
program.setCheckBox("Launch at startup", ticked=LaunchWelcome())
program.setCheckBoxChangeFunction("Launch at startup", Startup)


# num = 0
# def updateMeter():
#     global num
#     program.setMeter("battery", num)
#     #program.setLabel("level", str(num)+"%")
#     num += 1
# with program.frame("battery", 1, 1):
#     program.addLabel("battery", "Battery Remaining: ", 0, 0)  # Update translation
#     #program.setLabelAlign("battery", "right")
#     program.setLabelAnchor("battery", "e")
#     program.addMeter("battery", 0, 2)
#     program.setMeterFill("battery", "#13d323")
#     program.addLabel("blank", "", 0, 3)
#     #program.setMeterPadding("battery", 5, 5)
#     program.registerEvent(updateMeter)
#     program.setPollTime(10000)


with open("language.txt", "r") as file:
    lang = file.readline()
    lang.rstrip("\n")

#print(lang)
#program.setLabelFrameStyle("-", "TFrame")
#program.setLabelFrameStyle("", "TFrame")
#program.ttkStyle.configure(".", background="white", foreground="black")

if solar_theme == False:
    ##program.ttkStyle.configure("TLabelframe", background="white")

    program.setLabelFrameStyle("Applications", "TFrame")
    program.setLabelFrameStyle("Start Programming", "TFrame")
    program.setLabelFrameStyle("Solar Pi Settings", "TFrame")
    program.setLabelFrameStyle("IDEs", "TFrame")
    program.setLabelFrameStyle("Scratch", "TFrame")
    program.setLabelFrameStyle("Python", "TFrame")
    program.setLabelFrameStyle("Java", "TFrame")
    program.setLabelFrameStyle("Guides & Tutorials", "TFrame")
    program.setLabelFrameStyle("Introduction to Python", "TFrame")
    program.setLabelFrameStyle("Programming Glossary", "TFrame")
    program.setLabelFrameStyle("A Byte of Python", "TFrame")
    program.setLabelFrameStyle("Java Guide", "TFrame")
    program.setLabelFrameStyle("About", "TFrame")
    program.setLabelFrameStyle("Raspberry Pi Info", "TFrame")
    program.setLabelFrameStyle("OS Info", "TFrame")
    program.setLabelFrameStyle("Disk Info", "TFrame")

if theme1 != "black":
    program.setBg("white")

#print(program.ttkStyle.lookup("TFrame", "bordercolor"))

program.go(language=lang)
