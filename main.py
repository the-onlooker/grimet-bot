import discord
from discord import app_commands
from discord.ext import commands
import aiohttp
 
TOKEN = "MTEwMDE2NDI0NjU1NTMzMjY5OQ.GvjjdM.Xn9kYz3zZn7J8O4e5ZnvpEa1swp2gyy9ABZ8lU"
API_KEY = "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"

bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("GPT-Bot is up!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)

@bot.command()
async def gpt(ctx: commands.Context, *, prompt: str):
    async with aiohttp.ClientSession() as session:
        payload = {
            "model": "text-davinci-003",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 10000,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,
        }
        headers = {"Authorization": f"Bearer {API_KEY}"}
        async with session.post("https://api.openai.com/v1/completions", json=payload, headers=headers) as resp:
            response = await resp.json()
            embed = discord.Embed(title="Chat GPT's Response:", description=response["choices"][0]["text"])
            await ctx.reply(embed=embed)

bot.run(TOKEN)