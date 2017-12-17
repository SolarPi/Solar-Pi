#!/usr/bin/env python

from appJar import gui
#from ttkthemes import ThemedStyle
from subprocess import Popen

def PageHandler(press):
    if press == "next1":
        program.setTabbedFrameSelectedTab("Solar Pi Starter Guide", "Get Started")
    elif press == "next2":
        program.setTabbedFrameSelectedTab("Solar Pi Starter Guide", "Power")
    elif press == "previous2":
        program.setTabbedFrameSelectedTab("Solar Pi Starter Guide", "Get Started")

def Exit_P(press):
    exit()
def Languages(press):
    Popen("/usr/local/bin/Solar Pi/Resources/Launchers/language_launcher.sh")

with gui("Starter Guide", useTtk=False) as program:
    #program.setPadding(5, 5)

    #program.ttkStyle = ThemedStyle(program.topLevel)
    #program.ttkStyle.set_theme("plastik")

    with program.tabbedFrame("Solar Pi Starter Guide"):
        program.setBg("white")
        with program.tab("Introduction"):
            program.setPadding(10, 10)
            #program.setBg("white")
            with program.frame("title", colspan=2):
                program.addImage("logo", "Logo_NEW_2.gif", 0, 0)
                program.zoomImage("logo", -50)
                program.addLabel("welcome", "Welcome to the Solar Pi\nStarter Guide!", 0, 1)
                program.getLabelWidget("welcome").config(font=("Segoe UI", "15", "bold"))


            # with program.toggleFrame("Languages", colspan=2):
            #     program.setSticky("ew")
            #     program.addLabel("languages", "If this is the incorrect language, please click the button and select the correct one.\nSi este es el idioma incorrecto, haga clic en el botón y seleccione el correcto.", colspan=2)
            #     program.addButton("Languages", Languages)

            with program.frame("frame", colspan=2):
                program.addLabel("label2", "Your Solar Pi is a Raspberry Pi based\ncomputer. It can do almost anything you\nwant, if you know how to program it.\n", 0, 0)
                program.addLabel("label3", "We aim to teach you how to use a computer\nand how to code, so that you have an\nadvantage over others when you get employed.", 1, 0)
                program.addImage("desktop", "Desktop.gif", 0, 1, rowspan=2)
                program.zoomImage("desktop", -10)
                program.addScrolledTextArea("text")
                program.setTextArea("text", "Your Solar Pi is a Raspberry Pi based\ncomputer. It can do almost anything you\nwant, if you know how to program it.\nWe aim to teach you how to use a computer\nand how to code, so that you have an\nadvantage over others when you get employed.")
                program.disableTextArea("text")

            program.addLabel("label1", "Click 'NEXT' to continue reading the guide", colspan=2)
            program.addNamedButton("PREVIOUS", "previous1", PageHandler, 10, 0)
            program.disableButton("previous1")
            program.addNamedButton("NEXT", "next1", PageHandler, 10, 1)
            
        with program.tab("Get Started"):
            program.setPadding(5, 5)
            #program.setBg("white")
            program.addLabel("label4", "This is the Solar Pi desktop.")

            program.addNamedButton("PREVIOUS", "previous2", PageHandler, 10, 0)
            program.addNamedButton("NEXT", "next2", PageHandler, 10, 1)
            

        with program.tab("Power"):
            program.setPadding(5, 5)
            
    #program.addButton("Exit", Exit_P, 2, 1)
program.go()
