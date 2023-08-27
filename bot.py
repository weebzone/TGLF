from pyrogram import Client, filters
import asyncio
import logging
import os
from dotenv import load_dotenv
import json
import re

load_dotenv('config.env', override=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
USER_SESSION = os.getenv("USER_SESSION")

# Load channel mappings from the JSON file
with open("chat_list.json", "r") as json_file:
    CHANNEL_MAPPING = json.load(json_file)

# Initialize the Client with user session or bot token
if USER_SESSION:
    app = Client(
        "my_user_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=USER_SESSION,
    )
    logger.info("Bot started using Session String")
else:
    app = Client(
        "my_bot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN
    )
    logger.info("Bot started using Bot Token")

def extract_links(message_text):
    # Use regular expressions to find links and magnet links in the message
    link_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    magnet_pattern = r'magnet:\?xt=urn:btih:[a-fA-F0-9]+&.*'
    
    links = []
    
    # Find all links and magnet links in the message
    matches_link = re.findall(link_pattern, message_text)
    matches_magnet = re.findall(magnet_pattern, message_text)
    
    links.extend(matches_link)
    links.extend(matches_magnet)
    
    return links

@app.on_message(filters.channel)
async def forward(client, message):
    # Forwarding the messages to the channels
    try:
        for mapping in CHANNEL_MAPPING:
            source_channel = mapping["source"]
            destinations = mapping["destinations"]
            prefix = mapping.get("prefix", "")
            suffix = mapping.get("suffix", "")

            if message.chat.id == int(source_channel):
                source_message = await client.get_messages(int(source_channel), message.id)
                extracted_links = extract_links(source_message.text)

                if extracted_links:
                    for link in extracted_links:
                        modified_message_text = f"{prefix} {link} {suffix}".strip()

                        for destination in destinations:
                            await client.send_message(chat_id=int(destination), text=modified_message_text)
                            await asyncio.sleep(5)

                        logger.info("Forwarded a modified message from %s to %s",
                                    source_channel, destinations)
                        
                        # Add a delay before sending the next link
                        await asyncio.sleep(1)
    except Exception as e:
        logger.exception(e)

if __name__ == "__main__":
    app.run()
