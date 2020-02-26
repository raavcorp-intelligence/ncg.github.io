wikiQuestion = "what is a mac"
import wikipedia
#Gets the wikipedia input and returns it in 2 sentences
wikitext = wikipedia.summary(wikiQuestion, sentences=2)
wikialltext = wikipedia.summary(wikiQuestion)
#adds the answer to storage
wikitext = "from the website wikipedia, " + str(wikitext)
print(wikitext)

