from botbuilder.core import Middleware, TurnContext
from typing import Callable, Awaitable

class Middleware1(Middleware):
    async def on_turn(self,turn_context:TurnContext,next:Callable[[TurnContext],Awaitable]):
        await turn_context.send_activity("Hey I am Middleware 1")
        await next() #the Next method will call the bot to perform it's logic.
        await turn_context.send_activity("called after the bot function")

