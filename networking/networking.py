import json
import threading

import websockets
import asyncio
import uuid as UUID
from websockets.sync.client import connect
import certifi
import ssl

ssl_context = ssl.create_default_context()
ssl_context.load_verify_locations(certifi.where())
class Networking:
    def __init__(self):
        self.queries = []
        self.responses = {}
        self.websocket = None
        self.connect()
        threading.Thread(target=self.update, daemon=True).start()

    def connect(self):
        self.websocket = connect("wss://websockets.rohananne.repl.co/events/", ssl_context=ssl.SSLContext(ssl.PROTOCOL_TLS))

    def close(self):
        if self.websocket is not None:
            self.websocket.close()
            self.websocket = None

    def update(self):
        while True:
            if self.websocket is not None:
                if len(self.queries) > 0:
                    self.websocket.send(json.dumps(self.queries[0][0]))
                    res = json.loads(self.websocket.recv())
                    self.responses[self.queries[0][1]] = res
                    self.queries.pop(0)

                else:
                    self.websocket.send(json.dumps({"action":"keep"}))
                    self.websocket.recv()


    def create_event(self, event_data):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "create_event",
                                 "data": event_data
                             }, ticket))
        return ticket

    def get_event(self, event_id):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "get_event",
                                 "event_id": event_id
                             }, ticket))
        return ticket



    def update_event(self, event_id, event_data):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "update_event",
                                 "event_id": event_id,
                                 "data": event_data
                             }, ticket))
        return ticket

    def get_events_num(self, events_num):
        ticket = str(UUID.uuid4())
        self.queries.append(({
            "action": "get_events_num",
            "event_number" : events_num
        }, ticket))
        return ticket
    
    def getCreatedEvents(self, events_num, username):
        ticket = str(UUID.uuid4())
        self.queries.append(({
            "action" : "get_created_events",
            "event_number" : events_num,
            "username" : username
        }, ticket))
        return ticket

    def getRegisteredEvents(self, events_num, userID):
        ticket = str(UUID.uuid4())
        self.queries.append(({
            "action" : "get_registered_events",
            "event_number" : events_num,
            "userID" : userID
        }, ticket))
        return ticket
        
    def delete_event(self, event_id):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "delete_event",
                                 "event_id": event_id
                             }, ticket))
        return ticket

    def update_and_request_player(self, player_data):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "updateAndRequestPlayer",
                                 "player_data":player_data
                             }, ticket))
        return ticket

    def login(self, username, pw):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "login",
                                 "username":username,
                                 "password":pw
                             }, ticket))
        return ticket

    def signup(self, username, pw):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "signup",
                                 "username":username,
                                 "password":pw
                             }, ticket))
        return ticket

    def retrieve_data(self, username):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "retrieveUserData",
                                 "username":username
                             }, ticket))
        return ticket

    def set_user_data(self, id, data):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "setUserData",
                                 "player_id":id,
                                 "data":data
                             }, ticket))
        return ticket

    def signupEvent(self, eventName, id):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "signupEvent",
                                 "event_name":eventName,
                                 "user_id":id
                             }, ticket))
        return ticket

    def getEventUsers(self, eventName):
        ticket = str(UUID.uuid4())
        self.queries.append(({
                                 "action": "getEventUsers",
                                 "event_name":eventName
                             }, ticket))
        return ticket

if __name__ == "__main__":
    # Define the event data (modify this data as needed)
    event_data = {
        "name": "Library Help",
        "company": "CCLS",
        "description": "Help the library in\nencouraging people to read",
        "address": "720 First Avenue Berwyn PA",
        "experienceNeeded": "No experience required!",
        "minimumAge": 12,
        "maximumAge": 18,
        "featuredImage": "https://www.tesd.net/cms/lib/PA01001259/Centricity/ModuleInstance/17529/large/01_01____static.jpg"
    }


    netw = Networking()
    netw.create_event(event_data)
    # #ticket0 = netw.getCreatedEvents(5, "RohanAnne")
    # ticket = netw.getRegisteredEvents(5, "6541730a15f4babb040385b9") # netw is Networking object, send query data
    # while ticket not in netw.responses: # wait until response is received
    #     # do something here like make a loading sign
    #     pass
    # print(netw.responses[ticket]['data']) # retrieve data










