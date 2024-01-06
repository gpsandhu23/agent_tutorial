# Simple AI Agent Using OpenAI and Langchain

This repository contains a simple AI agent built using OpenAI and Langchain, integrated with Slack. It's designed to interact through Slack Direct Messages (DMs), providing AI-powered responses.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Docker
- Docker Compose

### Setting Up Your Environment

1. **Clone the Repository**

    Start by cloning this repository to your local machine.

    ```bash
    git clone https://github.com/gpsandhu23/agent_tutorial.git
    cd agent_tutorial
    ```

2. **Create Slack App**

    - Create a new app in your Slack workspace.
    - Add the following scopes to your Slack app:
      ```
      oauth_config:
        scopes:
          bot:
            - chat:write
            - files:read
            - im:history
            - im:read
            - im:write
      settings:
        event_subscriptions:
          bot_events:
            - message.im
      ```
    - Obtain the following credentials:
      - `SLACK_APP_TOKEN`: Starts with `xapp-`.
      - `SLACK_BOT_TOKEN`: Starts with `xoxb-`.
      - `SLACK_SIGNING_SECRET`.

3. **Set Up Environment Variables**

    Add the following environment variables to a `.env` file in the root of the project:

    ```
    SLACK_APP_TOKEN="xapp-..."
    SLACK_BOT_TOKEN="xoxb-..."
    SLACK_SIGNING_SECRET="..."
    OPENAI_API_KEY="sk-..."
    ```

    Replace the placeholders with your actual Slack app credentials and OpenAI API key.

### Running the Application

1. **Build and Run with Docker Compose**

    In the project directory, run:

    ```bash
    docker-compose up
    ```

    This command builds the Docker image and starts the service.

2. **Interacting with the AI Agent**

    - Add the Slack app to your workspace.
    - Send a Direct Message to your app in Slack.
    - The AI agent will respond using its AI capabilities.