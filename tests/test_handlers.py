"""
Unit tests for bot handlers.
Run with: pytest tests/ -v
"""
from unittest.mock import AsyncMock, MagicMock

import pytest

from app.handlers import handle_help, handle_start_or_id


def _make_message(chat_id: int, user_id: int, text: str = "/id") -> MagicMock:
    """Helper: build a minimal fake aiogram Message."""
    message = MagicMock()
    message.chat.id = chat_id
    message.from_user.id = user_id
    message.text = text
    message.answer = AsyncMock()
    return message


@pytest.mark.asyncio
async def test_handle_id_replies_with_chat_id() -> None:
    message = _make_message(chat_id=-100123456, user_id=42)
    await handle_start_or_id(message)

    message.answer.assert_awaited_once()
    reply_text: str = message.answer.call_args[0][0]
    assert "-100123456_ERROR_TEST" in reply_text


@pytest.mark.asyncio
async def test_handle_help_contains_commands() -> None:
    message = _make_message(chat_id=999, user_id=1, text="/help")
    await handle_help(message)

    message.answer.assert_awaited_once()
    reply_text: str = message.answer.call_args[0][0]
    assert "/start" in reply_text
    assert "/id" in reply_text
    assert "/help" in reply_text
