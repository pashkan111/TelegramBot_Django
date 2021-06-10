from aiogram.dispatcher.filters.state import StatesGroup, State


class AdvertisementState(StatesGroup):
    name = State()
    description = State()
    price = State()
    sales_price = State()
