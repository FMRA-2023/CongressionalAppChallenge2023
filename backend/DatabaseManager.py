from VolunteerEvent import VolunteerEvent
import pymongo
import certifi


class DatabaseManager:
    volunteerClient = pymongo.MongoClient(
        "mongodb+srv://FMRA:CongressionalAppChallenge2023@cluster0.oqikimn.mongodb.net/?retryWrites=true&w=majority")
    volunteeringDatabase = volunteerClient["VolunteeringDatabase"]
    volunteeringEvents = volunteeringDatabase["VolunteerEvents"]
    ca = certifi.where()


    def insertData(self, volunteerEvent):
        self.volunteeringEvents.insert_one(volunteerEvent.returnTable())

    def updateData(self, volunteerEventName, newTable):
        self.volunteeringEvents.replace_one({"Name" : volunteerEventName}, newTable)


    def deleteData(self, volunteerEventName): # HELPER FUNCTION ONLY, DONT USE IN ACTUAL APP
        myquery = {"Name" : volunteerEventName}
        self.volunteeringEvents.delete_one(myquery)

"""
Testing DatabaseManager Class

databaseEvent = VolunteerEvent("Database Event", "Database Inc.", "This is an event to help people create databases.", "324 AP Even Road",
                           "Must be able to work with computers and know how databases and APIs work.", 0, 50, "Database Image")

ca = certifi.where()

print(databaseEvent.latitude)
print(databaseEvent.longitude)
print(databaseEvent.state)

db = DatabaseManager()
db.updateData("FMRA Event", databaseEvent.returnTable())
"""









