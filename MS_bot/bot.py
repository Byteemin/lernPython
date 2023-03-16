from aiogram.utils import executor
from create_bot import dp
from hendlers import other


async def on_startup(_):
	print('Бот запущен!')

other.register_hendlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)