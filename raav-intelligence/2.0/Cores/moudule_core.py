import pyttsx3
import os
import time
import sys
import datetime
import speedtest
from user_options import checkuseroptions, editvalue
from encryption_core import encryptionCore
import pathlib
import base64
import nltk
loglocation = "log.raavlog"

def logfiles(logentry):
    global log
    log = []
    logentry.replace("\n", " ")
    timenow = datetime.datetime.now()
    logfinalvalue = ">>> Command: " + logentry + " at " + str(timenow)
    filelog = open(loglocation, "a")
    filelog.write(logfinalvalue)
    filelog.write("\n")
    filelog.close()


class Memory:
# This class is the memory reading and indexing part 
    def __init__(self):
        placeholder = True

    def get(self, questionToGet, question_memory_value):
        filepath = question_memory_value
        # The try checks to see if the Question Exists
        # Trying to open the file and seeing if it exists
        questionToGet = questionToGet.upper()
        try:
            open(filepath)
        except ValueError:
            open(filepath, "w+")
        # Temp file list
        cacheList = []
        # This opens the Question file to get all of the saved values
        with open(filepath) as fp:
            cacheLine = fp.readline()
            count = 1
            while cacheLine:
                # This is adding the contents of the memory file to a list to be indexed.
                tempLine = cacheLine.strip()
                cacheList.append(tempLine)
                cacheLine = fp.readline()
                count += 1
        # Encrypting the question to be able to compare
        questionToGet = encryptionCore(questionToGet, "E")
        questionToGet = ">>>" + questionToGet
        if questionToGet in cacheList:
            # This is the indexing part `itemPlacement` is the varable that shows what entry the question is on
            # It returns the number entry on the list
            itemPlacement = cacheList.index(questionToGet)
            # This returns the NUMBER as an int, so it can be found in the memory file.
            return itemPlacement 
        else:
            return "null"
    def findvalue(self, numlist, answer_memory_value):
        memoryCached = []
        # This is where we find the value of memory in the memory file
        filepath = answer_memory_value
        # Adding the contense of the files to a list
        with open(filepath, encoding="ISO-8859-1") as fp:
            tempLine = fp.readline()
            count = 1
            while tempLine:
                memoryCached.append(tempLine.strip())
                tempLine = fp.readline()
                count += 1
        # This is condesing the >>>QUESTION to just QUESTION
        numlist = numlist - 1
        # ^ that syncs the indexed value to the python weird (lists start at zero thing)
        returningvaluecondence = memoryCached[numlist]
        # That removes the >>> in the front of the args
        memoryvaluecondeser = returningvaluecondence[3:len(returningvaluecondence)]
        # Un-Encrypting the string
        encryptionCore(memoryvaluecondeser, "D")
        return memoryvaluecondeser

    def Output(self, talktext):
        logfiles("Outputing: " + talktext)
        engine = pyttsx3.init()
        talktext = talktext + "\n"
        print(talktext)
        engine.say(talktext)
        engine.runAndWait()
        


def speedTest():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    data = res['download']
    data2 = round(data / 1048576)
    return data2
def internet_check():
    try:
        internet_speed = speedTest()
        if internet_speed >= 1:
            offlinemodex = False
        else:
            offlinemodex = True
    except:
        offlinemodex = True
        placeholder = 0
    offlinemodex = str(offlinemodex)
    logfiles(offlinemodex)
    return offlinemodex
def followUp():
    typeortalk = checkuseroptions(1)
    if typeortalk == "False":
        textToPass = input("Response: ")
        textToPass = textToPass.upper()
        return textToPass
def concat(a, b):
    return int(f"{a}{b}")
def offlinemodecheck():
    offline = os.system("ping www.google.com -t 2")
    if offline == 0:
        return False
    if offline == 1:
        return True

def questionCondensation(string):
    wordsList = []
    descrpList = []
    tokens = nltk.word_tokenize(string)
    # print(tokens)
    tagged = nltk.pos_tag(tokens)
    for tag in tagged:
        subTag = tag[0]
        wordsList.append(subTag)
        subTag = tag[1]
        descrpList.append(subTag)



