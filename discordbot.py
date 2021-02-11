#!/usr/bin/env python3

import discord

client = discord.Client()


@client.event
async def on_ready():
    print("{}: I'm ready".format(client.user))

@client.event
async def on_message(message):
    print(message.content)
    if (message.content == '=ping'):
        await message.channel.send('Pong {0}ms'.format(round(client.latency * 1000), 1))
    if (message.content.split()[0] == '=del'):
        await message.channel.purge(limit=int(message.content.split()[1]))
    if (message.content.split()[0] == '=say'):
        await message.channel.send(message.content.split("\"")[1])

client.run("MY_TOKEN")