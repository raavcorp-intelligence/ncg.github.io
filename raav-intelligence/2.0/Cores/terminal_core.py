from user_options import checkuseroptions
import sys

# Terminal Core, this is for information about RAAV
modelbuild = 1.0
def terminal():
    print("RXT TERMINAL BUILD " + str(modelbuild))
    print("Type `help` for commands.")
    terminalrunning = 0
    while terminalrunning == 0:
        command = input(">>> ")
        splicedcommand = command.split(" ")
        if splicedcommand[0] == "exit":
            sys.exit()
        if splicedcommand[0] == "get":

            if splicedcommand[1] == "filelocation":
                tempanswer = checkuseroptions(2)
                print("File location: " + tempanswer)

