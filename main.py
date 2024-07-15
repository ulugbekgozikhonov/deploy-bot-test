# pip install aiogram==2.25.1

from aiogram import Bot,Dispatcher,types,executor
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from state import *
from default_btn import *

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7288939415:AAFqXavEYXOKmy9LsNGwNiE_wjlpURmLSB4"
PROXY_URL = "http://proxy.server:3128"
bot = Bot(token=BOT_TOKEN,parse_mode="HTML",proxy=PROXY_URL)
storage = MemoryStorage()
dp = Dispatcher(bot=bot,storage=storage)

@dp.message_handler(commands="start")
async def start_handler(message:types.Message):
    await message.answer("<b>Welcome To Quiz Bot</b> ❔")
    await message.answer("Enter full name:")
    await RegisterState.full_name.set()
    
@dp.message_handler(state=RegisterState.full_name)
async def get_full_name_handler(message:types.Message,state:FSMContext):
    full_name = message.text
    await state.update_data(full_name=full_name)
    await message.answer("Share Contact",reply_markup=phone_number)
    await RegisterState.phone_number.set()

@dp.message_handler(state=RegisterState.phone_number,content_types="contact")
async def get_phone_number_handler(message:types.Message,state:FSMContext):
    phone_number = message.contact.phone_number
    await state.update_data(phone_number=phone_number)
    await message.answer("Successfully registreted")
    await message.answer("Choise Course",reply_markup=courses)
    data = await state.get_data()
    
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp,skip_updates=True)