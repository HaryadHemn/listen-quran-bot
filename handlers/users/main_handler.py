from aiogram import types, exceptions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from quran import Quran, Text
import requests

from loader import dp

obj = Quran()
txt = Text()


@dp.message_handler(state=None)
async def send_date(message: types.Message):
    if len(message.text.split(':')) == 2:
        try:
            surah, ayah = message.text.split(':')
            surah = int(surah)
            ayah = int(ayah)
            await message.answer_audio(obj.get_surah_audio(surah, ayah, link=True), caption=f"<b>Tarjimasi:</b>\n\n<i>{txt.translaton(surah, ayah, 'uzbek_mansour')}\n\nАлауддин Мансур</i>")
            await message.answer_photo(obj.get_quran_ayah_image(surah, ayah, link=True), caption=f"<b><code>{surah}:{ayah}</code></b>")
        except:
            await message.answer('<b>Xato murojaat qildingiz.</b>\n\n<i>Malumot uchun shuni aytishim mumkinki, suralar soni 114 ta. Oyatlar soni esa siz tanlagan suraga bog\'liq.</i>')
    else:
        try:
            try:

                if send_audio(int(message.text)):
                    name = get_sura_name(f'{int(message.text)}:1')
                    await message.answer_audio(
                        send_audio(int(message.text)),
                        caption=f"<b>«{name}» сураси</b> | <b>Mishary Alafasy</b>"
                    )
                else:
                    ans = (
                        "<b>Quronda 114 sura mavjud.</b>",
                        "Iltimos, 1 dan 114 gacha bo'lgan son kirting."
                    )
                    await message.reply('\n\n'.join(ans))
            except exceptions.WrongFileIdentifier:
                ans = (
                    "<b>Ботда хатолик юз берди, бу хатолик устида ҳозирда ишлаяпмиз</b>"
                    "<a href='https://telegra.ph/file/895a32ea912dd1409e82f.png'> </a>",
                    "Telegram-да bot орқали 50 МБ ҳажмдан кўп бўлган аудио жўнатса "
                    "<a href='https://core.telegram.org/bots/api#sendaudio'>бўлмас экан</a>. "
                    "Баъзи сураларнинг ҳажми 50 МБ-дан ошиб кетяпти, шу сабабдан хатолик юз беряпти. "
                    "Яқин орада бу хатоликка барҳам берамиз (биизниллаҳ).",
                    "<b>Ноқулайликлар учун узр сўраймиз..)</b>"
                )
                await message.answer('\n\n'.join(ans), reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                'Veb sahifa', url='https://listen-quran.cf'),
                            InlineKeyboardButton(
                                'Telegram', url='https://t.me/ListenQuran_uz')
                        ]
                    ],
                ))
        except ValueError:
            text = ("<b>Botni ishlatishda xatolik!</b>",
                    "<i>Botni islatishga tushunmagan bo'lsangiz /help ni bosing</i>")
            await message.reply("\n\n".join(text))


def send_audio(num):
    if num < 10:
        return f'http://server8.mp3quran.net/afs/00{num}.mp3'
    elif num < 100:
        return f'http://server8.mp3quran.net/afs/0{num}.mp3'
    elif num <= 114:
        return f'http://server8.mp3quran.net/afs/{num}.mp3'
    else:
        return False


def get_sura_name(inp):
    url = f"https://api.alquran.cloud/v1/ayah/{inp}/editions/quran-uthmani,uz.sodik"
    r = requests.get(url)
    res = r.json()
    return res['data'][1]['surah']['englishName']
