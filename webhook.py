from discord_webhook import DiscordWebhook
import os

WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')


webhook = DiscordWebhook(url=WEBHOOK_URL, content='test webhook execute')
response = webhook.execute()