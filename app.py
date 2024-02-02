from flask import Flask
from bot_start import *
import asyncio

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    asyncio.run(bot_start())
    app.run()
