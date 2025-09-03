from telethon import TelegramClient, events
from dotenv import load_dotenv
import os
import sendgrid
from sendgrid.helpers.mail import Mail

# Load environment variables from .env
load_dotenv()

# Telegram credentials
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = 'samarth_session'

# Email credentials
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
TO_EMAIL = os.getenv("TO_EMAIL")
FROM_EMAIL = os.getenv("FROM_EMAIL")  # Make sure this email is verified in SendGrid

# Keywords to monitor
target_keywords = [
    'cse-ai', 'ai & ml', 'aiml', 'ai-ml', 'cse-aiml', 'all branches',
    'open to all', 'artificial intelligence', 'artificial intelligence and machine learning',
    'ai', 'ai&ml', 'allied'
]

# Setup Telegram client
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

            # Prepare SendGrid email
            subject = "📢 New Placement Drive Alert - Engineering 2026"
            body = f"Group: {chat.title}\n\nMatched Message:\n{event.message.message}"

            message = Mail(
                from_email=FROM_EMAIL,
                to_emails=TO_EMAIL,
                subject=subject,
                plain_text_content=body
            )

            try:
                sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
                response = sg.send(message)
                print(f"📧 Email sent via SendGrid: {response.status_code}")
            except Exception as e:
                print("❌ Failed to send email via SendGrid:", str(e))

# Start the bot
client.start()
print("🤖 Listening to messages and forwarding to Gmail via SendGrid...")
client.run_until_disconnected()
