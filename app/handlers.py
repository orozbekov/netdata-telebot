from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.logger import get_logger

router = Router()
logger = get_logger(__name__)


@router.message(Command(commands=["start", "id"]))
async def handle_start_or_id(message: Message) -> None:
    """
    Handle /start and /id commands.
    Responds with the current chat ID — useful for configuring Netdata alerts.
    """
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "unknown"

    logger.info("User %s requested chat ID in chat %s", user_id, chat_id)

    await message.answer(
        f"<b>Ваш ID чата:</b> <code>{chat_id}</code>\n\n"
        f"Используйте этот ID для настройки уведомлений Netdata.",
        parse_mode="HTML",
    )


@router.message(Command("help"))
async def handle_help(message: Message) -> None:
    """Handle /help command — show available commands."""
    await message.answer(
        "<b>Доступные команды:</b>\n\n"
        "/start — приветствие и ID чата\n"
        "/id — узнать ID чата\n"
        "/help — список команд",
        parse_mode="HTML",
    )
