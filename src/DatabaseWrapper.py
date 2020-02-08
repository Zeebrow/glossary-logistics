# Glossary Database object
#
# The Glossary Database is a collection phrases and descriptors.
# A phrase is a word of short collection of words to be defined and stored.
# A collection of a phrase, abreviation, and definition, is an Entry.
# Each Entry is uniquely identified by an index, and (future) may be linked to
# other references other Entries specified in the "see-also" field (list of indecies).
#

import os, csv, time
class GlossaryDatabaseWrapper:
    def __init__(self, csvDataFilePath):
        self.csvDataFilePath = csvDataFilePath

    def startDatabase(self):
        # If database doesn't exist, create a new one (ask to continue?)
        if not(os.path.exists(self.csvDataFilePath)):
            print("No database was found at \"{0}\". Creating new...".format(self.csvDataFilePath))
            self.initDatabase()

    def initDatabase(self, _csvHeaderRow = ["index,abv,phrase,defn"]):
        # _csvHeaderRow = ["abv", "phrase", "defn"]
        with open(self.csvDataFilePath, 'w+') as c:
            writer = csv.writer(c, delimiter="\n", quoting = csv.QUOTE_NONE)
            writer.writerow(_csvHeaderRow)
        print("Finished loading csv Data.")
        return True

    def importDatabase(self, csvFileToImport=""):
        csvFileToImport = self.csvDataFilePath
        _beginTime=time.time()
        print("Beginning import of {0}...".format(csvFileToImport))
        time.sleep(2) #Make believe you're real programmer!
        _endTime=time.time()
        print("Finished importing in {0} seconds.".format(_endTime-_beginTime))

    def exportDatabase(self, pathToExport="."):
        #Determine path and filename of export

        #Write header to export file
        with open(self.csvDataFilePath, 'w+') as c:
            writer = csv.writer(c, delimiter="\n", quoting = csv.QUOTE_NONE)
            writer.writerow(_csvHeaderRow)
        print("Finished exporting data to {0}")

        #Begin exporting database

        # Return true on success
        return True
