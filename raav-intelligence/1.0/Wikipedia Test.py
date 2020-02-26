import wikipedia
Question = input("Question: ")
print(wikipedia.summary(Question, sentences=2))
