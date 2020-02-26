#Raav Voice Build 1.1
# 1 MEANS YES 0 MEANS NO
#__________________________USER OPTIONS______________________________________
TalkToProgram = False       # If you want to use the speech recognition moudule or just the type command
# Change that to true or false
#__________________________Imports___________________________________________
import wolframalpha
import os
from moudule_core import Memory, logfiles, internet_check, offlinemodecheck
from memory_core import verifyAnswer
from information_core import wikipediax, callWolf, stackoverflowcall
from user_options import checkuseroptions, editfilelocation
from terminal_core import terminal
#from Keywords import 
#import speedtest
import wikipedia
import speech_recognition as SR
import math
import webbrowser
import subprocess
#import pyaudio
import pyttsx3
import sys
import time
import math
import requests
import base64
import pathlib
#The imports commented out have not been installed on RaavDesk
#Installed on RaavDesk:
#-wolframalpha
#-math {built in}
#-Wikipedia
#-Speech Recognition
#__________________________THE OUTPUT________________________________________
file_path = pathlib.Path(__file__).resolve()
pythonfilelocation = str(file_path.parent)
editfilelocation(pythonfilelocation)
#__________________________Varables__________________________________________
app_id = "LQEGLQ-JVJTQP73QA"
# That is for WolframAlpha
stackurl = "https://stackoverflow.com/search?q="
# for stackoverflow
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# this is for the webbrowser function it would always open in IE
question_memory_value = "Question.raavmemory"
answer_memory_value = "Memory.raavmemory"
# Big list
# Preneeded code
# Defintion of Mic
r = SR.Recognizer()
#This is for an audio file
#SR.AudioFile('')
try: 
    mic = SR.Microphone()
except:
    computerUsingMic = False
#mic.list_microphone_names()
Memory = Memory()
#Keywordx = Keywords()
offlinemode = False 

logfiles("---------------STARTED NEW RUN OF PROGRAM----------------")
#__________________________MAIN-LOOP_________________________________________


def mainline(QuestionAsked, programIsOffline):
    # this is just to check to make sure that the command isnt just `exit`
    print(QuestionAsked)
    if QuestionAsked == "exit":
        logfiles("Exiting")
        sys.exit()
    # Terminal Function to be added soon :)
    if QuestionAsked == "terminal":
        logfiles("terminal opened")
        terminal()
    tryfail = 0
    # Making the question entry Uppercase
    QuestionAsked = QuestionAsked.upper()
    logfiles("Checking Memory")
    checkanswerfromverify = verifyAnswer(QuestionAsked, False)
    # This will try to see if the command is answerable by wolframalpha and/or wikipedia
    # The "checkanswerfromverify" checks to make sure that the question isnt in memory
    if checkanswerfromverify != False:
        Memory.Output(checkanswerfromverify)
        # Exit search protocal from answer in memory
    elif checkanswerfromverify == False:
        if programIsOffline == False:
            logfiles("trying wolframalpha for answer to " + QuestionAsked)
            finalAnswer = callWolf(QuestionAsked)
            if finalAnswer == "noint":    
                try:
                    logfiles("trying wikipedia for answer to " + QuestionAsked)
                    finalAnswer = wikipediax(QuestionAsked)
                    tryfail += 1
                except:
                    logfiles("failed wikipedia")
            else:
                Memory.Output(finalAnswer)
            placeholder = True
            if tryfail == 0:
                if checkanswerfromverify == True:
                    pass
                elif checkanswerfromverify == False:
                    Memory.Output("I could not find an answer to that")
        if programIsOffline == True:
            Memory.Output("You are in offline mode and I cannot get anything from the internet right now")
            refresh_offline_mode = input("Re-Check for internet? y/n ")
            if refresh_offline_mode == "y":
                offlinemode = internet_check()
                if programIsOffline == True:
                    Memory.Output("You are still offline")
                    sys.exit()
                if programIsOffline == False:
                    Memory.Output("Back online")
                    sys.exit()


        
#--------------------------Code------------------------------------------
# Offline Mode check, since the internet check takes so long to go and return I have set this up so it only runs everynow and then

offlinemode = offlinemodecheck()
print("Offline: " + str(offlinemode))
typeortalk = checkuseroptions(1)
if typeortalk == "False": 
    textToPass = input("Command: ")
    logfiles("Question: " + textToPass)
    mainline(textToPass, offlinemode)
