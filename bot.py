import tracemalloc
import discord
import os
from discord.ext import commands
import discord.ext
import time
import random
import asyncio
 
tracemalloc.start()
description = "A bot made for a disc user by Lazer69"
bot = commands.Bot(command_prefix=".", description=description)
bot.remove_command("help")
 
async def statusBgTask():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="to see who the best bot is oh wait, I am! | .help"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="the game where I watch you; Everywhere ::) | .help"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="when will discord add bot statuses | .help"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to the birds chirping | .help"))
        await asyncio.sleep(5)
 
@bot.event
async def on_ready():
    print(f"Logged in as:")
    print(f"{bot.user.name}")
    print(f"{bot.user.id}")
    print(f"In servers: {bot.guilds}")
    print(f"Latency: {round(bot.latency * 1000)} ms")
    print(f"----------------------------------------------------------")
    bot.loop.create_task(statusBgTask())
 
@bot.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain."
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."]
    _8ballEmbed = discord.Embed(title="8 ball results", description=f"Question: {question}", color=0x0000ff)
    _8ballEmbed.add_field(name="Anwser", value=f"Anwser: {random.choice(responses)}")
    await ctx.send(embed=_8ballEmbed)
    print(f"{ctx.author} used the 8ball command in {ctx.message.channel}")
 
 
@bot.command()
async def calnum(ctx, num1:int, operation, num2:int):
    if operation == "+":
        addEmbed = discord.Embed(title="Calculator add", description=f"{num1} + {num2} = {num1 + num2}", color=0x0000ff)
        await ctx.send(embed=addEmbed)
        print(f"{ctx.author} has added {num1} and {num2} and got {num1 + num2}")
    
    if operation == "-":
        subEmbed = discord.Embed(title="Calculator subtract", description=f"{num1} - {num2} = {num1 - num2}", color=0x0000ff)
        await ctx.send(embed=subEmbed)
        print(f"{ctx.author} has subtracted {num1} and {num2} and got {num1 - num2}")
 
    if operation == "x":
        mulEmbed = discord.Embed(title="Calculator multiply", description=f"{num1} x {num2} = {num1 * num2}", color=0x0000ff)
        await ctx.send(embed=mulEmbed)
        print(f"{ctx.author} has multiplied {num1} and {num2} and got {num1 * num2}")
 
    if operation == "/":
        divEmbed = discord.Embed(title="Calculator divide", description=f"{num1} / {num2} = {num1 / num2}", color=0x0000ff)
        await ctx.send(embed=divEmbed)
        print(f"{ctx.author} has divided {num1} and {num2} and got {num1 / num2}")
 
@bot.command()
async def ping(ctx):
    pingEmbed = discord.Embed(title="Pong!", description=f"Latency: {round(bot.latency * 1000)} ms", color=0x0000ff)
    await ctx.send(embed=pingEmbed)
    print(f"{ctx.author} used the ping command in {ctx.message.channel}")
 
@bot.command()
async def help(ctx):
    helpEmbed = discord.Embed(title="Help", description="Here are the commands and info for the bot", color=0x0000ff)
    helpEmbed.add_field(name="Description:", value=f"{description}")
    helpEmbed.add_field(name=".calnum", value="Say, **.calnum** (num1) (operation) (num2) to use this command. Example .calnum 10 + 10. You can use 4 operations, addition, subtraction, division, and multiplacation")
    helpEmbed.add_field(name=".8ball", value="Say, **.8ball (question)** to use this command. Example .8ball Is this a good bot?")
    helpEmbed.add_field(name=".ping", value="Say **.ping** to use this command. This gives the latency of the bot.")
    helpEmbed.add_field(name=".help", value="Shows this message")
    helpEmbed.add_field(name=".credits", value="Shows the credits")
    await ctx.author.send(embed=helpEmbed)
    print(f"{ctx.author} used the help command in {ctx.message.channel}")
 
@bot.command()
async def credits(ctx):
    creditEmbed = discord.Embed(title="Credits", description="Thank you to Lazer 69 for making this bot.", color=0x0000ff)
    await ctx.send(embed=creditEmbed)
    print(f"{ctx.author} used the credit command in {ctx.message.channel}")
 
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        print(f"{ctx.message.author} has posted an invalid command in {ctx.channel}")
        CNFErrorEmbed = discord.Embed(title="Error", description=f"This command does not exist. To see the list of commands say **.help**.", color=0x0000ff)
        await ctx.message.delete()
        await ctx.send(embed=CNFErrorEmbed)
 
    if isinstance(error, commands.MissingRequiredArgument):
        print(f"{ctx.message.author} posted a command that had missing arguments in {ctx.channel}")
        MRAErrorEmbed = discord.Embed(title="Error", description="You forgot to include what you wanted the command to do. If you need help use the **.help** command.", color=0xFF0000)
        await ctx.message.delete()
        await ctx.send(embed=MRAErrorEmbed)
 
bot.run("token")
