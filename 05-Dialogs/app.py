from flask import Flask,request,Response
# Import necessary classes and functions for the Microsoft Bot Framework SDK
from botbuilder.schema import Activity
from botbuilder.core import (
    BotFrameworkAdapter,
    BotFrameworkAdapterSettings,
    ConversationState,
    UserState,
    MemoryStorage 
)

import asyncio
from bot_dialog import BotDialog

app = Flask(__name__)
loop = asyncio.get_event_loop()

botadaptersettings = BotFrameworkAdapterSettings("","")
botadapter = BotFrameworkAdapter(botadaptersettings)

memstore = MemoryStorage()
constate = ConversationState(memstore)

ebot = BotDialog(constate)

# Define the route for incoming HTTP requests
@app.route("/api/messages",methods=["POST"])
def messages():
    # Check if the request content type is JSON
    if "application/json" in request.headers["content-type"]:
      jsonmessage = request.json
    else:
      # Return a 415 Unsupported Media Type response
      return Response(status=415)
   
    # Deserialize the JSON message into an Activity object
    activity = Activity().deserialize(jsonmessage)

    auth_header = (request.headers['Authorization'] if "Authorization" in request.headers else "")



    # Define the async function for processing the activity
    # Call the on_turn method of the custom StateBot object
    async def turn_call(turn_context):
        await ebot.on_turn(turn_context)

    task = loop.create_task(botadapter.process_activity(activity,auth_header,turn_call))
    # Run the event loop until the task is completed
    loop.run_until_complete(task)

if __name__ == '__main__':
    app.run('localhost',3978)
