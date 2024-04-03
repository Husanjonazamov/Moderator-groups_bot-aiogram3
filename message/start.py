from aiogram.types import Message


async def start_command_answer(message: Message):
    await message.answer(f"🤚Assalomu alaykum {message.from_user.first_name}")

