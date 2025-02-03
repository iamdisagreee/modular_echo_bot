import asyncio
import os

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

#Функция конфигурирования и запуска бота
async def main() -> None:

    #Загружаем конфиг в переменную конфиг
    config: Config = load_config()
    #print(os.getenv('BOT_TOKEN'))

    #Инициализируем бота и диспетчера
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    #Регистрируем роутеры в диспетчере
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)


    #Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
