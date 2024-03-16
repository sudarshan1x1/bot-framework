
from botbuilder.core import ActivityHandler,TurnContext,ConversationState, MessageFactory
from botbuilder.dialogs import DialogSet,WaterfallDialog,WaterfallStepContext
from botbuilder.dialogs.prompts import (
    TextPrompt,
    NumberPrompt,
    PromptOptions
)

#The BotDialog class initializes a new conversation state, creates a dialog set, and adds several dialogs to it
class BotDialog(ActivityHandler):
#Initializes the conversation state, creates a dialog set, and adds the necessary dialogs to it    
    def __init__(self, conversation:ConversationState):
        self.con_state = conversation
        
        self.state_prop = self.con_state.create_property("dialog_set")
        
        self.dialog_set = DialogSet(self.state_prop)
        
        self.dialog_set.add(TextPrompt("text_prompt"))
        self.dialog_set.add(NumberPrompt("number_prompt"))
        self.dialog_set.add(WaterfallDialog("main_dialog",[self.getname, self.getno, self.getemail_id, self.completed]))

# Prompts the user to enter their name and returns the user's input.
    async def getname(self, waterfall_step: WaterfallStepContext):
        return await waterfall_step.prompt("text_prompt", PromptOptions(prompt= MessageFactory.text("Please enter the name")))

# Prompts the user to enter their mobile number and returns the user's input.
    async def getno(self, waterfall_step: WaterfallStepContext):
        name = waterfall_step._turn_context.activity.text
        waterfall_step.values["name"] = name
        return await waterfall_step.prompt("number_prompt", PromptOptions(prompt=MessageFactory.text("Please enter the mobile number")))

# Prompts the user to enter their email address and returns the user's input.
    async def getemail_id(self, waterfall_step: WaterfallStepContext):
        mobile = waterfall_step._turn_context.activity.text
        waterfall_step.values['mobile'] = mobile
        return await waterfall_step.prompt("text_prompt", PromptOptions(prompt=MessageFactory.text("Please enter the email id")))

# Combines the user's input from the previous steps and sends a summary message to the user.   
    async def completed(self,waterfall_step: WaterfallStepContext):
        email = waterfall_step._turn_context.activity.text
        waterfall_step.values['email'] = email
        name = waterfall_step.values['name']
        mobile = waterfall_step.values['mobile']
        mail = waterfall_step.values['email']
        profileinfo = f"name: {name}, Email : {mail}, mobile: {mobile}"
        await waterfall_step._turn_context.send_activity(profileinfo)
        return await waterfall_step.end_dialog()
    
#Handles each turn of the conversation by creating a dialog context and either continuing the current dialog or starting a new one
    async def on_turn(self, turn_context: TurnContext):
        dialog_context = await self.dialog_set.create_context(turn_context)
        
        if (dialog_context.active_dialog is not None):
            await dialog_context.continue_dialog()

        else:
            await dialog_context.begin_dialog("main_dialog")
# A method that saves changes to the conversation state.
        await self.con_state.save_changes(turn_context)
    



    

