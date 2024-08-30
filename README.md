# Reddit Meme Bot

A Discord bot that fetches random memes from specified subreddits and posts them to your Discord server. This bot uses the [PRAW](https://praw.readthedocs.io/en/latest/) library to interact with Reddit and the [discord.py](https://discordpy.readthedocs.io/en/stable/) library to interact with Discord.

## Features

- Fetches memes from multiple subreddits.
- Posts meme images to your Discord channel.
- Simple command to trigger the meme fetch.

## Setup

### 1. Create a Reddit Application

To access Reddit's API, you'll need to create a Reddit application to obtain your `client_id`, `client_secret`, and configure your `user_agent`. Follow these steps to create an application:

1. Go to the [Reddit App Preferences](https://www.reddit.com/prefs/apps) page.
2. Scroll down to the "Developed Applications" section and click the "Create App" or "Create Another App" button.
3. Fill in the application details:
   - **name**: Choose a name for your app (e.g., "Meme Bot").
   - **App type**: Select "script".
   - **description**: You can leave this blank or add a brief description (optional).
   - **about url**: Leave this blank or add a URL if you have one.
   - **permissions**: This is not required for a script application.
   - **redirect uri**: Enter `http://localhost:8080` or any valid URL (the redirect URI is not used in script applications but is required for the creation process).
4. Click "Create app" to save your application.

After creating the app, you’ll see your **client_id** (under "webapp" or "script") and **client_secret** (click on "edit" to view it). Keep these credentials secure.

### 2. Configure Reddit and Discord Credentials

Open `bot.py` and replace the placeholders with your actual Reddit and Discord credentials.

```python
reddit = praw.Reddit(
    client_id='YOUR_REDDIT_CLIENT_ID',  # Replace with your Reddit app personal use script
    client_secret='YOUR_REDDIT_CLIENT_SECRET',  # Replace with your Reddit app client_secret aka secret key
    user_agent='python:meme_bot:v1.0 (by /u/YOUR_REDDIT_USERNAME)'  # Replace with your Reddit username
    client.run('YOUR_DISCORD_BOT_TOKEN')  # Replace TOKEN with your Discord bot token
)
