from User import User
from VolunteerEvent import VolunteerEvent

rohan = User("RohanAnne", "rohanpassword1234", 30)
underage = User("Underager", "iamunderage", 15)

myEvent = VolunteerEvent("Old people only", "Old people", "Only old people can sign up for this event", "1201 N Broad Street", "No experience necessary, just be old.", 30, 120, "Image of old person.")
myEvent.signUp(rohan)
myEvent.signUp(underage)