from aiogram import Bot, Dispatcher
import logging
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(level=logging.DEBUG)

TOKEN = "6673453076:AAE-gIEpOi14q55DumXAqDfssKPHQ4ExwdU"
bot = Bot(token=TOKEN, parse_mode="HTML")

dp = Dispatcher()
dp['started_at'] = datetime.now().strftime("%Y-%m-%d %H:%M")

sched = AsyncIOScheduler()



