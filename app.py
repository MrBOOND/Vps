import asyncio
import logging
from telegram import Bot
from telegram.error import TelegramError

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8054991584:AAF-VmW1-YPLZG_mQ3HHL9kkbAcGEdU0iAc"
USER_ID = 7069636058
MESSAGE = "Automated message from the bot"
INTERVAL = 5

async def send_periodic_messages():
    bot = Bot(token=BOT_TOKEN)
    message_count = 0
    while True:
        try:
            await bot.send_message(chat_id=USER_ID, text=f"{MESSAGE} ({message_count})")
            message_count += 1
            logger.info(f"Message {message_count} sent to {USER_ID}")
        except TelegramError as e:
            logger.error(f"TelegramError: {e}")
        await asyncio.sleep(INTERVAL)

async def main_loop():
    while True:
        try:
            await send_periodic_messages()
        except Exception as e:
            logger.error(f"Unhandled Exception: {e}. Restarting loop...")

if __name__ == "__main__":
    try:
        asyncio.run(main_loop())
    except KeyboardInterrupt:
        logger.info("Manual stop received.")
