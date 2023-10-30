import json
import websockets
import asyncio


async def create_event(event_data):
    # WebSocket server URL

    async with websockets.connect("wss://websockets.rohananne.repl.co/events/") as ws:
        # Construct a message to create an event
        create_event_message = {
            "action": "create_event",
            "data": event_data
        }

        await ws.send(json.dumps(create_event_message))
        response = await ws.recv()
        print("Response: ", response)

async def get_event(event_id):
    async with websockets.connect("wss://websockets.rohananne.repl.co/events/") as ws:
        get_event_message = {
            "action": "get_event",
            "event_id": event_id
        }
        await ws.send(json.dumps(get_event_message))
        response = await ws.recv()
        print("Response: ", response)

async def replace_event(event_id, event_data):
    async with websockets.connect("wss://websockets.rohananne.repl.co/events/") as ws:
        replace_event_message = {
            "action": "update_event",
            "event_id": event_id,
            "data": event_data
        }
        await ws.send(json.dumps(replace_event_message))
        response = await ws.recv()
        print("Response: ", response)


async def delete_event(event_id):
    async with websockets.connect("wss://websockets.rohananne.repl.co/events/") as ws:
        delete_event_message = {
            "action": "delete_event",
            "event_id": event_id
        }
        await ws.send(json.dumps(delete_event_message))
        response = await ws.recv()
        print("Response: ", response)






if __name__ == "__main__":
    # Define the event data (modify this data as needed)
    event_data = {
        "name": "Sample Event",
        "company": "Event Company",
        "description": "This is a test event",
        "address": "324 AP Even Road",
        "experienceNeeded": "No experience required",
        "minimumAge": 18,
        "maximumAge": 99,
        "featuredImage": "event_image.jpg"
    }

    event_id = "653e8beae11a434b5d02372d"

    # Create a new event loop
    loop = asyncio.new_event_loop()

    # Set the newly created event loop as the current event loop
    asyncio.set_event_loop(loop)

    # Run the create_event coroutine with the specified event data
    #loop.run_until_complete(create_event(event_data))
    loop.run_until_complete(get_event(event_id))
    #loop.run_until_complete(replace_event(event_id, event_data))
    #loop.run_until_complete(delete_event(event_id))









