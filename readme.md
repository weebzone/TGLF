---

# Tglf Bot

This is a Python bot built using Pyrogram that automatically forwards messages with links from a source channel to multiple destination channels. The bot can be configured using a JSON file and can be run using either a user session or a bot token.

## Prerequisites

- Python 3.6 or higher
- A Telegram account
- API ID and API hash for creating a Pyrogram client
- Bot token or user session string for bot authentication
- A `config.env` file for storing environment variables (API_ID, API_HASH, BOT_TOKEN, USER_SESSION)
- A `chat_id.json` file for specifying channel mappings and modifications

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/weebzone/tglf.git
   cd tglf
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `config.env` file in the project directory with the following content:
   ```env
   API_ID=your_api_id
   API_HASH=your_api_hash
   BOT_TOKEN=your_bot_token
   USER_SESSION=your_user_session_string (if available)
   ```

## Configuration

1. Create a JSON file named `chat_list.json` in the same directory as the script.
2. Define the channel mappings within the JSON file. Each mapping consists of the following properties:

   - `"source"`: The ID of the source channel from which you want to forward messages.

   - `"destinations"`: An array of channel IDs where the messages with links will be forwarded to.

   - `"prefix"` (Optional): A string that will be added before the link in the forwarded message. This can be useful for providing additional context to the forwarded content.

   - `"suffix"` (Optional): A string that will be added after the link in the forwarded message. Similar to the prefix, this can be used to add context.

3. Define the channel mappings in the JSON file:
   ```json
   [
       {
           "source": "source_channel_id",
           "destinations": ["destination_channel_id1", "destination_channel_id2"],
           "prefix": "Optional prefix",
           "suffix": "Optional suffix"
       }
   ]
   ```
4. Here's an example of a `chat_list.json` file with multiple mappings:

    ```json
    [
        {
            "source": "source_channel_id1",
            "destinations": ["destination_channel_id1", "destination_channel_id2"],
            "prefix": "Check out this link:"
        },
        {
            "source": "source_channel_id2",
            "destinations": ["destination_channel_id3"],
            "suffix": "🔗"
        },
        {
            "source": "source_channel_id3",
            "destinations": ["destination_channel_id4"]
        }
        // Add more mappings as needed
    ]
    ```

In this example:

- The first mapping forwards messages from `source_channel_id1` to `destination_channel_id1` and `destination_channel_id2`. It adds a prefix before the link.

- The second mapping forwards messages from `source_channel_id2` to `destination_channel_id3` and adds a suffix after the link.

- The third mapping forwards messages from `source_channel_id3` to `destination_channel_id4` without any prefix or suffix.

Remember to replace `source_channel_id` and `destination_channel_id` with the actual channel IDs you want to use.

If you don't want to use prefixes or suffixes, simply omit the `"prefix"` and `"suffix"` properties from the mapping.
## Running the Bot

1. Open a terminal and navigate to the bot's directory.
2. Run the bot script:
   ```
   python bot.py
   ```
3. The bot will start forwarding messages with links from the source channel to the specified destination channels. It will add optional prefixes and suffixes to the forwarded messages.

## Notes

- Make sure the bot has necessary permissions to read messages from source and send messages to destination channels.
- The bot forwards messages with links from the source channel to all specified destination channels.
- The forwarding process is subject to a delay of 5 seconds between messages to avoid spamming.

---
