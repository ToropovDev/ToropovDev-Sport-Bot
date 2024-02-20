from aiogram import Bot, Dispatcher
import logging
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(level=logging.DEBUG)

TOKEN = ""
bot = Bot(token=TOKEN, parse_mode="HTML")

dp = Dispatcher()
dp['started_at'] = datetime.now().strftime("%Y-%m-%d %H:%M")

sched = AsyncIOScheduler()



