##############################
#   Index:                   #
#   0 = clock                #
#   1 = battery meter        #
#   2 = welcome              #
#   3 = theme                #
#   4 = language             #
##############################

def getSetting(setting):
    with open("../../Solar Pi Settings/Settings.ini", "r") as file:
        data = file.readlines()[0].split(",")
    if setting == "clock":
        return int(data[0])
    elif setting == "battery":
        return data[1] == "True"
    elif setting == "welcome":
        return data[2] == "True"
    elif setting == "theme":
        return data[3]
    elif setting == "language":
        return data[4]

def setSetting(setting, value):
    with open("../../Solar Pi Settings/Settings.ini", "r") as file:
        data = file.readlines()[0].split(",")
    
    clock = data[0]
    battery = data[1]
    welcome = data[2]
    theme = data[3]
    language = data[4]
    
    if setting == "clock":
        clock = value
    elif setting == "battery":
        battery = value
    elif setting == "welcome":
        welcome = value
    elif setting == "theme":
        theme = value
    elif setting == "language":
        language = value

    data = clock + "," + battery + "," + welcome + "," + theme + "," + language
    with open("../Solar Pi Settings/Settings.ini", "w") as file:
        file.write(data)

if __name__ == "__main__":
    print("This is a module!")
    exit()
