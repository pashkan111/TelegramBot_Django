from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


choice = InlineKeyboardMarkup(row_width=2)

assign = InlineKeyboardButton(text='Указать', callback_data='assign')
choice.insert(assign)

reject = InlineKeyboardButton(text='Отклонить', callback_data='reject')
choice.insert(reject)

link_to_mainpage = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Перейти на страницу с объявлениями", url='http://127.0.0.1:8000/home/')
    ]
])
