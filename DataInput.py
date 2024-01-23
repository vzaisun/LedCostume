def formatData(myInt):
    if myInt <= 9:
        myString = "000" + str(myInt)
    elif myInt <= 99:
        myString = "00" + str(myInt)
    else:
        myString = "0" + str(myInt)
    return myString


def formatDuration(myInt):
    return str(myInt * 1000)


def DataInputMech():
    print("Give sample input for 10 cycles: ")
    # Get Input Data
    mode = int(input("Enter ON or Blink (0/1): "))
    r_color = int(input("Enter R value in RGB (0-255): "))
    g_color = int(input("Enter G value in RGB (0-255):  "))
    b_color = int(input("Enter B value in RGB (0-255): "))
    duration = int(input("Enter Duration for the sequence in seconds: "))
    # Convert data to required format
    mode_value = formatData(mode)
    r_value = formatData(r_color)
    g_value = formatData(g_color)
    b_value = formatData(b_color)
    duration_value = formatDuration(duration)
    # Combine to for a string
    oneValue = mode_value + r_value + g_value + b_value + duration_value
    return oneValue


def DataInputMain():
    Datalist = []
    for i in range(0, 3):
        Datalist.append(DataInputMech())
    return ''.join(Datalist)
