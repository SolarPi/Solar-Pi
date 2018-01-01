#!/usr/bin/python
# Configures autorun

from os import remove, chmod

def FileOpenTest(file):
    try:
        with open(file, "r") as file2:
            return True
    except IOError:
        return False

def Autorun(item, mode, file):
    if mode == True:
        if FileOpenTest(file) == False:
            with open(file, "w") as file:
                if item == "welcome":
                    data = """[Desktop Entry]
        Name=Solar Pi Welcome
        Type=Application
        Comment=Launch the main Solar Pi application
        Exec="/usr/local/bin/Solar Pi/Resources/Launchers/Python Welcome Launcher.sh"
                        """
                elif item == "battery":
                    data = """[Desktop Entry]
        Name=Battery Meter
        Type=Application
        Comment=Display the battery meter in the bottom left of the display
        Exec="/usr/local/bin/Solar Pi/Solar Pi Power/Battery Meter exec"""

                file.write(data)
            chmod(file, 0o775)


    elif mode == False:
        if FileOpenTest(file) == True:
            remove("/home/pi/.config/autostart/Welcome Launcher.desktop")


if __name__ == "__main__":
    Autorun()
