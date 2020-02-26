QA = ">>>" + QA
    if questionsAsked.index(QA):
	    for listItem in questionsAsked:
		for index, x in enumerate(questionsAsked):
			if x == listItem:
				index = index + 1
				return index
    else:
	return False
