import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from func import *

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '$', intents=intents)

@client.event
async def on_ready():
  print("Bot is Ready")
  print("------------")

@client.command()
async def hello(ctx):
  await ctx.send("Hello")

@client.command(pass_context = True)
async def rteam(ctx, arg):
  await ctx.send(arg)
  teams = test(arg)
  await ctx.send(teams[0])
  await ctx.send(teams[1])

client.run(os.getenv('DISCORD_TOKEN'))