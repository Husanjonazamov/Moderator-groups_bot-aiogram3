from aiogram import Bot, Dispatcher, F
import message
from asyncio import run



dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(5765144405, 'Bot ishga tushdi✅')

async def shutdown_answer(bot: Bot):
    await bot.send_message(5765144405, "Bot to'xtadi❌")


async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.include_router(message.router)

    bot = Bot('7178118588:AAHMuun6LvJ4lyjObeo7n_S_WmC_H45pWfI', parse_mode='HTML')
    await dp.start_polling(bot, polling_timeout=1)

run(start())
