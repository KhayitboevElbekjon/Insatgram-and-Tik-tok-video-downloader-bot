import json
from aiogram.dispatcher.filters import Text
from instagram import instagramDown
# from facebook import facebook
from tik_tok import tik_tok
import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="5855817176:AAHcYvLuNmZQn--Tc-rJJTffLPYDwCUvPKI")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(
        "Assalomu alaykum! TikTok, Facebook va Instagramdan videolarni yuklash uchun men tayyorman. Videoni yuklash uchun linkni menga yuboring!")

if Text(startswith='https://www.instagram.com'):
    @dp.message_handler(Text(startswith='https://www.instagram.com'))
    async def send_media(message:types.Message):
        link=message.text
        data=instagramDown(urll=link)
        if data=='Bad':
            await message.reply('Bu link orqali hech narsa topa olmadik')
        else:
            if data['type'] == 'video':
                await message.reply_video(video=data['media'])

# https://www.facebook.com/100070608220470/videos/147301844941454/
# elif Text(startswith='https://www.facebook.com/'):
#     @dp.message_handler(Text(startswith='https://www.facebook.com/'))
#     async def send_media(message:types.Message):
#         await message.reply('Video qidirilmoqda')
#         natija=message.text
#         data=facebook(urll=natija)
#         if data=='Bad':
#             await message.reply('Bu link orqali hech narsa topa olmadik')
#         else:
#             await message.reply_video(data['video'])

elif Text(startswith='https://vm.tiktok.com/'):
    @dp.message_handler(Text(startswith='https://vm.tiktok.com/'))
    async def send_media(message:types.Message):
        natija=tik_tok(urll=message.text)
        if natija=='Bad':
            await message.reply('Bu link orqali hech narsa topa olmadik')
        else:
            await message.reply_video(natija['Video'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)








