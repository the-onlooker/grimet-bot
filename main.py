import discord
from discord import app_commands
from discord.ext import commands
from typing import Optional
from config import TOKEN

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Grimet-Bot is up!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="kick", description="Kick a user from your server.")
async def kick(interaction: discord.Interaction, member: str, *, reason: Optional[str] = None):
    guild = interaction.guild
    member_obj = discord.utils.get(guild.members, mention=member)
    try:
        await member_obj.kick(reason=reason)
        await interaction.response.send_message(f"Kicked {member_obj.mention}. Reason: {reason}")
    except discord.errors.Forbidden:
        await interaction.response.send_message("I don't have permission to kick members!")
    except AttributeError:
        await interaction.response.send_message("Invalid user specified.")

@bot.tree.command(name="ban", description="Ban a user from your server.")
async def ban(interaction: discord.Interaction, member: str, *, reason: Optional[str] = None):
    guild = interaction.guild
    member_obj = discord.utils.get(guild.members, mention=member)
    try:
        await member_obj.ban(reason=reason)
        await interaction.response.send_message(f"Banned {member_obj.mention}. Reason: {reason}")
    except discord.errors.Forbidden:
        await interaction.response.send_message("I don't have permission to ban members!")
    except AttributeError:
        await interaction.response.send_message("Invalid user specified.")


bot.run(TOKEN)