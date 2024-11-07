from aiogram import F
from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware

class FloodMiddleware(BaseMiddleware):
    def __init__(self, rate_limit=15, interval=30):
        super().__init__()
        self.rate_limit = rate_limit
        self.interval = interval
        self.user_requests = {}
        self.user_warned = {}

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        now = event.date

        if user_id in self.user_requests:
            requests = self.user_requests[user_id]

            requests = [req for req in requests if (now - req).total_seconds() <= self.interval]

            if len(requests) >= self.rate_limit:

                if not self.user_warned.get(user_id, False):
                    await event.reply("Вы слишком часто используете команду. Подождите немного и попробуйте снова.")
                    self.user_warned[user_id] = True 
                return
            
            requests.append(now)
            self.user_requests[user_id] = requests

            self.user_warned[user_id] = False
        else:
            self.user_requests[user_id] = [now]
            self.user_warned[user_id] = False

        return await handler(event, data)

