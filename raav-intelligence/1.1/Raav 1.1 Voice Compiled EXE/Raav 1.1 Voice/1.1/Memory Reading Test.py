question_memory_value = "Question.raavmemory"
answer_memory_value = "Memory.raavmemory"


class Memory:
	# This calss is the memory reading and indexing part 
	def __init__(self, memsave, memrestore, x, x1):
		self.x = x
		self.x1 = x1
		self.memsave = memsave
		self.memrestore = memrestore
		x = []
		x1 = []

	def getx(self, QAtoget):
		filepathx1 = question_memory_value
		# The try checks to see if the Question Exists
		try:
			open(filepathx1)
		except ValueError:
			open(filepathx1, "w+")
		x = []
		# This opens the Question file to get all of the saved values
		with open(filepathx1) as fp:
			linex1 = fp.readline()
			count = 1
			while linex1:
				x.append(linex1.strip())
				linex1 = fp.readline()
				count += 1
		
		QAtoget = ">>>" + QAtoget
		if QAtoget in x:
			#This is the indexing part `itemplacement` is the varable that shows what entry the question is on
			itemplacement = x.index(QAtoget)
			return itemplacement
		else:
			return False
	def findvalue(self, numlist):
			x1 = []
			#This is the file read in part where we see the memory that is stored
			filepathx2 = answer_memory_value
			with open(filepathx2) as fp:
				linex2 = fp.readline()
				count = 1
				while linex2:
					x1.append(linex2.strip())
					linex2 = fp.readline()
					count += 1
			#This is condesing the >>>QUESTION to just QUESTION
			numlist = numlist - 1
			returningvaluecondence = x1[numlist]
			memoryvaluecondeser = returningvaluecondence[3:len(returningvaluecondence)]
			return memoryvaluecondeser

def verifyAnswer(questioncheck):
	print("passed")
	memtemp = Memory.getx("", questioncheck)
	if memtemp == False:
		return False
	else:
		memoryRestoreAnswer = Memory.findvalue("", memtemp)
		print(memoryRestoreAnswer)
		return True
		


b = "who is abraham lincoln"
b = b.upper()

a = verifyAnswer(b)
print(a)

def memoryStorageWrite(addMEM, MEMquestion):
	#indexQuestion = memoryStorageReadgetValues(MEMquestion)
	#if indexQuestion == True:

	fileMEM = open("Memorytest.raavmemory", "a")
	fileMEM.write(">>>" + addMEM)
	fileMEM.write("\n")
	fileMEM.close()
	fileQST = open("Questiontest.raavmemory", "a")
	fileQST.write(">>>" + MEMquestion)
	fileQST.write("\n")
	fileQST.close()


#memoryStorageWrite("raava", "hello")


