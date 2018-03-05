#!/usr/bin/python
# Configures autorun

from os import remove, chmod
from shutil import chown

def FileOpenTest(file):
    try:
        with open(file, "r") as file2:
            return True
    except IOError:
        return False

def Autorun(item, mode, file):
    if mode == True:
        if FileOpenTest(file) == False:
            with open(file, "w") as file2:
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
    Exec="/usr/local/bin/Solar Pi/Power/Battery Meter exec"
    """

                file2.write(data)
            chmod(file, 0o775)
            chown(file, "pi", group=None)


    elif mode == False:
        if FileOpenTest(file) == True:
            remove(file)


if __name__ == "__main__":
    print("You aren't supposed to run this Python file.")
