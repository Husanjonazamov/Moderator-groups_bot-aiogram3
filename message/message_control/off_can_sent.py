from aiogram.types import Message, ChatPermissions
from aiogram import Bot


async def off_command_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ('administrator', "creator"):
        permissions = ChatPermissions(can_send_messages=True)
        await message.chat.set_permissions(permissions)
        await message.answer(f"🛑<b>Guruhda Xabar yuborish cheklandi!</b>", parse_mode='HTML')
    else:
        await message.answer("<b>🧑‍💻Siz guruhda xabar yuborishni cheklash uchun admin bo'lishingiz kerak</b>", parse_mode='HTML')
