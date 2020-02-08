# Class to define an abreviation


class Abbreviation:
    def __init__(self, abv, phrase, defn=""):
        self.abv = abv
        self.phrase = phrase
        self.defn = defn

    def getAbv(self):
        print("{0}: {1}".format(self.abv, self.phrase))
        return self.phrase

    def updateDefn(self, newDefn):
        self.defn = newDefn
        return true

    def updatePhrase(self, newPhrase):
        self.phrase = newPhrase
        return true

    # def _isAcceptableDefn(defnToCheck):
    #     if defnToCheck

    # def create(self, newAbv, newDefn=""):
    #     self.abv = newAbv
    #     print("New abbreviation!")
    #
    # def remove(self):
    #     pass
    #
    # def update(self):
    #     pass
