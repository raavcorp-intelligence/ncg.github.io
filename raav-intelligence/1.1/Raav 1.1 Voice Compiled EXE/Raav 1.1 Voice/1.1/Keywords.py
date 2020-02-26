class Keywords:
    def __init__(self):
        placeholder = True
        # So this is kinda like a analization program
        # It will break up each word and it will analize it
        # We need a condition that will dod something whether it is a who, what, where, why, and how keywords.
    def analyze(self, keypartword):
        keysplitword = keypartword.split(" ")
        print(keysplitword)
        if "is" in keysplitword:
            typeofquestion = "Boolean"
        





