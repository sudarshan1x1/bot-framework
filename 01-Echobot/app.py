# A bot is a web application
#A Bot needs a framework to run. In C# is ASP.NET core is required. For TypeScript Node.js is required. 
# In Python we require Flask to Run the application

from flask import Flask, request, Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter,BotFrameworkAdapterSettings

#The use of asyncio is to enable concurrent execution of asynchronous tasks.
#It provides high-level APIs to run Python coroutines concurrently and have full control over their execution. 
import asyncio

from echobot import EchoBot


app = Flask(__name__)
loop = asyncio.get_event_loop()

#Initializing Variables
botadaptersettings = BotFrameworkAdapterSettings("","")
botadapter = BotFrameworkAdapter(botadaptersettings)

ebot = EchoBot()

@app.route("/api/messages", methods=["POST"])
def messages():
    # We have to check whether HTTP header content type is JSON or not.
    if "application/json" in request.headers['content-type']:
        jsonmessage = request.json
    else : 
        return Response(status=415) #415 - Unsupported media type.

# Next JSON has to be converted to an Activity to send it to the Adapter Turn Context. 
# Activity is a schema of the bot framework
    activity = Activity().deserialize(jsonmessage) #Our Activity object is ready

    async def turn_call(turn_context):
        await ebot.on_turn(turn_context)

#The process_activity method is an asynchronous method that takes an Activity object and a callback function as parameters. 
#It processes the incoming activity and calls the callback function with the TurnContext object.    
#Now this activity object is passed to Adapter, Turn Context using ProcessActivity method.
    task = loop.create_task(botadapter.process_activity(activity,"", turn_call))
    loop.run_until_complete(task)
    
if __name__== '__main__':
    app.run('localhost',port=3978)
