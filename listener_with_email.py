from telethon import TelegramClient, events
import yagmail


from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env file

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
gmail_user = os.getenv("GMAIL_USER")
gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
session_name = 'samarth_session'

# Telegram credentials loaded from .env file
# Gmail credentials loaded from .env file


# # Telegram credentials
# api_id = 11196646
# api_hash = '973630c74e36490a307704505e5fc18e'
# session_name = 'samarth_session'

# # Gmail credentials
# gmail_user = 'samarthdudi04@gmail.com'                # <-- your Gmail
# gmail_app_password = 'aiax gbjp ufyp ygzy'   # <-- your App Password (NOT your Gmail password)

# Who should receive the email?
receiver_email = 'samarthdudi04@gmail.com'  # could be same as sender

# Keywords
target_keywords = [
    'cse-ai', 'ai & ml', 'aiml', 'ai-ml', 'cse-aiml', 'all branches',
    'open to all', 'artificial intelligence', 'artificial intelligence and machine learning',
    'ai', 'ai&ml', 'allied'
]

# Setup yagmail client
yag = yagmail.SMTP(gmail_user, gmail_app_password)

# Start Telegram client
client = TelegramClient(session_name, api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    chat = await event.get_chat()

    if hasattr(chat, 'title') and 'engineering 2026 batch' in chat.title.lower():
        message_text = event.message.message.lower()
        normalized_text = message_text.replace('&', 'and')

        if any(keyword in normalized_text for keyword in target_keywords):
            print("\n📩 Matched Message from Engineering 2026 batch:\n")
            print(event.message.message)
            print("-" * 50)

            # ✅ Send the email
            subject = "📢 New Placement Drive Alert - Engineering 2026"
            body = f"Group: {chat.title}\n\nMatched Message:\n{event.message.message}"
            yag.send(to=receiver_email, subject=subject, contents=body)
            print("📧 Email sent to:", receiver_email)

client.start()
print("🤖 Listening to messages and forwarding to Gmail...")
client.run_until_disconnected()
