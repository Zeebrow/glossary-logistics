# Singleton class for glossary-logistics
import abbreviation
import definition
import DatabaseWrapper as DB
import csv

class GlossaryLogistics:
    # Start Database
    print("Preparing to run glossary-logistics app.")

    db = DB.GlossaryDatabaseWrapper(csvDataFilePath="../run/Data.csv")
    db.startDatabase()
    db.importDatabase()
    # Load objects from database into memory

    # Start http server, if required

    # Start "application"

    # Clean up

    # Exit
    print("Exiting glossary-logistics app.")
