# this is the seprate starter for the main core
from user_options import checkuseroptions
from moudule_core import logfiles
from raavcore import mainline, offlinemode
def ONSTART():
    typeortalk = checkuseroptions(1)
    if typeortalk == "False": 
        textToPass = input("Command: ")
        textToPass = str(textToPass)
        logfiles("Question: " + textToPass)
        mainline(textToPass, offlinemode)

while True:
    ONSTART()
print("Finished")