from botbuilder.core import TurnContext

class EchoBot: 
#The on_turn method of the EchoBot class is the callback function that is passed to the process_activity method. 
#   This method is called whenever a new activity is received. It simply echoes the received message back to the user.    
    async def on_turn(self,turn_context:TurnContext): 
        await turn_context.send_activity(turn_context.activity.text)
