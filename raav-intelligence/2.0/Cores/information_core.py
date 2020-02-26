# Information Core
# Import
import wolframalpha
from moudule_core import Memory, logfiles, followUp
from memory_core import memoryStorageWrite
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
from googlesearch import search

# Data
app_id = "LQEGLQ-JVJTQP73QA"
#That is the app_id for wolframalpha
Memoryx = Memory()
# Setting the memory funtion to a more usable state
stackurl = "https://stackoverflow.com/search?q="
# for stackoverflow
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
# this is for the webbrowser function it would always open in IE
#-----------------------------Defintions----------------------------------
def StackAPI(stackQuestion):
		stackQuestion = stackQuestion.replace(" ", "+")
		stackFinalURL = stackurl + stackQuestion
		webbrowser.get(chrome_path).open(stackFinalURL)
		#opens the stackoverflow url
	

def stackoverflowcall(QuestionAsked):
	if ("SEARCH STACK OVERFLOW" in QuestionAsked) or ("SEARCH STACKOVERFLOW" in QuestionAsked):
		# There are many diffrent combinations that STACKOVERFLOW could be said in
		if ("SEARCH STACK OVERFLOW FOR" in QuestionAsked):
			SendQuestion = QuestionAsked.replace("SEARCH STACK OVERFLOW FOR ", "")
			StackAPI(SendQuestion)
		elif ("SEARCH STACKOVERFLOW FOR" in QuestionAsked):
			SendQuestion = QuestionAsked.replace("SEARCH STACKOVERFLOW FOR", "")
			StackAPI(SendQuestion)
		elif ("SEARCH STACK OVERFLOW ABOUT" in QuestionAsked):
			SendQuestion = QuestionAsked.replace("SEARCH STACK OVERFLOW ABOUT", "")
			StackAPI(SendQuestion)
		elif ("SEARCH STACKOVERFLOW ABOUT" in QuestionAsked):
			SendQuestion = QuestionAsked.replace("SEARCH STACKOVERFLOW ABOUT", "")
			StackAPI(SendQuestion)
# Stack overflow search funtion

def wikipediax(wikiQuestion):
	wikiQuestion = wikiQuestion.lower()
	#Gets the wikipedia input and returns it in 2 sentences
	try:
		wikitext = wikipedia.summary(wikiQuestion, sentences=2)
		fullwikitext = wikipedia.summary(wikiQuestion, sentences=4)
		nowikianswer = False
	except:
		nowikianswer = True
	if len(wikitext) < len(fullwikitext):
		wikitext = "from the website wikipedia, " + wikitext
		memoryStorageWrite(wikitext, wikiQuestion)
		Memoryx.Output(wikitext + " would you like to hear more?")
		userresponse = followUp()
		# ADD IN LATER KEYWORDS FEATURE TO DETECT DIFFRENT VARIATIONS OF ANSWER
		if userresponse == "YES":
			fullwikitext = fullwikitext.replace(wikitext, "")
			Memoryx.Output("The rest says, " + fullwikitext)
		else:
    			Memoryx.Output("Yes sir")
	else:
		wikitext = "from the website wikipedia, " + wikitext
		memoryStorageWrite(wikitext, wikiQuestion)
		return wikitext
		
# Wikipedia search function

def callWolf(wolfQuestion): 
	#logfiles("Checking " + wolfQuestion + "on Wolframalpha")
	wolfQuestion = wolfQuestion.lower()
	#Wolfram Alpha Functions
	client = wolframalpha.Client(app_id)
	#validates the client ID
	result = ""
	try:
		result = client.query(wolfQuestion)
	except:
		return "noint"
	#gets the answer to the question
	wolfFinalAns = ""
	wolfAnswer = next(result.results).text
	if result != "noint":
		try:
			# Checking if it can be converted to a number
			wolfAnswer = int(wolfAnswer)
		except:
			return "noint"
	print(wolfFinalAns)
	memoryStorageWrite(wolfFinalAns, wolfQuestion)
	return wolfFinalAns
	#returns answer as x = y()
# Wolframalpha Search function
#callWolf("20 times 10 to the 30th in scientific notation")
#callWolf("graph x^2 + 3")