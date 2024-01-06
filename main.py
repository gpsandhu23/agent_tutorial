from agent import process_user_task
from dotenv import load_dotenv
import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Initialize the chat_history
chat_history = []

# Slack App Initialization
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

def process_message(event, client):
    """Process the message and respond accordingly."""
    try:
        user_id, channel_id = event.get('user'), event.get('channel')

        # Respond only to DMs and non-bot messages
        if 'channel_type' in event and event['channel_type'] == 'im' and 'bot_id' not in event:
            # Send an initial response to let the user know the AI is processing the request
            response = client.chat_postMessage(channel=channel_id, text="Processing your request, please wait...")
            # Get the timestamp of the response so that we can update it with the real response from the AI later
            ts = response['ts']
            # Get the text of the user message from Slack DM
            agent_input = event.get('text', '')
            # Process the user message using the agent
            agent_response_text = process_user_task(str(agent_input), chat_history)
            # Update the initial response with the real response from the AI
            client.chat_update(channel=channel_id, ts=ts, text=agent_response_text)
    except Exception as e:
        logging.error("Error processing message: %s", str(e))

@app.event("message")
def message_handler(event, say, ack, client):
    """Handles incoming messages."""
    ack()
    logging.info("Message received: %s", event)

    # Process the message
    process_message(event, client)

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN"))
    handler.start()