
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
    try:
        bot_info = await bot.get_me()
        logger.info(f"Connected as {bot_info.first_name} (@{bot_info.username})")
    except TelegramError as e:
        logger.critical(f"Failed to connect: {e}")
        return

    logger.info(f"Starting to send messages to user {USER_ID} every {INTERVAL} seconds")
    message_count = 0

    while True:
        try:
            await bot.send_message(chat_id=USER_ID, text=f"{MESSAGE} ({message_count})")
            message_count += 1
            logger.info(f"Message {message_count} sent to {USER_ID}")
        except TelegramError as e:
            err = str(e).lower()
            if "unauthorized" in err:
                logger.critical("Bot token is invalid")
                break
            if "chat not found" in err:
                logger.critical(f"Chat with ID {USER_ID} not found – the user needs to start a conversation with the bot first")
                break
            if "blocked" in err:
                logger.critical(f"Bot was blocked by the user {USER_ID}")
                break
            logger.error(f"TelegramError: {e}. Retrying in {INTERVAL} seconds...")

        await asyncio.sleep(INTERVAL)

if __name__ == "__main__":
    try:
        asyncio.run(send_periodic_messages())
    except KeyboardInterrupt:
        logger.info("Stopping message sending…")
