from aiogram import Router,F
from aiogram.filters import Command
from . import left_chat_members
from . import new_members
from . import ban
from . import unban
from . import mute
from . import unmute




router = Router()


router.message.register(new_members.new_members_answer, F.new_chat_members)
router.message.register(left_chat_members.left_chat_members, F.left_chat_member)
router.message.register(ban.ban_commnad_answer, F.text == '/ban')
router.message.register(unban.unban_commnad_answer, F.text == '/unban')
router.message.register(mute.mute_commnad_answer, F.text == '/mute')
router.message.register(unmute.unmute_commnad_answer, F.text == '/unmute')

