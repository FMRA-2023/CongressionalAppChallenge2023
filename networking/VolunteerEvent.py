import os
import json
from sanic import Sanic
from sanic.response import json as sanic_json
import motor.motor_asyncio
from bson import ObjectId
from bson import json_util
import requests


class VolunteerEvent():
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

  def __init__(self, eventName, company, description, address,
               experienceNeeded, minimumAge, maximumAge, featuredImage):
    self.eventName = eventName
    self.company = company
    self.description = description
    self.address = address
    self.signups = []

    # Implement latitude, longitude, and state code
    url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyDVj62Z0jNKH91N4Dk0FBNr5KJ_OvIduSE&address=' + address
    response = requests.get(url).json()

    if response['status'] == 'OK':
      result = response['results'][0]
      self.latitude = result['geometry']['location']['lat']
      self.longitude = result['geometry']['location']['lng']
      self.state = None
      self.formattedAddress = result['formatted_address']
      for component in result['address_components']:
        if 'administrative_area_level_1' in component['types']:
          self.state = component['long_name']

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
        "Featured Image": self.featuredImage,
        "IDs" : self.signups
    }
    return table

  def JSONString(self):
    return json.dumps(self.returnTable())
  
  def sign_up(self, user):
    user.sign_up_event(self)
    print(f"{user.username} signed up for {self.eventName}")
    user.addPoints(10)

