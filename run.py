import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ChatType

BOT_TOKEN = '8326615855:AAHJBV1Sq_sJXui-KMbH3sNB7hwjc9kqsOE'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_command(message: Message):
    await message.reply("Bot ishga tushdi, bu bot guruhlarga tashqaridan uzatilgan xabarlarni o'chiradi!")

@dp.message()
async def handle_message(message: Message):
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        if message.forward_origin is not None:
            try:
                await message.delete()
                await message.reply("Xabarni tashqaridan guruhga uzatish taqiqlanadi!")
            except Exception as e:
                print(f"Xabarni o'chirishda xatolik yuz berdi: {e}")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())