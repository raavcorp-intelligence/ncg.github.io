#Raav Voice Build 1.0
# 1 MEANS YES 0 MEANS NO
#__________________________Imports___________________________________________
import wolframalpha
import os
import speedtest
import wikipedia
import speech_recognition as SR
import math
import webbrowser
import pyaudio
import pyttsx3
#The imports commented out have not been installed on RaavDesk
#Installed on RaavDesk:
#-wolframalpha
#-math {built in}
#-Wikipedia
#-Speech Recognition
#__________________________Varables__________________________________________
app_id = "LQEGLQ-JVJTQP73QA"
# That is for WolframAlpha
stackurl = "https://stackoverflow.com/search?q="
# for stackoverflow
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# this is for the webbrowser function it would always open in IE
questionsAsked = []
# Big list
#__________________________Definitions_______________________________________
def keyWords(string):	#This will always be learning and storing
	print("Starting keyWords")
	keywordsFile = open("keywords_transfer.txt", "w")
	keywordsFile.write(string)
	keywordsFile.close()
	os.startfile("E:/R.A.A.V/Builds/1.0/keywords.py")

def speechOut(talktext):
	engine = pyttsx3.init()
	engine.say(talktext)
	engine.runAndWait()

"""def speedTest():
	s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    data = res['download']
    data2 = round(data / 1048576)
    return data2
"""
def StackAPI(stackQuestion):
	stackQuestion = stackQuestion.replace(" ", "+")
	stackFinalURL = stackurl + stackQuestion
	webbrowser.get(chrome_path).open(stackFinalURL)
	#opens the stackoverflow url


def memoryStorageWrite(addMEM, MEMquestion):
	fileMEM = open("Memory.txt", "w")
	fileMEM.write(addMEM)
	fileMEM.close()
	fileQST = open("Question.txt", "w")
	fileQST.write(MEMquestion)
	fileQST.close()
	#This makes the program run faster by saving the question and answer so if a previously asked question is stored in memory it can pull it up right away.


"""def memoryStorageReadloadValues(questionAsked):
	fileQA = open("Question.txt", "r")
	fileReadLen = 1
	while fileReadLen > 0:
		tempFileList = file.readline(fileReadLen)
		if tempFileList == "":
			x = 0
		else:
			
			#Big list will store all of the entries of the text file.
			questionsAsked.append(tempFileList)
"""

"""def memoryStorageReadgetValues(QA):
	try:
		if questionsAsked.index(QA):
	except ValueError:
		return 0
"""


def callWolf(wolfQuestion): 
	#Wolfram Alpha Functions
	client = wolframalpha.Client(app_id)
	#validates the client ID
	result = client.query(wolfQuestion)
	#gets the answer to the question
	wolfAnswer = next(result.results).text
	#memoryStorageWrite(wolfAnswer, wolfQuestion)
	#converts the answer to text 
	return wolfAnswer
	#returns answer as x = y()


def FollowUp():
	with mic as source:
		audioData = r.listen(source)
	type(audioData)
	QuestionText = r.recognize_google(audioData)
	return QuestionText


def wikipediaQ(wikiQuestion):
	#Gets the wikipedia input and returns it in 2 sentences
	wikitext = wikipedia.summary(wikiQuestion, sentences=2)
	#memoryStorageWrite(wikitext, wikiQuestion)
	return wikitext
#__________________________MAIN-LOOP_________________________________________


def mainline(QuestionAsked):
	QuestionAsked = QuestionAsked.upper()
	if ("SEARCH STACK OVERFLOW" in QuestionAsked) or ("SEARCH STACKOVERFLOW" in QuestionAsked):
		# There are many diffrent combinations that STACKOVERFLOW could be said in
		if ("SEARCH STACK OVERFLOW FOR" in QuestionAsked):
			SendQuestion = QuestionAsked.replace("SEARCH STACK OVERFLOW FOR ", "")
			StackAPI(SendQuestion)
			#------------------------------------------------------------------------------------
		elif ("SEARCH STACKOVERFLOW FOR" in QuestionAsked):
			SendQuestion = QuestionAsked.replace("SEARCH STACKOVERFLOW FOR", "")
			StackAPI(SendQuestion)
			#------------------------------------------------------------------------------------
		elif ("SEARCH STACK OVERFLOW ABOUT" in QuestionAsked):
			SendQuestion = QuestionAsked.replace("SEARCH STACK OVERFLOW ABOUT", "")
			StackAPI(SendQuestion)
			#------------------------------------------------------------------------------------
		elif ("SEARCH STACKOVERFLOW ABOUT" in QuestionAsked):
			SendQuestion = QuestionAsked.replace("SEARCH STACKOVERFLOW ABOUT", "")
			StackAPI(SendQuestion)
			#------------------------------------------------------------------------------------
		if (len(QuestionAsked) <= 21 ):
			speechOut("What would you like to search?")
			QuestionFollowUp = FollowUp()
			StackAPI(QuestionFollowUp)
	try:
		finalAnswer = callWolf(QuestionAsked)
		print(finalAnswer)
		speechOut(finalAnswer)
	except:
		finalAnswer = wikipediaQ(QuestionAsked)
		print(finalAnswer)
		speechOut(finalAnswer)
		#speechOut("I could not find an answer to that")

r = SR.Recognizer()
#This is for an audio file
#SR.AudioFile('')
mic = SR.Microphone()
#mic.list_microphone_names()
print(".")

def Recognize():
	with mic as source:
		audioData = r.listen(source)
	type(audioData)
	text = r.recognize_google(audioData)
	
	print(text)
	if text[:4] == "Rave":
		xtemp = len(text)
		textToPass = text[5:xtemp]
		print("Starting with: " + textToPass)
		mainline(textToPass)	
	else:
		Recognize()
Recognize()
