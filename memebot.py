import discord
import praw
import random
import os

reddit = praw.Reddit(
    client_id='9qjJGPvCXZ-TEt-IU6chHQ', # personal use script
    client_secret='pUPP-NXVNIKElfroTy0zOrqYDDWefQ', # secret key
    user_agent='python:meme_bot:v1.0 (by /u/Some_Finding_7514)' # CHANGE THE NAME TO YOURS
)

subreddits = ['memes', 'Memes_Of_The_Dank'] # you can here change what subreddits the bot will use

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!meme'):
        subreddit_name = random.choice(subreddits)
        subreddit = reddit.subreddit(subreddit_name)
        
        posts = list(subreddit.hot(limit=50))
        post = random.choice(posts)
        title = post.title
        url = post.url

        if url.endswith(('.jpg', '.jpeg', '.png')):
            embed = discord.Embed(title=title, url=url)
            embed.set_image(url=url)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(f'{title}\n{url}')

client.run('TOKEN') # replace TOKEN with your bot token