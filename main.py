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
  teams = test(arg)

  team1 = "\n".join(teams[0])
  team2 = "\n".join(teams[1])

  embed = discord.Embed(title = "League of Legends Teams")
  embed.add_field(name="Red Team:", value=team1, inline=False)
  embed.add_field(name="Blue Team:", value=team2, inline=False)

  await ctx.send(embed=embed)


client.run(os.getenv('DISCORD_TOKEN'))