import asyncio
import aiogram
from aiogram.filters import command
from aiogram import types

BOT_TOKEN = "8049350161:AAGUAK1QkJ-JeJJpgabQENi2w82hd-ApyO0"

bot = aiogram.Bot(token=BOT_TOKEN)
dispatcher = aiogram.Dispatcher()

async def main():
    await dispatcher.start_polling(bot)

def is_start_command_filter(message: types.Message) -> bool:
    return message.text == '/start'

def is_stop_command_filter(message: types.Message) -> bool:
    return message.text == '/stop'

def first_message_check(message: types.Message) -> bool:
    if message.text == "Hello":
        return True
    else:
        return False

@dispatcher.message(command.Command("start", prefix='/'))
async def welcome(message: types.Message) -> None:
    await message.reply("Hi. Hope you are having nice day!")


if __name__ == '__main__':
    asyncio.run(main())