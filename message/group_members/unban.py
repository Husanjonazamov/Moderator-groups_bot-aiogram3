from aiogram.types import Message
from aiogram import Bot




async def unban_commnad_answer(message: Message, bot: Bot):
    user = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in ('administrator', "creator"):
        if message.reply_to_message:
            ban_user = message.reply_to_message.from_user
            await message.chat.unban(ban_user.id)
            await message.answer(f"🛑<i>{ban_user.full_name}</i> <b>blokdan olindi</b>", parse_mode='HTML')

        else:
            await message.answer("<b>📎Kimnidir blokdan olish uchun uning xabarini reply qiling</b>", parse_mode='HTML')
    else:
        await message.answer("<b>🧑‍💻Siz kimnidir yozish imkonyatini berish uchun guruhda admin bo'lishingiz kerak</b>", parse_mode='HTML')