from aiogram.types import Message, ChatPermissions
from aiogram import Bot


async def on_command_answer(message: Message, bot: Bot):
    permissions = ChatPermissions(can_send_messages=True)
    await message.chat.set_permissions(permissions)
    await message.answer(f"<b>🧑‍💻Xabar yuborish Yoqildi</b>", parse_mode='HTML')