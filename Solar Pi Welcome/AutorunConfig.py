#!/usr/bin/python
# Configures autorun

def FileOpenTest():
    try:
        with open("/home/pi/.config/autostart/Welcome Launcher.desktop", "r") as file:
            return True
    except IOError:
        return False

def Autorun(mode):
    from os import remove, chmod
    if mode == "add":
        if FileOpenTest() == False:
            with open("/home/pi/.config/autostart/Welcome Launcher.desktop", "w") as file:
                data = """[Desktop Entry]
Name=Solar Pi Welcome
Type=Application
Comment=Launch the main Solar Pi application
Exec="/usr/local/bin/Solar Pi/Resources/Launchers/Python Welcome Launcher.sh"
"""
                file.write(data)
            chmod("/home/pi/.config/autostart/Welcome Launcher.desktop", 0o775)

    elif mode == "remove":
        if FileOpenTest() == True:
            remove("/home/pi/.config/autostart/Welcome Launcher.desktop")
        else:
            pass


if __name__ == "__main__":
    Autorun()
