from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from utils import TestStates

import json, string

@dp.message_handler(state='*', commands=['setstate'])
async def process_setstate_command(message: types.Message):
    argument = message.get_args()
    state = dp.current_state(user=message.from_user.id)
    if not argument:
        await state.reset_state()
        return await message.reply('Состояние сброшено!')

    if (not argument.isdigit()) or (not int(argument) < len(TestStates.all())):
        return await message.reply('Ключ  не подходит.\n')

    await state.set_state(TestStates.all()[int(argument)])
    await message.reply('Текущее состояние успешно изменено!', reply=False)


#######Команды вне машины состоянияй
# @dp.message_handler()
async def echo_send(message : types.Message):
		#парсер от матов
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
	.intersection(set(json.load(open('cenz.json')))) != set():
		await message.reply('Маты запрещены! Сообщение удалено!')
		await message.delete()

# @dp.message_handler(commands=['start', 'help']) # тут все просто это пример обычных базовых команд
async def commands_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Текст')
		await message.delete()
	except:
		await message.reply('Запусти бота! В ином случае информация не доступна!')

# @dp.message_handler(commands=['lol'])
async def commands_lol(message : types.Message):
	await bot.send_message(message.from_user.id, 'Сам ты лол')

# @dp.message_handler(commands=['Русский'])
async def commands_language(message : types.Message):
	await bot.send_message(message.from_user.id, 'Неа, чуваш')


########Команды состояний
# @dp.message_handler(state=TestStates.TEST_STATE_1)
async def first_test_state_case_met(message: types.Message):
    await message.reply('Первый!', reply=False)

# @dp.message_handler(commands=['test'], state=TestStates.TEST_STATE_1)
async def test_msg_St1(message: types.Message):
    await message.reply('Весело', reply=False)


# @dp.message_handler(state=TestStates.TEST_STATE_2)
async def second_test_state_case_met(message: types.Message):
    await message.reply('Второй!', reply=False)

# @dp.message_handler(commands=['test'], state=TestStates.TEST_STATE_2)
async def test_msg_St2(message: types.Message):
    await message.reply('Не Весело', reply=False)


def register_hendlers(dp : Dispatcher):
	###Вне State=none
	dp.register_message_handler(commands_start, commands=['start', 'help'] )
	dp.register_message_handler(commands_language, commands=['Русский'] )
	dp.register_message_handler(echo_send)
	#State 1
	dp.register_message_handler(test_msg_St1, commands=['test'], state=TestStates.TEST_STATE_1)
	dp.register_message_handler(first_test_state_case_met, state=TestStates.TEST_STATE_1)
	#State 2
	dp.register_message_handler(test_msg_St2, commands=['test'], state=TestStates.TEST_STATE_2)
	dp.register_message_handler(second_test_state_case_met, state=TestStates.TEST_STATE_2)
