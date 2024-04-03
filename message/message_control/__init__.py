from aiogram import Router, F
from . import reklama
import filters
from . import on_can_sent
from . import off_can_sent


router = Router()

router.message.register(reklama.reklama_answer, filters.reklama.IsReklama())
router.message.register(on_can_sent.on_command_answer, F.text == '/on')
router.message.register(off_can_sent.off_command_answer, F.text == '/off')
