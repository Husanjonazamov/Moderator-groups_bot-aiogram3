from aiogram.types import Message


async def new_members_answer(message: Message):
    new_members = message.new_chat_members[0]
    await message.delete()
    await message.answer(f"✋Assalomu alaykum {new_members.full_name}!")