fileMEM = open("Memory.raavmem", "a")
new_string = "hello"
fileMEM.write(new_string)
fileMEM.write("\n")
fileMEM.close()

fileMEM = open("Memory.raavmem", "r")
x = fileMEM.readline()
print(x)
fileMEM.close()


