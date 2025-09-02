from telethon.sync import TelegramClient

api_id = 11196646  # ← Replace with your actual API ID
api_hash = '973630c74e36490a307704505e5fc18e'  # ← Replace with your actual API hash

session_name = 'samarth_session'

with TelegramClient(session_name, api_id, api_hash) as client:
    me = client.get_me()
    print("✅ Logged in as:", me.first_name, me.username)
