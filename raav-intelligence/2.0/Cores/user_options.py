import json
jsonLocation = __file__
jsonLocation = jsonLocation.replace("user_options.py", "")
def checkuseroptions(option):
    f = open(jsonLocation + "user_options.json", "r")
    useroptions = f.read()
    jsonoptions = json.loads(useroptions)
    tempoption = jsonoptions[str(option)]
    f.close()
    return tempoption

def editfilelocation(filelocation):
    f = open(jsonLocation + "user_options.json", "r+")
    data = json.load(f)
    data["2"] = str(filelocation)
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
    f.close()

def editvalue(optionx, newvalue):
    f = open(jsonLocation + "user_options.json", "r+")
    data = json.load(f)
    data[optionx] = newvalue
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()
    f.close()
