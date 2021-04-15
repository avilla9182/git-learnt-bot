import discord
import os
from dotenv import load_dotenv

def main():
    client = discord.Client()
    load_dotenv()

    print("Using Discord Library version " + discord.__version__)

    key = 'TOKEN'
    token = os.getenv(key)
    if(token == None):
        print("Invalid Token. Please check that token in .env is correct/exists")
        exit(1)


    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))


    @client.event
    async def on_message(message):
        channel = message.channel
        author = message.author
        msg = message.content

        if author == client.user:
            return

        if msg.startswith("$hello"):
            await channel.send(content="Hello!")


    client.run(token)


if __NAME__==__MAIN__:
    main()
