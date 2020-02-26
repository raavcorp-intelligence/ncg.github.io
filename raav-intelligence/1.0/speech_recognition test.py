import speech_recognition as SR

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
	try:
		text = r.recognize_google(audioData)
	except ValueError:
		speechOut("I'm sorry I didn't understand you")

	print(text)
	textR = text[:4]
	if textR == "Rave":
		return 0
	else:
		Recognize()
	
Recognize()

