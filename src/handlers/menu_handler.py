from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import InputMediaPhoto

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.users import User
from src.keyboards import menu_markup

from src.keyboards.callback import *


from datetime import datetime, timedelta

from aiogram.types import InputMediaPhoto

menu_router = Router(name="menu")


@menu_router.message(Command("menu"))
async def menu_handler(message: Message, session: AsyncSession) -> None:
    user = await User.get(session=session, user_id=message.from_user.id)
        
    await message.answer("Меню", 
        reply_markup=menu_markup(message.from_user.id), parse_mode="HTML", 
    )
