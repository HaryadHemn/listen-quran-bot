from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    matn = f"<b>Assalom alaykum {message.from_user.full_name}\n</b>"
    matn += "Botdan foydalanish uchun quyidagicha murojaat qiling.\n"
    matn += "{sura tartib raqami}:{oyat tartib raqami}\n\n"
    matn += "Misol uchun sizga Baqara surasi, 255-oyat kerak bo'lsa.\n"
    matn += "Siz botga quyidagicha xabar jo'natishingiz kerak: <code>2:255</code>"
    await message.answer(matn)
