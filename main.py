import discord
import os

client = discord.Client()

print(discord.__version__)

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    channel = message.channel
    author = message.author
    msg = message.content
    print (channel.name)
    print (channel.type)

    if author == client.user:
        return

    if msg.startswith("$hello"):
        await channel.send(content="Hello!")

#client.run(os.getenv('TOKEN'))
client.run('ODMwMjc3OTMwMzUyMzc3ODc2.YHEWlA.qyPvjAw8lWGsVBkmWgVSHakg_yo')
#print("Hello World!\n")
