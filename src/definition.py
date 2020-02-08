# Define a word with a definition

class Definition:
    def __init__(self, phrase, defn=''):
        self.phrase = phrase
        self.defn = defn

    def getDefn(self):
        return self.defn

    def updateDefn(self, newDefn):
        self.defn = newDefn
        return self.defn
