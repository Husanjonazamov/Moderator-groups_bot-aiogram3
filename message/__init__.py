from aiogram import Router
from aiogram.filters import  CommandStart
from . import start
from  . import group_members
from . import message_control

router = Router()

router.message.register(start.start_command_answer, CommandStart())
router.include_router(group_members.router)
router.include_router(message_control.router)