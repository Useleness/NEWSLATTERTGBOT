from config import botik, admin, welcoming, cmd, symb # IMPORT LOCAL VALUES
from aiogram import Bot, Dispatcher, executor, types 
from database import DATABASE # class import
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(botik)
dp = Dispatcher(bot)
db = DATABASE('datab.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, welcoming)

@dp.message_handler(commands=[cmd])
async def cmd(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin:
            text = message.text[symb:]
            users = db.get_user()
            for msg in users:
                try:
                    await bot.send_message(msg[0], text)                                        
                    if int(msg[1]) != 1:
                        db.set_active(msg[0], 1)
                except:
                    db.set_active(msg[0], 0)

            await bot.send_message(message.from_user.id, "```\nLOG:\n» Рассылка запущена!\n```", parse_mode="MarkdownV2")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)

