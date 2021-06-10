from aiogram import types
from aiogram.dispatcher import FSMContext
from asgiref.sync import sync_to_async
from loader import dp
from .states import AdvertisementState
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, user
from keyboards.choise_buttons import choice, link_to_mainpage
from mainapp.models import Advertisement, User
import time


id_of_adv = []

def assign_sales_price(sales_price):
    adv = Advertisement.objects.filter(id=int(id_of_adv[-1])).first()
    if adv:
        adv.sales_price = sales_price
        adv.save()


@sync_to_async
def get_user(username):
    user=User.objects.get_or_create(username=username)
    return user[0]


@dp.message_handler(Command('create'), state=None)
async def create_advertisement(message: types.Message):
    username = message.from_user.username
    await message.answer(f'Здравствуйте, {username}')
    await message.answer("Введите название объявления")
    await AdvertisementState.name.set()


@dp.message_handler(state=AdvertisementState.name)
async def save_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await AdvertisementState.next()
    await message.answer('Введите описание объявления')


@dp.message_handler(state=AdvertisementState.description)
async def save_description(message: types.Message, state: FSMContext):
    description = message.text
    await state.update_data(description=description)
    await AdvertisementState.next()   
    await message.answer('Введите цену товара')


@dp.message_handler(state=AdvertisementState.price)
async def save_price(message: types.Message, state: FSMContext):
    price = message.text
    try:
        price = int(price)
    except Exception:
        await message.answer('Некорректные данные. Введите цену заново')
        return
    await state.update_data(price=price)
    data = await state.get_data()
    await state.finish()
    adv = Advertisement(**data, id=round(time.time()), user = await get_user(message.from_user.username))
    id_of_adv.append(adv.id)
    await sync_to_async(adv.save)()
    await message.answer(text="Есть ли горячая цена на товар?", reply_markup=choice)


@dp.callback_query_handler(text_contains='assign')
async def assign_price(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Укажите горячую цену')
    await AdvertisementState.sales_price.set()


@dp.message_handler(state=AdvertisementState.sales_price)    
async def save_sales_price(message: types.Message, state: FSMContext):
    sales_price = message.text
    try:
        sales_price = int(sales_price)
    except Exception:
        await message.answer('Некорректные данные. Введите цену заново')
        return
    await state.update_data(sales_price=sales_price)
    await sync_to_async(assign_sales_price)(sales_price)
    await state.finish()
    await message.answer(text="Спасибо, Ваше объявление будет закреплено")


@dp.callback_query_handler(text_contains='reject')
async def assign_price(call: CallbackQuery):
    await call.answer(cache_time=60)
    await call.message.answer('Ваше объявление будет закреплено, пока кто нибудь другой не укажет горячую цену', reply_markup=link_to_mainpage)