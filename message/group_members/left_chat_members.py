from aiogram.types import Message



async def left_chat_members(message: Message):
    left_members = message.left_chat_member
    await message.delete()
    await message.answer(f"✋Xayr {left_members.full_name}!")