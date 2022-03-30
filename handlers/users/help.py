from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    ans = f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>,</b> " \
          f"<b>bot ishlashiga biroz tushunmagan ko'rinasiz, sizga yordam berman.</b>" \
          + "\n\n"
    ans += "<b>Botdan foydalanish uchun ko'rsatilgandek xabar yozishingiz kerak bo'ladi:</b>" + "\n"
    ans += "{sura tartib raqami}:{oyat tartib raqami}" + "\n\n"
    ans += "Misol uchun bizga oyatlar kursi kerak bo'lsa (Бақара сураси, 255-оят), " \
           "botga quyidagicha murojaat qilishimiz kerak: "
    ans += "2:255"

    await message.answer(ans)
