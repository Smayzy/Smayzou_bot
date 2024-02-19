print("Bot starting ...")
import discord
from discord.ext import commands
import random

TOKEN = "Your_TOKEN"

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents)

@client.event
async def on_ready():
    print("[INFO] Bot is ready !")


@client.command()
async def help_command(ctx):
                """Display a list of avalible commands of Smayzou"""
                command_list = [
                        "/help - Display this help message",
                        "/kick - Kick a member",
                        "/ban - ban a member",
                        "/unban - Unban a member",
                        "/nickname - Change your name",
                        "/ping - View the ping",
                        "/question - You say question and I say yes or no",
                        "/slowmode - Set slowmode in this channel",
                        "/vote - Create a vote"
                ]
                await ctx.respond("Here's a list of available commands:\n```{}```".format('\n'.join(command_list)))


@client.command()
async def kick(ctx, user:discord.User, reason):
        """Kick a member"""
        if ctx.author.guild_permissions.kick_members:
                await ctx.guild.kick(user)
                await ctx.respond(f"I have kick {user} for the raison : {reason} !")

        else:
                await ctx.respond("You can't kick a member !")


@client.command()
async def ban(ctx, user:discord.User, reason):
        """Ban a member"""
        if ctx.author.guild_permissions.ban_members:
                await ctx.guild.ban(user)
                await ctx.respond(f"I have ban {user} for the raison : {reason} !")

        else:
                await ctx.respond("You can't ban a member !")


@client.command()
async def unban(ctx, user:discord.User, reason):
        """Unban a member"""
        if ctx.author.guild_permissions.ban_members:
                await ctx.guild.unban(user)
                await ctx.respond(f"I have unban {user} for the raison : {reason} !")

        else:
                await ctx.respond("You can't kick a member !")


@client.command()
async def ping(ctx):
        """View the ping"""
        await ctx.respond(f'Your ping is {round(client.latency * 1000)}ms')


@client.command()
async def question(ctx, question):
        responses = ['Yes',
                     'No',
                     'Without a doubt',
                     'Count on it',
                     'My sources say no',
                     'My sources say yes',]
        await ctx.respond(f'Question: {question} Answer: {random.choice(responses)}')


@client.command()
async def slowmode(ctx, seconds: int):
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.respond(f"Set the slowmode delay in this channel to {seconds} seconds!")


@client.command()
async def nickname(ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.respond(f'Nickname was changed for {member.mention} ')


@client.command()
async def vote(ctx, message):
        emb=discord.Embed(title=" VOTE ", description=f"{message}")
        msg=await ctx.channel.send(embed=emb)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')

client.run(TOKEN)