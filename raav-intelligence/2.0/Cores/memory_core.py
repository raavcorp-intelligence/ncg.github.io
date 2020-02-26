# Memory Core
# This is the memory saving feature it saves the question that is asked and it saves the answer that is returned
# Import
import wolframalpha
from moudule_core import Memory, logfiles
from encryption_core import encryptionCore
import os
import wikipedia
import math
import webbrowser
import subprocess
import pyaudio
import pyttsx3
import sys
import time
import math
import requests
filelocation = str(__file__).replace("memory_core.py", "")
question_memory_value =  str(filelocation) + "eQuestion.raavmemory"
answer_memory_value = str(filelocation) + "eMemory.raavmemory"
# Data
app_id = "LQEGLQ-JVJTQP73QA"
#That is the app_id for wolframalpha
Memory = Memory()
# Setting the memory funtion to a more usable state

def memoryStorageWrite(addMEM, MEMquestion):
    indexQuestion = verifyAnswer(MEMquestion, True)
    if indexQuestion == True:
        pass
    else:
        logfiles("adding " + MEMquestion + ", " + addMEM + " to memory")
        addMEM = addMEM.upper()
        addMEM = encryptionCore(addMEM, "E")
        MEMquestion = MEMquestion.upper()
        MEMquestion = encryptionCore(MEMquestion, "E")
        fileMEM = open(answer_memory_value, "a")
        fileMEM.write(">>>" + addMEM)
        fileMEM.write("\n")
        fileMEM.close()
        fileQST = open(question_memory_value, "a")
        fileQST.write(">>>" + MEMquestion)
        fileQST.write("\n")
        fileQST.close()
        #This makes the program run faster by saving the question and answer so if a previously asked question is stored in memory it can pull it up right away.

def verifyAnswer(questioncheck, checkorfind):
    # Log command
    logfiles("Checking memory for " + questioncheck)
    # Getting the indexed entry for the question
    # Passing the ("Question", "question_file_location")
    memCache = Memory.get(questioncheck, question_memory_value)
    # It will either return the entry line number or False, meaning that it could not find it in memory
    if memCache == "null":
        # Couldn't find the entry in memory
        return False
    else:
        # This would be if they just wanted to check if the question was in memory and not get the value
        if checkorfind == True:
            return True
        else:
            # This is if they wanted to get the value of the entry
            memCache += 1
            memoryAnswerMEM = str(encryptionCore(Memory.findvalue(memCache, answer_memory_value), "D"))
            logfiles("Found in memory" + memoryAnswerMEM)
            memoryAnswerMEM = memoryAnswerMEM.lower()
            return memoryAnswerMEM

#memoryStorageWrite("hello", "q3")
#xtemp = Memory.get("q3", question_memory_value)
#xtemp = verifyAnswer("q3", False)
#print(xtemp)