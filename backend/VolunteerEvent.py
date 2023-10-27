import requests


class VolunteerEvent:
    eventName = None
    company = None
    description = None
    address = None
    latitude = None
    longitude = None
    state = None
    experienceNeeded = None
    minimumAge = None
    maximumAge = None
    featuredImage = None
    formattedAddress = ""

    def __init__(self, eventName, company, description, address, experienceNeeded, minimumAge, maximumAge, featuredImage):
        self.eventName = eventName
        self.company = company
        self.description = description
        self.address = address

        # Implement latitude, longitude, and state code
        url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDVj62Z0jNKH91N4Dk0FBNr5KJ_OvIduSE&address=' + address
        response = requests.get(url).json()
        self.latitude = response['results'][0]['geometry']['location']['lat']
        self.longitude = response['results'][0]['geometry']['location']['lng']
        self.state = response['results'][0]['address_components'][5]['long_name']
        self.formattedAddress = response['results'][0]['formatted_address']
        self.experienceNeeded = experienceNeeded
        self.minimumAge = minimumAge
        self.maximumAge = maximumAge
        self.featuredImage = featuredImage

    def returnTable(self):
        table = {
            "Name": self.eventName,
            "Company": self.company,
            "Description": self.description,
            "Full Address": self.formattedAddress,
            "Latitude": self.latitude,
            "Longitude": self.longitude,
            "State": self.state,
            "Experience Needed": self.experienceNeeded,
            "Minimum Age": self.minimumAge,
            "Maximum Age": self.maximumAge,
            "Featured Image": self.featuredImage}
        return table

    def signUp(self, user):
        if user.age < self.minimumAge or user.age > self.maximumAge:
            print("User age does not meet requirements for this event")
            return

        print(f"{user.username} signed up for {self.eventName}")
        user.addPoints(10)
