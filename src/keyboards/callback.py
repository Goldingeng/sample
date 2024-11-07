from aiogram.filters.callback_data import CallbackData


class PrimerCallback(CallbackData, prefix="history"):
    user_id: int



