from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callback import *

def menu_markup(user_id: int):
    callback_data_primer = PrimerCallback(user_id=user_id)
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Пример", callback_data=callback_data_primer.pack()),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)