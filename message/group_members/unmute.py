from aiogram.types import Message, ChatPermissions
from aiogram import Bot



async def unmute_commnad_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ('administrator', "creator"):
        if message.reply_to_message:
            user = message.reply_to_message.from_user
            permissions = ChatPermissions(can_send_messages=True)
            await message.chat.restrict(user.id, permissions)
            await message.answer(f"🛑<i>{user.full_name}</i><b>Endi xabar yubora oladi</b>", parse_mode='HTML')

        else:
            await message.answer("<b>📎Kimnidir blokdan olish uchun uning xabarini reply qiling</b>", parse_mode='HTML')
    else:
        await message.answer("<b>🧑‍💻Siz kimnidir blokdan olish uchun guruhda admin bo'lishingiz kerak</b>", parse_mode='HTML')