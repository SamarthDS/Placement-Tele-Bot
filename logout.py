from telethon.sync import TelegramClient

api_id = 11196646
api_hash = '973630c74e36490a307704505e5fc18e'
session_name = 'samarth_session'

with TelegramClient(session_name, api_id, api_hash) as client:
    client.log_out()
    print("✅ Logged out successfully.")
