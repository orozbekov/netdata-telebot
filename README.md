# KeyDev Netdata Bot

Telegram-бот для получения уведомлений от [Netdata](https://netdata.cloud).  
Позволяет узнать ID чата/группы для настройки алертов и служит точкой приёма нотификаций.

---

## Структура проекта

```
netdata-telebot/
├── app/
│   ├── __init__.py
│   ├── config.py       # Настройки через pydantic-settings
│   ├── handlers.py     # Обработчики команд бота
│   └── logger.py       # Настройка логгера
├── tests/
│   ├── __init__.py
│   └── test_handlers.py
├── bot.py              # Точка входа
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Быстрый старт

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-org/netdata-telebot.git
cd netdata-telebot
```

### 2. Создай `.env` из примера

```bash
cp .env.example .env
```

Заполни `.env`:

```dotenv
TELEGRAM_BOT_TOKEN=123456789:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
LOG_LEVEL=INFO
```

### 3. Запусти через Docker Compose

```bash
docker compose up -d --build
```

Проверить логи:

```bash
docker logs -f netdata-telebot
```

---

## Локальная разработка

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python bot.py
```

---

## Тесты

```bash
pip install pytest pytest-asyncio
pytest tests/ -v
```

---

## Настройка Netdata → Telegram

1. Добавь бота в нужную группу/канал
2. Напиши боту `/id` — он вернёт Chat ID
3. Пропиши в `/etc/netdata/health_alarm_notify.conf` на сервере Netdata:

```bash
SEND_TELEGRAM="YES"
TELEGRAM_BOT_TOKEN="ВАШ_ТОКЕН"
DEFAULT_RECIPIENT_TELEGRAM="ВАШ_CHAT_ID"
role_recipients_telegram[sysadmin]="ВАШ_CHAT_ID"
role_recipients_telegram[dba]="ВАШ_CHAT_ID"
```

4. Проверь:

```bash
docker exec netdata-parent /usr/libexec/netdata/plugins.d/alarm-notify.sh test telegram
```

---

## Переменные окружения

| Переменная           | Обязательная | По умолчанию | Описание                        |
|----------------------|--------------|--------------|---------------------------------|
| `TELEGRAM_BOT_TOKEN` | ✅           | —            | Токен бота от @BotFather        |
| `LOG_LEVEL`          | ❌           | `INFO`       | Уровень логирования             |

---

## Деплой на продакшн

Рекомендуется запускать рядом с контейнером Netdata на том же сервере:

```bash
# На сервере
git clone https://github.com/your-org/netdata-telebot.git /opt/netdata-telebot
cd /opt/netdata-telebot
cp .env.example .env && nano .env
docker compose up -d --build
```

---

## Лицензия

MIT
