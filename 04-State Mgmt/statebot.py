from botbuilder.core import (
    ActivityHandler,
    TurnContext,
    UserState,
    ConversationState
)

from data_model import ConState, UserProfile, EnumUser

class StateBot(ActivityHandler):
    """ Custom bot class that handles user input and updates the user profile."""
    def __init__(self,constate:ConversationState,userstate:UserState):
        self.constate = constate
        self.userstate = userstate

        self.conprop = self.constate.create_property("constate")
        self.userprop = self.userstate.create_property("userstate")

    # Implement the on_turn method to save changes to the conversation and user state 
    async def on_turn(self, turn_context: TurnContext):
        await super().on_turn(turn_context)
        await self.constate.save_changes(turn_context)
        await self.userstate.save_changes(turn_context)
        

    # Implement the on_message_activity method to handle user input and update the user profile.
    async def on_message_activity(self, turn_context: TurnContext):
        # Get the current state of the conversation and user profile.
        conmode = await self.conprop.get(turn_context,ConState)
        usermode = await self.userprop.get(turn_context,UserProfile)
        
        # Handle user input based on the current state of the conversation.
        if(conmode.profile == EnumUser.NAME):
            # Prompt the userto enter their name.
            await turn_context.send_activity("Enter the name ")
            conmode.profile = EnumUser.PHONE
        

        elif(conmode.profile == EnumUser.PHONE):
            # Update the user profile with the user's name.
            usermode.name = turn_context.activity.text
            await turn_context.send_activity("Enter phone number")
            conmode.profile = EnumUser.EMAIL
        
        elif(conmode.profile == EnumUser.EMAIL):
            # Update the user profile with the user's phone number.
            usermode.phone = turn_context.activity.text
            await turn_context.send_activity("Enter Email Id")
            conmode.profile = EnumUser.DONE
        
        elif(conmode.profile == EnumUser.DONE):
            # Update the user profile with the user's email.
            usermode.email = turn_context.activity.text
            info = usermode.name + " " + usermode.phone + " " + usermode.email
            await turn_context.send_activity(info)



    






    