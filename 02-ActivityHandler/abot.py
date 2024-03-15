from botbuilder.core import TurnContext,ActivityHandler
from botbuilder.schema import ActivityTypes,ChannelAccount

class ActivityBot(ActivityHandler):
        #Before we used conditional statements to check turn_context's activity type. 
        # With help of Activity Handler, we use methods such as the ones below. 

        async def on_message_activity(self,turn_context:TurnContext):
            await turn_context.send_activity(turn_context.activity.text)
        async def on_members_added_activity(self,member_added : ChannelAccount,turn_context:TurnContext):
            await turn_context.send_activity("Hello Welcome to Echo Bot")
            # for member in member_added: # What are the members in the member_added?
            #     await turn_context.send_activity(member.name) #Send the member name as a message.
            
        